from application import db
from application.models import Base
from sqlalchemy.sql import text, exists

movie_genre = db.Table('movie_genre', Base.metadata,
    db.Column('movie_id', db.Integer, db.ForeignKey('movie.id')),
    db.Column('genre_id', db.Integer, db.ForeignKey('genre.id'))
)

class Movie(Base):
    title = db.Column(db.String(150), nullable = False)
    poster_url = db.Column(db.String(255), nullable = False)
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'), nullable = False)
    director = db.relationship("Director", back_populates = "movies")
    plot = db.Column(db.String(1000), nullable = False)
    genres = db.relationship("Genre", secondary=movie_genre, back_populates="movies")

    def __init__(self, title, poster_url, director_name, plot, genres, id = None):
        self.title = title
        self.plot = plot
        self.poster_url = poster_url

        self.set_director(director_name)
        self.set_genres(genres)

        if id is not None:
            self.id = id

    # Sets the director for this movie by a name
    def set_director(self, director_name):
        existing_director = db.session().query(Director).filter(Director.name == director_name)
        if existing_director.count() == 0:
            new_director = Director(director_name)
            db.session().add(new_director)
            db.session().commit()

        existing_director = db.session().query(Director).filter(Director.name == director_name).first()
        self.director_id = existing_director.id
        self.director = existing_director
        existing_director.movies.append(self)

    # Adds a list of genres to this movie's genres
    def set_genres(self, genres):
        # Clear genres
        self.genres[:] = []

        for genre_name in genres:
            genre_name = genre_name.lstrip().rstrip()
            existing_genre = db.session().query(Genre).filter(Genre.name == genre_name)

            # Add genre if it doesn't exist
            if existing_genre.count() == 0:
                new_genre = Genre(genre_name)
                db.session().add(new_genre)
                db.session().commit()

            # Get genre object and add to genres
            genre = db.session().query(Genre).filter(Genre.name == genre_name).first()
            self.genres.append(genre)

    # Creates a text version of genres and returns it
    def get_genres_text(self):
        genres_text = ""
        for genre in self.genres:
            genres_text += genre.name + ", "
        genres_text = genres_text[:-2]
        return genres_text

    @staticmethod
    def search_movies(search_text):
        search_text = search_text.lower()
        statement = text("SELECT Movie.id FROM Movie, Genre, Director, movie_genre "
                         "WHERE (movie_genre.movie_id = Movie.id AND movie_genre.genre_id = Genre.id AND lower(Genre.name) = :search_text) "
                         "OR (Movie.director_id = Director.id AND lower(Director.name) = :search_text) "
                         "OR lower(Movie.title) = :search_text")\
                         .params(search_text=search_text)

        res = db.engine.execute(statement)
        movies = []
        for row in res:
            mov = Movie.query.filter_by(id=row[0]).first()
            if mov is not None and not mov in movies:
                movies.append(mov)

        return movies

class Director(Base):
    name = db.Column(db.String(150), nullable = False)
    movies = db.relationship("Movie", back_populates = "director")

    def __init__(self, name):
        self.name = name

class Genre(Base):
    name = db.Column(db.String(150), nullable = False)
    movies = db.relationship("Movie", secondary=movie_genre, back_populates="genres")

    def __init__(self, name):
        self.name = name
