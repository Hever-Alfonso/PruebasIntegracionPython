
class DiscountEngine:
    # Regla: >=300 → 20%, >=100 → 10%, >=50 → 5%, otro → 0%
    def discount_for(self, subtotal: float) -> float:
        if subtotal >= 300.0:
            return 0.20
        if subtotal >= 100.0:
            return 0.10
        if subtotal >= 50.0:
            return 0.05
        return 0.0
