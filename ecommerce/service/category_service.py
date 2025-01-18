from ..model.category import Category


class CategoryService:
    """A category service class."""

    @classmethod
    def get_category_by_id(cls, id: int):
        """A function to get category by ID."""

        category: Category = Category.query.get(id)

        return category

    @classmethod
    def get_categories(cls):
        """A function to get a list of category."""

        categories: list[Category] = Category.query.all()

        return categories
