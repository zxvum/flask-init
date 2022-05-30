# from flask import redirect, url_for
# from werkzeug.security import generate_password_hash, check_password_hash
# from app import db
#
# def create_user(user):
#     name = user.get('name')
#     email = user.get('email')
#     password = user.get('password')
#     user = User.query.filter_by(email=email).first()
#
#     if user:
#         return redirect(url_for('register'))
#
#     new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
#
#     db.session.add(new_user)
#     db.session.commit()
#
#     return redirect(url_for('login'))