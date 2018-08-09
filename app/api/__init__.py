from .view import Test
from flask_restful import Api
from flask import Blueprint

api = Blueprint("api", __name__) 
resource = Api(api)
resource.add_resource(Test, "/shopee/test")
