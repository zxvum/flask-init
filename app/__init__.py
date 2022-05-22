from flask import Flask
from app.routes import routes
from app.models import db

from flask_migrate import Migrate

app = Flask(__name__)
app.register_blueprint(routes)

db.init_app(app)
migrate = Migrate(app, db)