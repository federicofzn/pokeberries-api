import json
from dotenv import load_dotenv
from flask import Flask, Response
from flask_injector import FlaskInjector
from injector import Injector

from src.pokeberry.infrastructure.pokeberry_dependency_container import PokeberryDependencyContainer

load_dotenv()

app = Flask(__name__)


@app.route("/")
def index():
    return Response(
        mimetype="application/json",
        response=json.dumps("Welcome to Pokeberries API"),
        status=200,
    )


injector = Injector()
injector.binder.install(PokeberryDependencyContainer(injector))

FlaskInjector(app=app, injector=injector)


if __name__ == "__main__":
    app.run(debug=True)
