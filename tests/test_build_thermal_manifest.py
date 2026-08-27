import csv
import tempfile
import unittest
from pathlib import Path

from scripts.build_thermal_manifest import build_manifest, write_outputs


class ThermalManifestTests(unittest.TestCase):
    def test_matches_left_and_right_png_txt_pairs(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            left = root / "C01_왼쪽"
            right = root / "C02_오른쪽"
            (left / "텍스트파일").mkdir(parents=True)
            (right / "텍스트파일").mkdir(parents=True)

            serial = "H2032509301621B220012S000"
            for view, directory in (("1", left), ("3", left), ("2", right), ("4", right)):
                (directory / f"{serial} _{view}.png").touch()
                (directory / "텍스트파일" / f"{serial} _{view}.txt").touch()

            rows = build_manifest(left, right)

            self.assertEqual(len(rows), 4)
            self.assertTrue(all(row["match_status"] == "matched" for row in rows))
            self.assertEqual({row["expected_side"] for row in rows if row["view_id"] in {"1", "3"}}, {"left"})
            self.assertEqual({row["expected_side"] for row in rows if row["view_id"] in {"2", "4"}}, {"right"})

    def test_records_a_missing_txt_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            left = root / "C01_왼쪽"
            right = root / "C02_오른쪽"
            left.mkdir()
            right.mkdir()
            (left / "H2032509301621B220012S000 _1.png").touch()

            rows = build_manifest(left, right)

            self.assertEqual(rows[0]["match_status"], "missing_txt")
            summary = write_outputs(rows, root / "thermal_manifest.csv")
            self.assertEqual(summary["status_counts"], {"missing_txt": 1})
            with (root / "thermal_manifest.csv").open(encoding="utf-8") as file:
                self.assertEqual(next(csv.DictReader(file))["view_id"], "1")


if __name__ == "__main__":
    unittest.main()
