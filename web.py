from flask import Flask, render_template

def createApp():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return render_template("pages/index.html")

    return app

if __name__ == "__main__":
    createApp().run(host="0.0.0.0", port=80, debug=True)