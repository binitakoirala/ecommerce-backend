from flask import request, jsonify
from ..model import user_auth
from ..database import database
from ..service.user_auth_service import UserAuthService


class UserAuthController:
    user_auth_service = UserAuthService()

    def login_user(self):
        login_request = request.get_json()

        email = login_request.get("email")
        password = login_request.get("password")

        if not email or not password:
            return jsonify({"message": "Email and password is required."}), 400

        tokens = self.user_auth_service.login(email=email, password=password)

        if not tokens:
            return {"message": "Invalid email or password."}, 401

        return jsonify(tokens), 200
