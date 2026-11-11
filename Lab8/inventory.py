from product import Product


class Inventory:
    """Groups Product objects (aggregation). It holds references to products but does
    not create them or control their lifecycle, so a Product can outlive or leave it."""

    def __init__(self) -> None:
        self.__products: list[Product] = []

    def add_product(self, product: Product) -> bool:
        """Store a Product. Returns True if added, False if its ID already exists."""
        if self.find_product(product.get_product_id()) is not None:
            return False
        self.__products.append(product)
        return True

    def remove_product(self, product_id: str) -> Product | None:
        """Remove the reference to this product and hand the Product back.
        The Product itself is not destroyed. Returns None if it is not found."""
        product = self.find_product(product_id)
        if product is not None:
            self.__products.remove(product)
        return product

    def find_product(self, product_id: str) -> Product | None:
        """Return the Product with this ID (any letter case), or None if not found."""
        wanted = str(product_id).strip().upper()
        for product in self.__products:
            if product.get_product_id() == wanted:
                return product
        return None

    def display_all(self) -> None:
        """Print every product. Each product prints itself (polymorphism)."""
        print("Current Inventory")
        print("-" * 48)
        if not self.__products:
            print("No products in inventory.")
        for product in self.__products:
            product.display_information()
        print("-" * 48)

    def get_all_products(self) -> list[Product]:
        """Return a copy of the product list (so outside code cannot change the original)."""
        return list(self.__products)