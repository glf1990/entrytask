from flask_restful import Resource

from app.util import make_result
from .parser import parser


class Test(Resource):
    def get(self):
        req = parser.parse_args(strict=True)
        a = req.get("a")
        b = req.get("b")
        return make_result(data=str(a)+b)
