import os

from flask import Flask
from sqlalchemy.sql import text
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager

from .model import *
from .database import database, migrate
from .route.user_route import user_bp
from .route.product_route import product_bp
from .route.category_route import category_bp
from .route.user_auth_route import user_auth_bp

load_dotenv()

app = Flask(__name__)

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")

app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

database.init_app(app)
migrate.init_app(app, database)

jwt = JWTManager(app)

app.register_blueprint(product_bp)
app.register_blueprint(category_bp)
app.register_blueprint(user_bp)
app.register_blueprint(user_auth_bp)


@app.route("/")
def hello_world():
    return {"message": "Welcome to Ecommerce API!"}
