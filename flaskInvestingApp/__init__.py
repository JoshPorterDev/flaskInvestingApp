"""Initialize Flask App."""
from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# Globally accessible libraries
# db = SQLAlchemy()


def create_app():
    """Create Flask app."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # Initialize plugins
    # db.init_app(app)

    with app.app_context():
        # Import parts of our application
        from .home import home

        # Register blueprints
        app.register_blueprint(home.home_bp)

        return app