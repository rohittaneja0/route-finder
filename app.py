from flask import Flask
from flask_restful import Api
from flasgger import Swagger
from db import db
import os
from resources.route_finder import RouteFinder

# add azure auth
app = Flask(__name__)

@app.before_first_request
def create_tables():
    db.create_all()

swagger = Swagger(app)
api = Api(app)

api.add_resource(RouteFinder, '/routefinder/<site>')

db.init_app(app)

if "__main__" == __name__:
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')
