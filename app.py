import json
from dotenv import load_dotenv
from flask import Flask, Response
from flask_injector import FlaskInjector
from flask_restful import Api
from injector import Injector

from src.pokeberry.application.get_all_berry_stats import GetAllBerryStats
from src.pokeberry.infrastructure.pokeberry_dependency_container import PokeberryDependencyContainer

load_dotenv()

app = Flask(__name__)
api = Api(app)


@app.route("/")
def index():
    return Response(
        mimetype="application/json",
        response=json.dumps("Welcome to Pokeberries API"),
        status=200,
    )


injector = Injector()
injector.binder.install(PokeberryDependencyContainer(injector))

api.add_resource(GetAllBerryStats, "/allBerryStats")

FlaskInjector(app=app, injector=injector)
