from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User

router = Blueprint("router", __name__, template_folder="templates")


@router.route('/')
def index():
    return render_template("app.html")

@router.route('/login', methods=("GET", "POST"))
def login():
    if request.method == "POST":
        return request.form
    return render_template("login.html")

@router.route('/register', methods=("GET", "POST"))
def register():
    if request.method == "POST":
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')

        user = User.query.filter_by(
            email=email).first()  # if this returns a user, then the email already exists in database

        if user:  # if a user is found, we want to redirect back to signup page so user can try again
            return redirect(url_for('auth.signup'))

        # create a new user with the form data. Hash the password so the plaintext version isn't saved.
        new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

        # add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template("register.html")