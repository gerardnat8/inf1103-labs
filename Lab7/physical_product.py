from product import Product


class PhysicalProduct(Product):
    """A product that is stored in a warehouse and has to be shipped."""

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

    def display_information(self):
        """Parent prints the common line, then this class adds the weight."""
        super().display_information()
        print(f"    Weight: {self.__weight:.2f} kg")

    def display_details(self):
        """Parent prints the common block, then this class adds the weight."""
        super().display_details()
        print(f"Weight: {self.__weight:.2f} kg")
        print(f"Fulfilment: {self.get_fulfilment_info()}")