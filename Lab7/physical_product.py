from can_be_shipped import CanBeShipped
from product import Product


class PhysicalProduct(Product, CanBeShipped):
    """A product that is stored in a warehouse and has to be shipped."""

    BASE_SHIPPING_FEE = 5.00
    FEE_PER_KG = 2.00

    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        weight = float(weight)
        if weight < 0:
            raise ValueError("Weight cannot be negative.")
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def get_fulfilment_info(self):
        return "Physical product: packed in the warehouse and shipped to the customer."

    def calculate_shipping_cost(self):
        """Shipping is a flat fee plus a charge for every kilogram."""
        return self.BASE_SHIPPING_FEE + self.FEE_PER_KG * self.__weight

    def display_information(self):
        """Parent prints the common line, then this class adds the weight."""
        super().display_information()
        print(f"    Weight: {self.__weight:.2f} kg")

    def display_details(self):
        """Parent prints the common block, then this class adds the weight and shipping."""
        super().display_details()
        print(f"Weight: {self.__weight:.2f} kg")
        print(f"Shipping Cost: ${self.calculate_shipping_cost():.2f}")
        print(f"Fulfilment: {self.get_fulfilment_info()}")