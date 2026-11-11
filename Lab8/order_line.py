from product import Product


class OrderLine:
    """One product and a quantity inside an Order. An Order creates and manages its
    lines (composition), so nothing outside Order should create or move an OrderLine.
    It only refers to its Product (association) and does not own it."""

    def __init__(self, product: Product, quantity: int) -> None:
        if not isinstance(product, Product):
            raise TypeError("product must be a Product object.")
        if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
            raise ValueError("Quantity must be a whole number greater than 0.")
        self.__product: Product = product
        self.__quantity: int = quantity

    def get_product(self) -> Product:
        return self.__product

    def get_quantity(self) -> int:
        return self.__quantity

    def calculate_subtotal(self) -> float:
        """Price of the product multiplied by the quantity."""
        return self.__product.get_price() * self.__quantity

    def display_information(self) -> None:
        print(f"{self.__product.get_name()} x {self.__quantity} "
              f"@ ${self.__product.get_price():.2f} = ${self.calculate_subtotal():.2f}")