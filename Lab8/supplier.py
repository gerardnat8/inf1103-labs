class Supplier:
    """A company that supplies products. A Supplier exists on its own, so it is only
    associated with the products it supplies (no ownership either way)."""

    def __init__(self, supplier_id: str, name: str, contact_email: str) -> None:
        supplier_id = str(supplier_id).strip().upper()
        name = str(name).strip()
        contact_email = str(contact_email).strip()
        if not supplier_id:
            raise ValueError("Supplier ID cannot be empty.")
        if not name:
            raise ValueError("Supplier name cannot be empty.")
        self.__supplier_id: str = supplier_id
        self.__name: str = name
        self.__contact_email: str = contact_email

    def get_supplier_id(self) -> str:
        return self.__supplier_id

    def get_name(self) -> str:
        return self.__name

    def get_contact_email(self) -> str:
        return self.__contact_email

    def display_information(self) -> None:
        """Print the supplier on one line."""
        print(f"Supplier ID: {self.__supplier_id} | Name: {self.__name} | "
              f"Email: {self.__contact_email}")