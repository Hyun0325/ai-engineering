"""Create a file-level manifest for streamed thermal research data.

The script reads file names and metadata only. It never copies, moves, or
modifies the source PNG/TXT files stored in Google Drive.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path


FILE_PATTERN = re.compile(r"^(?P<serial>.+?)\s+_(?P<view>[1-4])\.(?P<extension>png|txt)$", re.IGNORECASE)
EXPECTED_SIDE = {"1": "left", "2": "right", "3": "left", "4": "right"}
MANIFEST_COLUMNS = [
    "material_serial",
    "view_id",
    "expected_side",
    "image_path",
    "txt_path",
    "image_exists",
    "txt_exists",
    "image_source_side",
    "txt_source_side",
    "match_status",
]


def discover_files(directory: Path, source_side: str) -> dict[tuple[str, str], dict[str, str]]:
    """Return PNG/TXT paths keyed by (material serial, view id)."""
    records: dict[tuple[str, str], dict[str, str]] = {}

    for path in directory.rglob("*"):
        if not path.is_file():
            continue

        match = FILE_PATTERN.match(path.name)
        if not match:
            continue

        key = (match.group("serial"), match.group("view"))
        extension = match.group("extension").lower()
        record = records.setdefault(key, {})
        path_key = f"{extension}_path"
        side_key = f"{extension}_source_side"

        if path_key in record:
            raise ValueError(f"Duplicate {extension.upper()} file for {key}: {path}")

        record[path_key] = str(path.resolve())
        record[side_key] = source_side

    return records


def build_manifest(left_dir: Path, right_dir: Path) -> list[dict[str, str]]:
    """Build one manifest row per observed serial/view combination."""
    combined: dict[tuple[str, str], dict[str, str]] = {}

    for source_side, directory in (("left", left_dir), ("right", right_dir)):
        for key, record in discover_files(directory, source_side).items():
            target = combined.setdefault(key, {})
            for field, value in record.items():
                if field in target:
                    raise ValueError(f"Duplicate file type for {key}: {field}")
                target[field] = value

    rows: list[dict[str, str]] = []
    for (serial, view), record in sorted(combined.items()):
        expected_side = EXPECTED_SIDE[view]
        image_exists = "png_path" in record
        txt_exists = "txt_path" in record
        observed_sides = {
            record.get("png_source_side"),
            record.get("txt_source_side"),
        } - {None}

        if observed_sides and observed_sides != {expected_side}:
            status = "unexpected_side"
        elif image_exists and txt_exists:
            status = "matched"
        elif image_exists:
            status = "missing_txt"
        else:
            status = "missing_png"

        rows.append(
            {
                "material_serial": serial,
                "view_id": view,
                "expected_side": expected_side,
                "image_path": record.get("png_path", ""),
                "txt_path": record.get("txt_path", ""),
                "image_exists": str(image_exists).lower(),
                "txt_exists": str(txt_exists).lower(),
                "image_source_side": record.get("png_source_side", ""),
                "txt_source_side": record.get("txt_source_side", ""),
                "match_status": status,
            }
        )

    return rows


def write_outputs(rows: list[dict[str, str]], output_path: Path) -> dict[str, object]:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=MANIFEST_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)

    status_counts = Counter(row["match_status"] for row in rows)
    summary = {
        "manifest_path": str(output_path.resolve()),
        "total_serial_view_records": len(rows),
        "unique_material_serials": len({row["material_serial"] for row in rows}),
        "png_files": sum(row["image_exists"] == "true" for row in rows),
        "txt_files": sum(row["txt_exists"] == "true" for row in rows),
        "status_counts": dict(sorted(status_counts.items())),
    }
    summary_path = output_path.with_name(f"{output_path.stem}_summary.json")
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return summary


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a PNG/TXT thermal-data manifest without copying source files.")
    parser.add_argument("--left-dir", type=Path, required=True, help="C01 left-camera folder in Google Drive.")
    parser.add_argument("--right-dir", type=Path, required=True, help="C02 right-camera folder in Google Drive.")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/manifests/thermal_manifest.csv"),
        help="CSV output path. Defaults to an ignored local data directory.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_arguments()
    if not args.left_dir.is_dir() or not args.right_dir.is_dir():
        raise SystemExit("Both --left-dir and --right-dir must be existing Drive folders.")

    rows = build_manifest(args.left_dir, args.right_dir)
    summary = write_outputs(rows, args.output)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
