from flask import request
from ..model import Product

from ..service.product_service import ProductService


class ProductController:

    product_service = ProductService()

    def get_products(self):
        products = self.product_service.get_products()

        if not products:
            return {"message": "Products not found."}, 404

        return [
            {
                "id": product.id,
                "name": product.name,
                "description": product.description,
                "price": product.price,
                "stock_quantity": product.stock_quantity,
                "brand": product.brand,
                "weight": product.weight,
                "dimension": product.dimension,
                "color": product.color,
            }
            for product in products
        ], 200

    def get_product(self, id: int):
        product = self.product_service.get_product_by_id(id=id)

        if not product:
            return {"message": "Product not found."}, 404

        return {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "stock_quantity": product.stock_quantity,
            "brand": product.brand,
            "weight": product.weight,
            "dimension": product.dimension,
            "color": product.color,
        }, 200

    def add_product(self):
        product = request.get_json()

        if not product:
            return {"message": "No product provided."}, 400

        try:
            new_product = self.product_service.add_product(product)
            return {
                "id": new_product.id,
                "name": new_product.name,
                "description": new_product.description,
                "price": new_product.price,
                "stock_quantity": new_product.stock_quantity,
                "brand": new_product.brand,
                "weight": new_product.weight,
                "dimension": new_product.dimension,
                "color": new_product.color,
            }, 201
        except Exception as e:
            return ({"error": str(e)}), 500

    def delete_product(self, id: int):
        product = self.product_service.delete_product_by_id(id=id)

        if product is None:
            return {"message": "Product not found."}, 404

        return "", 204
