from flask_restful import Resource
from app.blueprints.{{blueprint_name}} import HelloService
from flask import jsonify


class HelloResource:
    def get(self):
        message, status = HelloService.get_hello()
        return jsonify(message, status)
