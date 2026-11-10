"""Textile Dye House Recipe Formulation, Liquor Ratio & Chemical Batching Engine."""

from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field


class DyeChemical(BaseModel):
    chemical_name: str
    dosing_pct_or_gpl: float  # Percentage on weight of fabric (% owf) or grams per liter (g/l)
    is_percentage_owf: bool = True  # True if % owf, False if grams per liter (g/l)
    unit_cost_per_kg: float


class DyeingBatchOrder(BaseModel):
    batch_no: str
    shade_name: str  # e.g., Navy Blue Pantone 19-4028
    fabric_type: str  # 100% Cotton Single Jersey, Poly-Cotton, Viscose
    fabric_weight_kg: float
    liquor_ratio: float = 8.0  # 1:8 ratio (1 kg fabric to 8 Liters water)
    dyes_and_auxiliaries: List[DyeChemical]


class BatchDispensingSheet(BaseModel):
    batch_no: str
    fabric_weight_kg: float
    total_water_liters: float
    chemical_requirements: List[Dict[str, Any]]
    total_recipe_cost: float
    cost_per_kg_fabric: float


class TextileDyeingEngine:
    """Computes exact dye formulation weight in grams and total water bath volume."""

    def calculate_dispensing_sheet(self, order: DyeingBatchOrder) -> BatchDispensingSheet:
        # Total water in dyeing vessel (Fabric weight * liquor ratio)
        total_water_liters = order.fabric_weight_kg * order.liquor_ratio
        
        reqs = []
        total_cost = 0.0

        for item in order.dyes_and_auxiliaries:
            if item.is_percentage_owf:
                # Weight of dye (kg) = (fabric_weight_kg * pct) / 100
                qty_kg = (order.fabric_weight_kg * item.dosing_pct_or_gpl) / 100.0
            else:
                # Grams per liter (g/l) -> Qty in kg = (gpl * total_water_liters) / 1000
                qty_kg = (item.dosing_pct_or_gpl * total_water_liters) / 1000.0

            qty_grams = round(qty_kg * 1000.0, 2)
            cost = round(qty_kg * item.unit_cost_per_kg, 2)
            total_cost += cost

            reqs.append({
                "chemical": item.chemical_name,
                "dosing_input": item.dosing_pct_or_gpl,
                "type": "% owf" if item.is_percentage_owf else "g/L",
                "required_grams": qty_grams,
                "required_kg": round(qty_kg, 3),
                "cost": cost
            })

        cost_per_kg = round(total_cost / order.fabric_weight_kg, 2) if order.fabric_weight_kg > 0 else 0.0

        return BatchDispensingSheet(
            batch_no=order.batch_no,
            fabric_weight_kg=order.fabric_weight_kg,
            total_water_liters=round(total_water_liters, 1),
            chemical_requirements=reqs,
            total_recipe_cost=round(total_cost, 2),
            cost_per_kg_fabric=cost_per_kg
        )
