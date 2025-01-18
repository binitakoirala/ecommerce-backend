from ..model.product import Product


class ProductService:
    """A product service class."""

    @classmethod
    def get_product_by_id(cls, id: int):
        """A function to get product by ID."""

        product: Product = Product.query.get(id)

        return product

    @classmethod
    def get_products(cls):
        """A function to get a list of products."""

        products: list[Product] = Product.query.all()

        return products
