from application import db
from application.models import Base
from application.movies.models import Movie

movie_account = db.Table('movie_account', Base.metadata,
    db.Column('movie_id', db.Integer, db.ForeignKey('movie.id')),
    db.Column('account_id', db.Integer, db.ForeignKey('account.id'))
)

class User(Base):
    __tablename__ = "account"

    username = db.Column(db.String(144), nullable = False)
    password = db.Column(db.String(144), nullable = False)
    role = db.Column(db.String(144))
    favorite_movies = db.relationship("Movie", secondary = movie_account)

    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role;

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        return self.role
