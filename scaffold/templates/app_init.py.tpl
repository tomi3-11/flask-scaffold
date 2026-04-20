from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from config import DevelopmentConfig, ProductionConfig, TestingConfig

db = SQLAlchemy()
migrate = Migrate()

config_map = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
}

def create_app(config_object=None):
    app = Flask(__name__)
    env = os.getenv("FLASK_ENV", "development")

    if config_object:
        app.config.from_object(config_object)
    else:
        app.config.from_object(config_map.get(env, DevelopmentConfig))

    # extension initializations
    db.init_app(app)
    migrate.init_app(app, db)

    # register blueprints
    from app.blueprints.{{blueprint_name}} import {{blueprint_name}}_bp
    app.register_blueprint({{blueprint_name}}_bp

    # Registers an authentication blueprint if user choose to have auth
    {% if include_auth %}
    from app.blueprints.auth import auth_bp
    app.register_blueprint(auth_bp)
    {% endif %}

    {% for bp in extra_blueprints %}
    from app.blueprints.{{bp}} import {{bp}}_bp
    app.register_blueprint({{bp}}_bp)
    {% endof %}

    return app
