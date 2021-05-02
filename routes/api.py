from flask import Blueprint, jsonify

bp = Blueprint("api", __name__, url_prefix="/api")

@bp.route("/products")
def products():
    return jsonify(
        success=True,
        data=[
            {
                "title": "Super Cupcakes",
                "img": "https://sophiaskitchen.blog/wp-content/uploads/2017/07/IMG_4477-e1501525659741.jpg",
                "description": "A unicorn cupcake",
                "slug": "super-cupcakes",
                "url": "",
                "inStock": True
            }
        ]
    )