"""Initialize Flask App."""
import os
from flask import Flask
from flaskInvestingApp.config import Config
from dotenv import load_dotenv
# from flask_sqlalchemy import SQLAlchemy

# Globally accessible libraries
# db = SQLAlchemy()


def create_app(config=Config):
    """Create Flask app."""
    app = Flask(__name__)
    app.config.from_object(config)

    # bring in .env file
    APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
    dotenv_path = os.path.join(APP_ROOT, '.env')
    load_dotenv(dotenv_path)

    # Initialize plugins
    # db.init_app(app)

    with app.app_context():
        # Import parts of our application
        from .home import home

        # Register blueprints
        app.register_blueprint(home.home_bp)
        print(app.secret_key)
        print(app.debug)

        return app