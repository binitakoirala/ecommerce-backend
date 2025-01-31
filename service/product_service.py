from ..model.product import Product
from ..database import database


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

    @classmethod
    def add_product(cls, product: dict) -> Product:
        """A function to add a new product."""
        new_product = Product(
            name=product.get("name"),
            description=product.get("description"),
            price=product.get("price"),
            stock_quantity=product.get("stock_quantity"),
            brand=product.get("brand"),
            weight=product.get("weight"),
            dimension=product.get("dimension"),
            color=product.get("color"),
        )

        try:
            database.session.add(new_product)
            database.session.commit()
            return new_product
        except Exception as e:
            database.session.rollback()
            raise e

    @classmethod
    def delete_product_by_id(cls, id: int):
        """A function to delete product by ID."""

        product: Product = Product.query.get(id)

        if product is None:
            return None

        Product.query.filter_by(id=id).delete()

        database.session.commit()

        return product
