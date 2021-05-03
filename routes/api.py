from flask import current_app, Blueprint, request, render_template, jsonify

from modules.data import getReviews, getProducts, getSocialMedias, getOpeningTimes, isOpen

bp = Blueprint("api", __name__, url_prefix="/api")


@bp.route("/")
def index():
    return jsonify(data=[i.endpoint for i in current_app.url_map.iter_rules()])

@bp.route("/products")
def products():
    return jsonify(
        success=True,
        data=getProducts()
    )

@bp.route("/reviews")
def reviews():
    return jsonify(
        success=True,
        data=getReviews()
    )

@bp.route("/social-medias")
def social_medias():
    return jsonify(
        success=True,
        data=getSocialMedias()
    )

@bp.route("/opening-times")
def opening_times():
    data = getOpeningTimes()
    data["isOpen"] = isOpen()

    return jsonify(
        success=True,
        data=data
    )