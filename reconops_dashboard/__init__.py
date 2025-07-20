from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # SECRET_KEY for sessions and flash
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'super-secret-key-change-me'

    # SQLite database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reconops.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Register Blueprints
    from reconops_dashboard.routes.main_routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
