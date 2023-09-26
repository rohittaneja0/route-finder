from flask import Flask
from flask_restful import Resource
import time

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from support_functions.graph_maker import Graph, solver  # pylint: disable=E402 # noqa: E402

# Creating an engine to query on Entitlement Engine Database
# UGengine = create_engine(app_config.variables.sql_server_string_read)
# UGSession = scoped_session(sessionmaker(bind=UGengine))
# s = UGSession()

class RouteFinder(Resource):

    @classmethod
    def get(cls, site):

        return {"message": f"Hello World, '{site}'"}