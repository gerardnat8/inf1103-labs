from product import Product
 
 
class Inventory:
    """Manages a collection of Product objects (Single Responsibility)."""
 
    def __init__(self):
        self.__products = []
 
    def add_product(self, product):
        """Store a Product. Returns True if added, False if its ID already exists."""
        if self.search_product(product.get_product_id()) is not None:
            return False
        self.__products.append(product)
        return True
 
    def search_product(self, product_id):
        """Return the Product with this ID (any letter case), or None if not found."""
        wanted = str(product_id).strip().upper()
        for product in self.__products:
            if product.get_product_id() == wanted:
                return product
        return None
 
    def display_all(self):
        """Print every product."""
        print("Current Inventory")
        print("-" * 48)
        if not self.__products:
            print("No products in inventory.")
        for product in self.__products:
            product.display_information()
        print("-" * 48)
 
    def get_all_products(self):
        """Return a copy of the product list (so outside code cannot change the original)."""
        return list(self.__products)