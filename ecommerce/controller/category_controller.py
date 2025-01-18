from ..model import Category
from ..database import database

from ..service.category_service import CategoryService


class CategoryController:

    category_service = CategoryService()

    def get_categories(self):
        categories = self.category_service.get_categories()

        if not categories:
            return {"message": "Categories not found."}, 404

        return [
            {
                "id": category.id,
                "name": category.name,
                "description": category.description,
                "created_at": category.created_at,
                "updated_at": category.updated_at,
            }
            for category in categories
        ], 200

    def get_category(self, id: int):
        category = self.category_service.get_category_by_id(id=id)

        if not category:
            return {"message": "Category not found."}, 404

        return {
            "id": category.id,
            "name": category.name,
            "description": category.description,
            "created_at": category.created_at,
        }, 200


# @category_bp.route("/", methods=["POST"])
# def add_category():
#     category = request.get_json()
#     if not category:
#         return jsonify({
#             "error": "No category provided"
#         }), 400

#     new_category = Category(
#         name= category.get("name"),
#         description= category.get("description")
#     )
#     try:
#          database.session.add(new_category)
#          database.session.commit()
#          return jsonify({
#             "id": new_category.id,
#             "name": new_category.name,
#             "description": new_category.description
#          }), 201
#     except Exception as e:
#         database.session.rollback()
#         return jsonify({"error": str(e)}), 500

# @category_bp.route("/<int:id>", methods=["DELETE"])
# def delete_category(id: int):
#     category = Category.query.get(id)
#     database.session.delete(category)
#     database.session.commit()
#     return("Category deleted successfully!")
