from dataclasses import dataclass


@dataclass
class Contact:
    id: int
    name: str
    cell_phone: str
    email: str
