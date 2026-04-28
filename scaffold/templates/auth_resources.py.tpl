# Auth resources here
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.blueprint.auth.service import AuthService
from flask import request, jsonify

auth_service = AuthService()


class RegisterResource(Resource):
    def post(self):
        data = requests.get_json()
        message, status = auth_service.register(data)
        return jsonify(message, status)


class LoginResource(Resource):
    def post(self):
        pass


class RefreshResource(Resource):
    @jwt_required(refresh=True)
    def post(self):
        pass


class LogoutResource(Resource):
    def post(self):
        pass


class PasswordResetRequestResource(Resource):
    def post(self):
        pass


class PasswordResetConfirmResource(Resource):
    def post(self):
        pass


class MeResource(Resource):
    @jwt_required()
    def post(self):
        pass
