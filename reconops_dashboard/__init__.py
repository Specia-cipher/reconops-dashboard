from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import and register blueprints
    from reconops_dashboard.routes.main import main
    app.register_blueprint(main)

    return app
