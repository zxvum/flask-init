from app.routes import routes
from flask import render_template, request

@routes.route('/')
def index():
    return render_template("index.html")

@routes.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == "POST":
        return request.form

    return render_template("auth/login.html")