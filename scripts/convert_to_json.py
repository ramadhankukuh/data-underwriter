import pandas as pd
import json
from pathlib import Path

input_csv = Path("data/underwriters.csv")
output_json = Path("data/ipo.json")

if not input_csv.exists():
    raise FileNotFoundError(f"Tidak menemukan {input_csv}, cek nama file dari Kaggle")

# Load CSV
df = pd.read_csv(input_csv)

# Export ke JSON
df.to_json(output_json, orient="records", indent=2, force_ascii=False)

print(f"✅ JSON berhasil dibuat: {output_json}")
