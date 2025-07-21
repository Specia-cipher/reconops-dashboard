from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    
    # Basic config
    app.config['SECRET_KEY'] = 'super-secret-key-change-me'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reconops.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Init extensions
    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)

    # Register blueprints
    from reconops_dashboard.routes.main_routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from reconops_dashboard.routes.settings_routes import settings_bp as settings_blueprint
    app.register_blueprint(settings_blueprint, url_prefix='/settings')

    return app
