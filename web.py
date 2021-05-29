from flask import Flask, render_template, url_for, request

from routes import blueprints
from modules.data import getProducts, getReviews, getSocialMedias, getOpeningTimes, isOpen, Enquiries

from re import findall,sub

enquiriesApi = Enquiries()

def createApp():
    app = Flask(__name__)
    app.static_folder = "public"

    app.jinja_env.globals.update({
        "getProducts": getProducts,
        "getReviews": getReviews,
        "getSocialMedias": getSocialMedias,
        "getOpeningTimes": getOpeningTimes,
        "isOpen": isOpen,
        "getEndpoints": lambda: [i for i in app.url_map.iter_rules() if not i.endpoint == "static"],
        "len": len,
        "enumerate": enumerate,
        "zip": zip
    })

    @app.route("/")
    def index():
        return render_template("pages/index.html")

    @app.route("/tray-bakes")
    def trayBakes():
        return "Tray Bakes"

    @app.route("/special-occasions")
    def specialOccasions():
        return "Special Occasions"

    @app.route("/contact", methods=["GET", "POST"])
    def contact():
        if request.method == "POST":
            print(request.form)
            enquiriesApi.add(**request.form)
        return render_template("pages/contact.html")

    for i in blueprints:
        app.register_blueprint(i)

    return app

if __name__ == "__main__":
    createApp().run(host="0.0.0.0", port=80, debug=True)