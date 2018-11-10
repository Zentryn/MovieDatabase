from application import app, db
from flask import render_template, request, redirect, url_for
from application.movies.models import Movie

@app.route("/movies/new")
def new_movie_form():
    return render_template("movies/new_movie.html")

@app.route("/movies", methods=["GET"])
def movies():
    return render_template("movies/movies.html", movies = Movie.query.all())

@app.route("/movies/<movie_id>", methods=["GET"])
def movie_info(movie_id):
    return render_template("movies/movie.html", movie = Movie.query.get(movie_id))

@app.route("/movies/update_movie", methods=["POST"])
def update_movie():
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

@app.route("/movies", methods=["POST"])
def add_movie():
    mov = Movie(request.form.get("title"), request.form.get("poster_url"))

    db.session().add(mov)
    db.session().commit()

    return redirect(url_for("movies"))
