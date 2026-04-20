from flask_restful import Api
from app.blueprints.{{blueprint_name}}.resources import HelloResource

def register_routes(bp):
    api = Api(bp)

    # register routes with the resources
    api.add_resource(HelloResource, "/")
