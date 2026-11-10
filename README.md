# ERPNext Textile Dyeing Recipe Manager 🧵🎨

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![ERPNext](https://img.shields.io/badge/ERPNext-v14%20%7C%20v15-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Build](https://img.shields.io/badge/Build-Passing-brightgreen.svg)

An industrial dye house chemical formulation, Pantone lab dip, and liquor ratio dispensing manager for **ERPNext Manufacturing & Textile Mills** (Tirupur, Surat, Ludhiana garment clusters).

---

## 🚀 Key Features

- **Liquor Ratio (M:L) Water Volume Calculation**: Computes exact bath liters according to machine capacity (1:5 to 1:10 liquor ratio).
- **Dual Dosing Mode**: Supports percentage on weight of fabric (`% owf`) for reactive/disperse dyes, and grams per liter (`g/L`) for salts and fixing alkalis.
- **Precision Recipe Costing**: Computes batch dispensing weight down to grams and exact chemical cost per kilogram of dyed fabric.
- **Automated Bill of Materials (BOM)**: Generates ERPNext production BOM items for seamless stock ledger issue.

---

## 📦 Installation & Setup

```bash
git clone https://github.com/shyampandey1104/erpnext-textile-dyeing-recipe-manager.git
cd erpnext-textile-dyeing-recipe-manager
pip install -r requirements.txt
```

---

## 🛠️ Usage Example

```python
from dyeing.engine import TextileDyeingEngine, DyeingBatchOrder, DyeChemical

engine = TextileDyeingEngine()

order = DyeingBatchOrder(
    batch_no="BATCH-2026-NAVY",
    shade_name="Pantone 19-4028",
    fabric_type="Cotton Single Jersey",
    fabric_weight_kg=250.0,
    liquor_ratio=8.0,
    dyes_and_auxiliaries=[
        DyeChemical(chemical_name="Reactive Navy Blue", dosing_pct_or_gpl=3.0, is_percentage_owf=True, unit_cost_per_kg=650.0),
        DyeChemical(chemical_name="Glauber Salt", dosing_pct_or_gpl=60.0, is_percentage_owf=False, unit_cost_per_kg=22.0)
    ]
)

sheet = engine.calculate_dispensing_sheet(order)
print(f"Total Water: {sheet.total_water_liters} L | Cost/kg: ₹{sheet.cost_per_kg_fabric}")
```

---

## 🧪 Testing

```bash
pytest tests/
```

---

## 📄 License
MIT License. Created with ❤️ by [Shyam Pandey](https://github.com/shyampandey1104).
