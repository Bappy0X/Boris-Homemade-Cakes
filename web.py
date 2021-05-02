from flask import Flask, render_template

from routes import blueprints
from modules.data import getProducts, getReviews, getSocialMedias, isOpen

def createApp():
    app = Flask(__name__)
    app.static_folder = "public"

    app.jinja_env.globals.update({
        "getProducts": getProducts,
        "getReviews": getReviews,
        "getSocialMedias": getSocialMedias,
        "isOpen": isOpen,
        "zip": zip,
        "enumerate": enumerate
    })

    @app.route("/")
    def index():
        return render_template("pages/index.html")

    for i in blueprints:
        app.register_blueprint(i)

    return app

if __name__ == "__main__":
    createApp().run(host="0.0.0.0", port=80, debug=True)