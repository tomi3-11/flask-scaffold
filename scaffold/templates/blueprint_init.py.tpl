from flask import Blueprint
from app.blueprints.{{blueprint_name}}.routes import register_routes

{{blueprint_name}}_bp = Blueprint("{{blueprint_name}}", __name__, url_prefix="/api/{{blueprint_name}}")

register_routes({{blueprint_name}}_bp)


