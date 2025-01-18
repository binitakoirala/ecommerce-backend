from ..model import Product

# from flask import Blueprint, request, jsonify
from ..database import database

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


# @product_bp.route("/", methods=["POST"])
# def add_product():
#     product = request.get_json()
#     if not product:
#         return jsonify({
#             "error": "No product provided."
#         }), 400

#     new_product = Product(
#         name= product.get("name"),
#         description= product.get("description"),
#         price= product.get("price"),
#         stock_quantity= product.get("stock_quantity"),
#         brand= product.get("brand"),
#         weight= product.get("weight"),
#         dimension= product.get("dimension"),
#         color= product.get("color")
#     )

#     try:
#         database.session.add(new_product)
#         database.session.commit()
#         return jsonify ({
#             "id": new_product.id,
#             "name": new_product.name,
#             "description": new_product.description,
#             "price": new_product.price,
#             "stock_quantity": new_product.stock_quantity,
#             "brand": new_product.brand,
#             "weight": new_product.weight,
#             "dimension": new_product.dimension,
#             "color": new_product.color
#         }), 201
#     except Exception as e:
#         database.session.rollback()
#         return jsonify({"error": str(e)}), 500

# @product_bp.route("/<int:id>", methods=["DELETE"])
# def delete_product(id:int):
#     product = Product.query.get(id)
#     database.session.delete(product)
#     database.session.commit()
#     return("Product deleted successfully!")
