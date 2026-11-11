from abc import ABC, abstractmethod

from supplier import Supplier


class Product(ABC):
    """Abstract base for every product. Each product knows its one Supplier (association)."""

    def __init__(self, product_id: str, name: str, price: float, stock: int,
                 supplier: Supplier) -> None:
        price = float(price)
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if not self.__is_valid_quantity(stock):
            raise ValueError("Stock must be a whole number that is 0 or more.")
        if not isinstance(supplier, Supplier):
            raise TypeError("supplier must be a Supplier object.")
        self.__product_id: str = str(product_id).strip().upper()
        self.__name: str = str(name).strip()
        self.__price: float = price
        self.__stock: int = stock
        self.__supplier: Supplier = supplier

    @staticmethod
    def __is_valid_quantity(quantity: int) -> bool:
        """A valid stock level is a whole number (not True/False) that is 0 or more."""
        return isinstance(quantity, int) and not isinstance(quantity, bool) and quantity >= 0

    def get_product_id(self) -> str:
        return self.__product_id

    def get_name(self) -> str:
        return self.__name

    def get_price(self) -> float:
        return self.__price

    def get_stock(self) -> int:
        return self.__stock

    def get_supplier(self) -> Supplier:
        return self.__supplier

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        """Return a message explaining how this product gets to the customer."""

    def update_stock(self, quantity: int) -> bool:
        """Set the stock to a new level. Returns True if accepted, False if invalid."""
        if not self.__is_valid_quantity(quantity):
            return False
        self.__stock = quantity
        return True

    def display_information(self) -> None:
        """Print this product on one line (used when listing every product)."""
        print(f"ID: {self.__product_id} | Name: {self.__name} | "
              f"Price: ${self.__price:.2f} | Stock: {self.__stock}")

    def display_details(self) -> None:
        """Print this product as a detailed block (used by Search)."""
        print("-" * 48)
        print(f"ID: {self.__product_id}")
        print(f"Name: {self.__name}")
        print(f"Price: ${self.__price:.2f}")
        print(f"Stock: {self.__stock}")
        print(f"Supplier: {self.__supplier.get_name()} ({self.__supplier.get_supplier_id()})")
        print("-" * 48)