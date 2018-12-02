from application import db
from application.models import Base

class Director(Base):
    name = db.Column(db.String(150), nullable = False)
    movies = db.relationship("Movie", back_populates = "director")

    def __init__(self, name):
        self.name = name