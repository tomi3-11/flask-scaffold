from flask_restful import Api
from app.blueprint.auth.resources import (
    RegisterResource,
    LoginResource,
    LogoutResource,
    PasswordResetRequestResource,
    PasswordResetConfirmResource,
    MeResource,
    RefreshResource
)

def register_routes(bp):
    api = Api(bp)

    # Add resources
    api.add_resource(RegisterResource, "/register")
    api.add_resource(LoginResource, "/login")
    api.add_resource(LogoutResource, "/logout")
    api.add_resource(MeResource, "/me")
    api.add_resource(PasswordResetRequestResource, "/reset/request")
    api.add_resource(PasswordResetConfirmResource, "/reset/confirm")
    api.add_resource(RefreshResource, "/token/refresh")
