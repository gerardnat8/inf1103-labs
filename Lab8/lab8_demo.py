from digital_product import DigitalProduct
from inventory import Inventory
from order import Order
from physical_product import PhysicalProduct
from product import Product
from supplier import Supplier


def show_product_details(product: Product) -> None:
    """Works for ANY Product. It never checks which subclass it was given (LSP)."""
    product.display_information()
    print(product.get_fulfilment_info())


def section(title: str) -> None:
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def main() -> None:
    section("2. ASSOCIATION: Supplier and Product")
    supplier = Supplier("s1", "Acme Supplies", "sales@acme.com")
    guitar = PhysicalProduct("g1", "Guitar", 499.90, 3, supplier, 3.5)
    game = DigitalProduct("d1", "Game", 59.90, 100, supplier, 4200)
    print("Supplier shown through the guitar:")
    guitar.get_supplier().display_information()
    print("Supplier shown through the game:")
    game.get_supplier().display_information()
    print("Both products share the same Supplier object:",
          guitar.get_supplier() is game.get_supplier())
    del supplier
    print("\nAfter del supplier, the guitar can still show its supplier:")
    guitar.get_supplier().display_information()

    section("3. AGGREGATION: Inventory and Product")
    inventory_a = Inventory()
    inventory_b = Inventory()
    inventory_a.add_product(guitar)
    print("Guitar is in Inventory A:", inventory_a.find_product("g1") is guitar)
    removed = inventory_a.remove_product("g1")
    print("Removed from Inventory A, got the same object back:", removed is guitar)
    print("Inventory A still has the guitar:", inventory_a.find_product("g1") is not None)
    print("The guitar still works on its own:")
    guitar.display_information()
    inventory_b.add_product(guitar)
    print("Same guitar object is now in Inventory B:",
          inventory_b.find_product("g1") is guitar)

    section("4. COMPOSITION: Order and OrderLine")
    order_1 = Order("o1")
    order_1.add_order_line(guitar, 1)
    order_1.add_order_line(game, 2)
    order_1.display_information()
    order_2 = Order("o2")
    order_2.add_order_line(guitar, 1)
    line_1 = order_1.get_order_lines()[0]
    line_2 = order_2.get_order_lines()[0]
    print("\nSame guitar in two orders:")
    print("  Same OrderLine object?", line_1 is line_2)
    print("  Same Product object?  ", line_1.get_product() is line_2.get_product())
    order_1.remove_order_line("g1")
    print("After removing the guitar line from order 1, its total is:",
          f"${order_1.calculate_total():.2f}")
    print("The guitar product itself still exists:", guitar.get_name())

    section("6. LSP: one function, any Product")
    show_product_details(guitar)
    show_product_details(game)

    section("7. POLYMORPHISM: one loop, two product types")
    inventory = Inventory()
    inventory.add_product(guitar)
    inventory.add_product(game)
    for product in inventory.get_all_products():
        product.display_information()
        print(product.get_fulfilment_info())


if __name__ == "__main__":
    main()