import os
import pandas as pd
from pathlib import Path

data_folder = Path("data")
output_json = Path("data/ipo.json")

# Cari file CSV hasil download dari Kaggle
csv_files = [f for f in os.listdir(data_folder) if f.lower().endswith(".csv")]

if not csv_files:
    raise FileNotFoundError(f"Tidak menemukan file CSV di {data_folder}")

# Prioritaskan file yang mengandung "Underwriter" atau "e-IPO"
csv_target = None
for f in csv_files:
    if "underwriter" in f.lower() or "e-ipo" in f.lower():
        csv_target = f
        break

# Kalau tidak ada yang match, pakai file pertama
if csv_target is None:
    csv_target = csv_files[0]

input_csv = data_folder / csv_target

print(f"📂 Membaca file: {input_csv}")

# Baca CSV dan simpan ke JSON
df = pd.read_csv(input_csv)
df.to_json(output_json, orient="records", indent=2, force_ascii=False)

print(f"✅ JSON berhasil dibuat: {output_json}")
