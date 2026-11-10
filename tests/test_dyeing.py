import unittest
from dyeing.engine import TextileDyeingEngine, DyeingBatchOrder, DyeChemical


class TestTextileDyeingEngine(unittest.TestCase):
    def setUp(self):
        self.engine = TextileDyeingEngine()

    def test_dispensing_sheet(self):
        order = DyeingBatchOrder(
            batch_no="BATCH-COTTON-801",
            shade_name="Royal Navy Blue",
            fabric_type="100% Combed Cotton",
            fabric_weight_kg=500.0,
            liquor_ratio=6.0,  # 500 * 6 = 3000 Liters
            dyes_and_auxiliaries=[
                DyeChemical(chemical_name="Reactive Blue RGB", dosing_pct_or_gpl=2.5, is_percentage_owf=True, unit_cost_per_kg=600.0),
                DyeChemical(chemical_name="Glauber Salt (Electrolyte)", dosing_pct_or_gpl=50.0, is_percentage_owf=False, unit_cost_per_kg=25.0),
                DyeChemical(chemical_name="Soda Ash (Fixing Alkali)", dosing_pct_or_gpl=15.0, is_percentage_owf=False, unit_cost_per_kg=35.0),
            ]
        )

        sheet = self.engine.calculate_dispensing_sheet(order)
        self.assertEqual(sheet.total_water_liters, 3000.0)
        # 500 kg * 2.5% = 12.5 kg = 12500 grams of reactive dye
        self.assertEqual(sheet.chemical_requirements[0]["required_grams"], 12500.0)
        # 50 g/L * 3000 L = 150000 grams = 150 kg Glauber salt
        self.assertEqual(sheet.chemical_requirements[1]["required_kg"], 150.0)
        self.assertGreater(sheet.total_recipe_cost, 0)


if __name__ == "__main__":
    unittest.main()
