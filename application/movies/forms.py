from flask_wtf import FlaskForm
from wtforms import StringField, validators, TextAreaField

class MovieForm(FlaskForm):
    id = StringField("Movie ID", render_kw={"style": "display: none;"})
    title = StringField("Movie Title", [validators.Length(min=2, max=150)], id="input-title", render_kw={"placeholder": "Movie Title"})
    poster_url = StringField(
        "Poster URL",
        [
            validators.Regexp("^.*jpg|.*png$",
            message="Poster URL has to an image."),
            validators.Length(min=5, max=255)
        ],
        id="input-poster",
        render_kw={"placeholder": "Poster URL"}
    )

    backdrop_url = StringField(
        "Backdrop URL",
        [
            validators.Regexp("^.*jpg|.*png$", message="Backdrop URL has to an image."),
            validators.Length(min=5, max=255)
        ],
        id="input-backdrop",
        render_kw={"placeholder": "Backdrop URL"}
    )
    
    plot = TextAreaField("Plot", [validators.Length(min=15, max=1000)], id="input-plot", render_kw={"placeholder": "Movie Plot"})
    director = StringField("Director", [validators.Length(min=5, max=150)], id="input-director", render_kw={"placeholder": "Movie Director"})
    genres = StringField("Genres", [validators.Length(min=5, max=150)], id="input-genres", render_kw={"placeholder": "Genres seperated by a comma"})

    class Meta:
        csrf = False