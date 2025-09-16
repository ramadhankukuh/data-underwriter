import pandas as pd
import os
import json

# Folder data hasil download Kaggle
data_dir = "data"
input_csv = os.path.join(data_dir, "Underwriter - e-IPO Data.csv")
output_json = os.path.join(data_dir, "ipo.json")

if not os.path.exists(input_csv):
    raise FileNotFoundError(f"Tidak menemukan {input_csv}, cek nama file hasil Kaggle")

# Baca CSV
df = pd.read_csv(input_csv)

# Konversi ke list of dict
records = df.to_dict(orient="records")

# Simpan ke JSON
with open(output_json, "w", encoding="utf-8") as f:
    json.dump(records, f, ensure_ascii=False, indent=2)

print(f"✅ Berhasil konversi {len(records)} baris ke {output_json}")
