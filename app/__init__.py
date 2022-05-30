from flask import Flask
from app.routes import router
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.register_blueprint(router)
app.config.from_object("config")


db = SQLAlchemy()
db.init_app(app)
from app.models import User

with app.app_context():
    db.create_all()