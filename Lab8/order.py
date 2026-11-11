from order_line import OrderLine
from product import Product


class Order:
    """A customer order. It is composed of OrderLine objects: it creates them itself
    and they are removed together with the order. No method accepts a ready-made
    OrderLine, so a line can never be moved into a different Order."""

    def __init__(self, order_id: str) -> None:
        self.__order_id: str = str(order_id).strip().upper()
        self.__order_lines: list[OrderLine] = []

    def get_order_id(self) -> str:
        return self.__order_id

    def get_order_lines(self) -> list[OrderLine]:
        """Return a copy of the list of lines (so outside code cannot change the original)."""
        return list(self.__order_lines)

    def add_order_line(self, product: Product, quantity: int) -> None:
        """The Order creates the OrderLine itself from a Product and a quantity."""
        self.__order_lines.append(OrderLine(product, quantity))

    def remove_order_line(self, product_id: str) -> bool:
        """Remove the first line for this product ID. Returns False if there is none."""
        wanted = str(product_id).strip().upper()
        for line in self.__order_lines:
            if line.get_product().get_product_id() == wanted:
                self.__order_lines.remove(line)
                return True
        return False

    def calculate_total(self) -> float:
        """Ask every OrderLine for its subtotal and add them up."""
        return sum((line.calculate_subtotal() for line in self.__order_lines), 0.0)

    def display_information(self) -> None:
        print(f"Order {self.__order_id}")
        print("-" * 48)
        if not self.__order_lines:
            print("No order lines.")
        for line in self.__order_lines:
            line.display_information()
        print("-" * 48)
        print(f"Total: ${self.calculate_total():.2f}")