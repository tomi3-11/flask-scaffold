from flask import Blueprint
from app.blueprint.auth.routes import register_routes

auth_bp = Blueprint("auth", __name__, url_prefix="/auth)

register_routes(auth_bp)
