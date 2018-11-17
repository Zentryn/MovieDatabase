from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/login.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username = form.username.data, password = form.password.data).first()
    if not user:
        return render_template("auth/login.html", form = form, error = "Username or password is incorrect.")

    login_user(user)
    return redirect(url_for("movies"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("auth_login"))

@app.route("/auth/register", methods = ["GET", "POST"])
def auth_register():
    if request.method == "GET":
        return render_template("auth/register.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username = form.username.data).first()
    if user:
        return render_template("auth/register.html", form = LoginForm(), error = "That username is already taken.")

    user = User(form.username.data, form.password.data)
    db.session().add(user)
    db.session().commit()

    login_user(user)
    return redirect(url_for("movies"))