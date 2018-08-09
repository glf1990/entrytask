from flask import jsonify
from app.code import Code


def make_result(data="entrytest", code=Code.SUCCESS_CODE):
    return jsonify({"error_code": code,  "error_messag": Code.msg[code],"reference":data})
