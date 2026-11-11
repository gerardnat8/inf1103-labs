from product import Product
from supplier import Supplier


class DigitalProduct(Product):
    """A product that is delivered as a download."""

    def __init__(self, product_id: str, name: str, price: float, stock: int,
                 supplier: Supplier, download_size: float) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        download_size = float(download_size)
        if download_size < 0:
            raise ValueError("Download size cannot be negative.")
        self.__download_size: float = download_size

    def get_download_size(self) -> float:
        return self.__download_size

    def get_fulfilment_info(self) -> str:
        return "Digital product: delivered to the customer as a download."

    def display_information(self) -> None:
        """Parent prints the common line, then this class adds the download size."""
        super().display_information()
        print(f"    Download Size: {self.__download_size:.2f} MB")

    def display_details(self) -> None:
        """Parent prints the common block, then this class adds the download size."""
        super().display_details()
        print(f"Download Size: {self.__download_size:.2f} MB")
        print(f"Fulfilment: {self.get_fulfilment_info()}")