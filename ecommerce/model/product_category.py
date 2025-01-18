from ecommerce.main import database


class ProductCategory(database.Model):
    product_id = database.Column(database.Integer, database.ForeignKey("product.id"), nullable=False)
    category_id = database.Column(database.Integer, database.ForeignKey("category.id"), nullable=False)
