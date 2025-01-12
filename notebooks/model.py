# Notebook parsing_simple_sites.ipynb

from dataclasses import dataclass

@dataclass
class Product:
    sku: int
    name: str
    link: str
    price: float