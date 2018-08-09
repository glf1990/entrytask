from flask_restful.reqparse import RequestParser

parser = RequestParser()
parser.add_argument("a", type=int, location="args", required=True)
parser.add_argument("b", type=str, location="args", required=True)
