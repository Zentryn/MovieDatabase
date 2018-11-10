from flask import redirect, render_template, url_for
from application import app

@app.route("/")
def index():
    return redirect(url_for("movies"))