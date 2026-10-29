class Product:
    """Represents one product and manages its own state (Single Responsibility)."""
 
    def __init__(self, product_id, name, price, stock):
        price = float(price)
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if not self.__is_valid_quantity(stock):
            raise ValueError("Stock must be a whole number that is 0 or more.")
 
        self.__product_id = str(product_id).strip().upper()
        self.__name = str(name).strip()
        self.__price = price
        self.__stock = stock

    
    @staticmethod
    def __is_valid_quantity(quantity):
        """A valid stock level is a whole number (not True/False) that is 0 or more."""
        return isinstance(quantity, int) and not isinstance(quantity, bool) and quantity >= 0

    
    # ----- read-only access (the main program never touches the attributes directly) -----
    def get_product_id(self):
        return self.__product_id
 
    def get_name(self):
        return self.__name
 
    def get_price(self):
        return self.__price
 
    def get_stock(self):
        return self.__stock


    # ----- behaviour -----
    def update_stock(self, quantity):
        """Set the stock to a new level. Returns True if accepted, False if invalid."""
        if not self.__is_valid_quantity(quantity):
            return False
        self.__stock = quantity
        return True
 
    def display_information(self):
        """Print this product on one line (used when listing every product)."""
        print(f"ID: {self.__product_id} | Name: {self.__name} | "
              f"Price: ${self.__price:.2f} | Stock: {self.__stock}")
 
    def display_details(self):
        """Print this product as a detailed block (used by Search)."""
        print("-" * 48)
        print(f"ID: {self.__product_id}")
        print(f"Name: {self.__name}")
        print(f"Price: ${self.__price:.2f}")
        print(f"Stock: {self.__stock}")
        print("-" * 48)
 