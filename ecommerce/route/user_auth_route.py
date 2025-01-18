from flask import Blueprint, request, jsonify
from ..controller.user_auth_controller import UserAuthController

user_auth_controller = UserAuthController()

user_auth_bp = Blueprint("user_auth_bp", __name__, url_prefix="/login")

user_auth_bp.route("/", methods=["POST"])(user_auth_controller.login_user)
