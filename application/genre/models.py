from application import db
from application.models import Base

class Genre(Base):
    name = db.Column(db.String(150), nullable = False)

    def __init__(self, name):
        self.name = name