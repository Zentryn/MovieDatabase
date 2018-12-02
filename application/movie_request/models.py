from application import db
from application.models import Base

class MovieRequest(Base):
    movie_id = db.Integer()
    account_id = db.Integer()

    def __init__(self, movie_id, account_id):
        self.movie_id = movie_id
        self.account_id = account_id
