from application import db
from application.models import Base

class User(Base):
    __tablename__ = "account"

    username = db.Column(db.String(144), nullable = False)
    password = db.Column(db.String(144), nullable = False)
    role = db.Column(db.String(144))

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
