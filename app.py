import json
from dotenv import load_dotenv
from flask import Flask, Response

load_dotenv()

app = Flask(__name__)


@app.route("/")
def index():
    return Response(
        mimetype="application/json",
        response=json.dumps("Welcome to Pokeberries API"),
        status=200,
    )


if __name__ == "__main__":
    app.run(debug=True)
