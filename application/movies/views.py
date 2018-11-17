from flask import render_template, request, redirect, url_for
from flask_login import login_required

from application import app, db
from application.movies.models import Movie
from application.movies.forms import MovieForm

@app.route("/movies/new", methods=["GET"])
@login_required
def new_movie_form():
    return render_template("movies/new_movie.html", form = MovieForm())

@app.route("/movies/new", methods=["POST"])
def add_movie():
    form = MovieForm(request.form)

    if not form.validate():
        return render_template("movies/new_movie.html", form = form)

    mov = Movie(form.title.data, form.poster_url.data)

    db.session().add(mov)
    db.session().commit()

    return redirect(url_for("movies"))

@app.route("/movies", methods=["GET"])
@login_required
def movies():
    return render_template("movies/movies.html", movies = Movie.query.all())

@app.route("/movies/<movie_id>", methods=["GET"])
@login_required
def movie_info(movie_id):
    form = MovieForm()
    movie = Movie.query.get(movie_id)

    form.id.data = movie_id
    form.title.data = movie.title
    form.poster_url.data = movie.poster_url

    return render_template("movies/movie.html", form = form)

@app.route("/movies/update_movie", methods=["POST"])
def update_movie():
    form = MovieForm(request.form)

    if not form.validate():
        return render_template("movies/movie.html", form = form)

    db.session().query(Movie)\
    .filter(Movie.id == request.form.get("id"))\
    .update({"title": request.form.get("title"), "poster_url": request.form.get("poster_url")})
    
    db.session().commit()

    return redirect(url_for("movies"))

@app.route("/movies/delete_movie", methods=["POST"])
def delete_movie():
    db.session().query(Movie)\
    .filter(Movie.id == request.form.get("id"))\
    .delete()

    db.session().commit()

    return redirect(url_for("movies"))
