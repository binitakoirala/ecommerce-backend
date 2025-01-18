from flask import Blueprint, request, jsonify
from ..controller.category_controller import CategoryController

category_controller = CategoryController()

category_bp = Blueprint("category_bp", __name__, url_prefix="/categories")

category_bp.route("/", methods=["GET"])(category_controller.get_categories)


category_bp.route("/<int:id>", methods=["GET"])(category_controller.get_category)
