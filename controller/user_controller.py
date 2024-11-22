from flask import request

from ..model import Category
from ..database import database
from ..service.user_service import UserService


class UserController:

    user_service = UserService()

    def get_users(self):
        users = self.user_service.get_users()

        if not users:
            return {"message": "User not found."}, 404

        return [
            {
                "user_id": user.user_id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "dob": user.dob,
                "gender": user.gender,
                "address": user.address,
                "phone_number": user.phone_number,
                "role": user.role,
                "email": user.email,
                "status": user.status,
            }
            for user in users
        ], 200

    def get_user(self, id: int):
        user = self.user_service.get_user_by_id(id=id)

        if not user:
            return {"message": "User not found."}, 404

        return {
            "user_id": user.user_id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "dob": user.dob,
            "gender": user.gender,
            "address": user.address,
            "phone_number": user.phone_number,
            "role": user.role,
            "email": user.email,
            "status": user.status,
        }, 200

    def add_user(self):
        user_request: dict = request.get_json()
        print(user_request)
        response = self.user_service.create_user(user_detail=user_request)

        if not response:
            return {"message": "Unable to register user."}, 500

        return {"message": "User registration successful."}, 201


# @user_bp.route("/", methods=["POST"])
# def create_user():
#     user = request.get_json()
#     if not user:
#         return jsonify({
#             "error": "No input data provided"
#         }), 400

#     new_user = User(
#         first_name=user.get("first_name"),
#         last_name=user.get("last_name"),
#         dob=user.get("dob"),
#         gender=user.get("gender"),
#         address=user.get("address"),
#         phone_number=user.get("phone_number"),
#         role=user.get("role"),
#         email=user.get("email"),
#         status=user.get("status")
#     )

#     try:
#         database.session.add(new_user)
#         database.session.commit()
#         return jsonify({
#             "user_id": new_user.user_id,
#             "first_name": new_user.first_name,
#             "last_name": new_user.last_name,
#             "dob": new_user.dob,
#             "gender": new_user.gender,
#             "address": new_user.address,
#             "phone_number": new_user.phone_number,
#             "role": new_user.role,
#             "email": new_user.email,
#             "status": new_user.status
#         }), 201
#     except Exception as e:
#         database.session.rollback()
#         return jsonify({"error": str(e)}), 500

# @user_bp.route("/<int:id>", methods=["DELETE"])
# def delete_user(id: int):
#     user = User.query.get(id)
#     database.session.delete(user)
#     database.session.commit()
#     return("User deleted successfully!")
