#!/usr/local/bin/python3
from flask import Flask,abort,Response
import flask_restful
from app.api import api
from app.util import make_result 
from app.code import Code
app = Flask(__name__)
app.register_blueprint(api)
def my_abort(http_status_code, *args, **kwargs):
    if http_status_code == 400:
       abort(make_result(code=Code.PARAMS_ERRCODE))
    else:
       abort( make_result(code=Code.SYSTEM_ERRCODE))

flask_restful.abort = my_abort
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
