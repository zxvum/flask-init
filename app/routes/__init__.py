from flask import Blueprint

routes = Blueprint("routes", __name__, template_folder="app/templates")

from app.routes import urls