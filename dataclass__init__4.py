from dataclasses import dataclass

@dataclass
class InventoryItem:
    name: str
    price: float = 9.99
    quantity: int = 1

    def total_cost(self) -> float:
        return self.price * self.quantity


desk = InventoryItem('Desk', 1000, 12)
print(desk.total_cost())