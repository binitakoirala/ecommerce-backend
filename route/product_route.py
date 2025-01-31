from flask import Blueprint, request, jsonify
from ..controller.product_controller import ProductController

product_controller = ProductController()

product_bp = Blueprint("product_bp", __name__, url_prefix="/products")

product_bp.route("/", methods=["GET"])(product_controller.get_products)

product_bp.route("/<int:id>", methods=["GET"])(product_controller.get_product)

product_bp.route("/", methods=["POST"])(product_controller.add_product)

product_bp.route("/<int:id>", methods=["DELETE"])(product_controller.delete_product)
