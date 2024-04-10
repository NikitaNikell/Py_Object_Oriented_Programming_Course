from dataclasses import dataclass
from typing import List

@dataclass
class InventoryItem:
    name: str
    price: float = 9.99
    quantity: int = 1


@dataclass
class ProgramStaff:
    items: List[InventoryItem]


desk = InventoryItem('Desk', 1000, 12)
pen = InventoryItem('Pen')
monitor = InventoryItem('Monitor', quantity=2)

staff = ProgramStaff([desk, pen, monitor])
print(staff)