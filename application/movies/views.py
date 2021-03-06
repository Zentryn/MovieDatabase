from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db, login_required
from application.movies.models import Movie, movie_genre
from application.auth.models import User
from application.movies.forms import MovieForm

from sqlalchemy.sql import text

@app.route("/movies/new", methods=["GET"])
@login_required("ADMIN")
@login_required()
def new_movie_form():
    return render_template("movies/new_movie.html", form = MovieForm(), form_action = "/movies/new", button_text = "Add Movie")

@app.route("/movies/new", methods=["POST"])
@login_required("ADMIN")
def add_movie():
    form = MovieForm(request.form)

    if not form.validate():
        return render_template("movies/new_movie.html", form = form, form_action = request.form.get("form_action"), button_text = request.form.get("button_text"))

    # Get list of genres
    genres = form.genres.data.split(",")

    mov = Movie(form.title.data, form.poster_url.data, form.backdrop_url.data, form.director.data, form.plot.data, genres, True)

    db.session().add(mov)
    db.session().commit()

    return redirect(url_for("movies"))

@app.route("/movies/requested", methods=["GET"])
@login_required("ADMIN")
def list_requested_movies():
    movies = db.session().query(Movie).filter(Movie.validated == False).all()

    # Get a text version of genres
    for movie in movies:
        movie.genres_text = movie.get_genres_text()

    return render_template("movies/movies.html", movies = movies)

@app.route("/movies/favorited", methods=["GET"])
@login_required()
def list_favorited_movies():
    fav_mov_ids = []
    for mov in current_user.favorite_movies:
        fav_mov_ids.append(mov.id)

    movies = db.session().query(Movie).all()
    movs = []

    # Get a text version of genres
    for movie in movies:
        if movie.id in fav_mov_ids:
            movie.genres_text = movie.get_genres_text()
            movs.append(movie)

    return render_template("movies/movies.html", movies = movs)

@app.route("/movies/request", methods=["GET"])
@login_required()
def request_movie_form():
    return render_template("movies/new_movie.html", form = MovieForm(), form_action = "/movies/request", button_text = "Request Movie")

@app.route("/movies/request", methods=["POST"])
@login_required()
def request_movie():
    form = MovieForm(request.form)

    if not form.validate():
        return render_template("movies/new_movie.html", form = form, form_action = request.form.get("form_action"), button_text = request.form.get("button_text"))

    # Get list of genres
    genres = form.genres.data.split(",")

    mov = Movie(form.title.data, form.poster_url.data, form.backdrop_url.data, form.director.data, form.plot.data, genres, False)

    db.session().add(mov)
    db.session().commit()

    return redirect(url_for("movies"))

@app.route("/movies", methods=["GET"])
@login_required()
def movies():
    movies = db.session().query(Movie).filter(Movie.validated == True).all()

    # Get a text version of genres
    for movie in movies:
        movie.genres_text = movie.get_genres_text()

    return render_template("movies/movies.html", movies = movies)

@app.route("/movies/search", methods=["POST"])
@login_required()
def search_movies():
    movies = Movie.search_movies(request.form.get("search-input"))

    # Get a text version of genres
    for movie in movies:
        movie.genres_text = movie.get_genres_text()

    return render_template("movies/movies.html", movies = movies)

@app.route("/movies/<movie_id>", methods=["GET"])
@login_required()
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
    form.backdrop_url.data = movie.backdrop_url
    form.director.data = movie.director.name
    form.plot.data = movie.plot
    genres = movie.genres
    genres_text = ""

    fav_style = ""
    fav_content = "favorite_border"
    for fav_mov in current_user.favorite_movies:
        if fav_mov.id == int(movie_id):
            fav_style = "favorited"
            fav_content = "favorite"
            break

    counter = 0
    for genre in genres:
        genres_text += genre.name

        if counter < (len(genres) - 1):
            genres_text += ", "

        counter += 1

    movie.genres_text = genres_text

    form.genres.data = genres_text

    return render_template("movies/movie.html", form = form, movie = movie, form_action = "/movies/update_movie", fav_style = fav_style, fav_content = fav_content)

@app.route("/movies/update_movie", methods=["POST"])
@login_required("ADMIN")
def update_movie():
    form = MovieForm(request.form)
    mov = db.session().query(Movie)\
    .filter(Movie.id == request.form.get("id"))

    fav_style = ""
    fav_content = "favorite_border"
    for fav_mov in current_user.favorite_movies:
        if fav_mov.id == request.form.get("id"):
            fav_style = "favorited"
            fav_content = "favorite"
            break

    if not form.validate():
        return render_template("movies/movie.html", form = form, movie = mov, form_action = "/movies/update_movie", fav_style = fav_style, fav_content = fav_content)

    # Update genres and director
    mov.first().set_genres(request.form.get("genres").split(", "))
    mov.first().set_director(request.form.get("director"))

    # Update string datas
    mov.update(
        {
            "title": request.form.get("title"),
            "poster_url": request.form.get("poster_url"),
            "backdrop_url": request.form.get("backdrop_url"),
            "plot": request.form.get("plot")
        }
    )
    
    db.session().commit()

    return redirect(url_for("movies"))

@app.route("/movies/favorite", methods=["POST"])
@login_required()
def favorite_movie():
    movie_id = request.form.get("id")
    favorite = (request.form.get("favorite") == "false")

    mov = db.session().query(Movie)\
    .filter(Movie.id == movie_id).first()

    acc = db.session().query(User)\
    .filter(User.id == current_user.id)\
    .first()

    if (mov is not None):
        if favorite:
            acc.favorite_movies.append(mov)
        else:
            acc.favorite_movies.remove(mov)

    db.session().commit()

    return movie_info(movie_id)

@app.route("/movies/validate_movie", methods=["POST"])
@login_required("ADMIN")
def validate_movie():
    db.session().query(Movie)\
    .filter(Movie.id == request.form.get("id"))\
    .update({
        "validated": True
    })

    db.session().commit()
    return redirect(url_for("movies"))

@app.route("/movies/unvalidate_movie", methods=["POST"])
@login_required("ADMIN")
def unvalidate_movie():
    db.session().query(Movie)\
    .filter(Movie.id == request.form.get("id"))\
    .update({
        "validated": False
    })

    db.session().commit()
    return redirect(url_for("movies"))

@app.route("/movies/delete_movie", methods=["POST"])
@login_required("ADMIN")
def delete_movie():
    statement = text("DELETE FROM movie_genre WHERE movie_genre.movie_id = :movie_id")\
                    .params(movie_id=request.form.get("id"))

    db.engine.execute(statement)

    db.session().query(Movie)\
    .filter(Movie.id == request.form.get("id"))\
    .delete()

    print(request.form.get("id"))
    print(request.form.get("id"))
    print(request.form.get("id"))
    print(request.form.get("id"))

    db.session().commit()

    return redirect(url_for("movies"))
