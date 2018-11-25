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

    # Get list of genres
    genres = form.genres.data.split(",")

    mov = Movie(form.title.data, form.poster_url.data, form.director.data, form.plot.data, genres)

    db.session().add(mov)
    db.session().commit()

    return redirect(url_for("movies"))

@app.route("/movies", methods=["GET"])
@login_required
def movies():
    movies = Movie.query.all()

    # Get a text version of genres
    for movie in movies:
        movie.genres_text = movie.get_genres_text()

    return render_template("movies/movies.html", movies = movies)

@app.route("/movies/search", methods=["POST"])
@login_required
def search_movies():
    movies = Movie.search_movies(request.form.get("search-input"))

    # Get a text version of genres
    for movie in movies:
        movie.genres_text = movie.get_genres_text()

    return render_template("movies/movies.html", movies = movies)

@app.route("/movies/<movie_id>", methods=["GET"])
@login_required
def movie_info(movie_id):
    if movie_id is None:
        return redirect(url_for("movies"))

    form = MovieForm()
    movie = Movie.query.get(movie_id)

    if movie is None:
        return redirect(url_for("movies"))

    form.id.data = movie_id
    form.title.data = movie.title
    form.poster_url.data = movie.poster_url
    form.director.data = movie.director.name
    form.plot.data = movie.plot
    genres = movie.genres
    genres_text = ""

    for genre in genres:
        genres_text += genre.name + ", "

    form.genres.data = genres_text[:-2]

    return render_template("movies/movie.html", form = form)

@app.route("/movies/update_movie", methods=["POST"])
def update_movie():
    form = MovieForm(request.form)

    if not form.validate():
        return render_template("movies/movie.html", form = form)

    mov = db.session().query(Movie)\
    .filter(Movie.id == request.form.get("id"))

    # Update genres and director
    mov.first().set_genres(request.form.get("genres").split(", "))
    mov.first().set_director(request.form.get("director"))

    # Update string datas
    mov.update(
        {
            "title": request.form.get("title"),
            "poster_url": request.form.get("poster_url"),
            "plot": request.form.get("plot")
        }
    )
    
    db.session().commit()

    return redirect(url_for("movies"))

@app.route("/movies/delete_movie", methods=["POST"])
def delete_movie():
    db.session().query(Movie)\
    .filter(Movie.id == request.form.get("id"))\
    .delete()

    db.session().commit()

    return redirect(url_for("movies"))
