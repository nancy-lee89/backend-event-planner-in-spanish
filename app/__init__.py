from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_cors import CORS
import os

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "SQLALCHEMY_DATABASE_URI")

    # Import models here for Alembic setup
    # from app.models.ExampleModel import ExampleModel
    from app.models.contact_info import Contact_info
    from app.models.event_info import Event_info
    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    from app.routes.contact_info import contact_info_bp
    app.register_blueprint(contact_info_bp)
    # app.register_blueprint(example_bp)
    from app.routes.event_info import event_info_bp
    app.register_blueprint(event_info_bp)

    CORS(app)
    return app