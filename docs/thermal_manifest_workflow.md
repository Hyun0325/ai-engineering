# Thermal data manifest workflow

This workflow creates an inventory of the thermal research files without copying
or changing the original Google Drive data.

## Preconditions

1. In Google Drive for desktop, use **Stream files** rather than mirroring the
   research-data folder.
2. Locate the serial-labelled `C01_왼쪽` and `C02_오른쪽` folders in Finder.
3. Keep the output in the repository's ignored `data/` directory or in a private
   Drive folder. Do not commit a manifest containing confidential paths or labels.

## Run

Activate `pytorch_env`, then replace both sample paths with the actual Finder
paths for the streamed Drive folders.

```bash
python scripts/build_thermal_manifest.py \
  --left-dir "/path/to/Raw_data_extracted/데이터정리본_열화상이미지_시리얼라벨/C01_왼쪽" \
  --right-dir "/path/to/Raw_data_extracted/데이터정리본_열화상이미지_시리얼라벨/C02_오른쪽"
```

The script writes these ignored private outputs by default:

- `data/manifests/thermal_manifest.csv`
- `data/manifests/thermal_manifest_summary.json`

## Interpretation

Every manifest row represents one `material_serial + view_id` combination.

| View ID | Expected side |
| --- | --- |
| `_1`, `_3` | left (C01) |
| `_2`, `_4` | right (C02) |

`match_status` is `matched` only when the PNG and TXT have the same serial and
view ID on the expected side. Review `missing_png`, `missing_txt`, and
`unexpected_side` rows before using the data for train/validation/test splits.
