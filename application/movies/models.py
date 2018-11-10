from application import db

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date_added = db.Column(db.DateTime, default = db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default = db.func.current_timestamp(),
    onupdate = db.func.current_timestamp())

    title = db.Column(db.String(150), nullable = False)
    poster_url = db.Column(db.String(255), nullable = False)

    def __init__(self, title, poster_url, id = None):
        self.title = title
        self.poster_url = poster_url
        
        if id is not None:
            self.id = id