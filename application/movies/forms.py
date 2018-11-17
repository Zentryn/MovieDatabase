from flask_wtf import FlaskForm
from wtforms import StringField, validators

class MovieForm(FlaskForm):
    id = StringField("Movie ID", render_kw={"style": "display: none;"})
    title = StringField("Movie Title", [validators.Length(min=2)], id="input-title", render_kw={"placeholder": "Movie Title"})
    poster_url = StringField("Poster URL", [validators.Regexp("^.*jpg|.*png$", message="URL has to an image."), validators.Length(min=5)], id="input-poster", render_kw={"placeholder": "Poster URL"})

    class Meta:
        csrf = False