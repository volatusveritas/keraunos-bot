from threading import Thread

from flask import Flask


app = Flask(__name__)


@app.route("/")
def home():
    return "[Flask] Keraunos is online."


def run():
    app.run(host="0.0.0.0", port=8080)


def keep_alive():
    t = Thread(target=run, daemon=True)
    t.start()
