## Database Overview

The database consists of 6 tables and uses PostgreSQL on Heroku and SQLite when the project is ran locally. Here is a brief overview of each of them and provided are also SQL queries for creating them.

### Base table
This isn't an actual table in the database but it is a base for all other tables, which is why it's listed here. All other tables have the columns that this tables does.
```
CREATE TABLE base (
    id INTEGER PRIMARY KEY,
    date_created DateTime,
    date_modified DateTime
)
```

### Movie
The movie table contains data of a singular movie.

_title_: The title of the movie

_poster_url_: URL to the movie's poster image

_backdrop_url_: URL to the movie's backdrop image

_plot_: A plot summary of the movie

_validated_: A flag that tells if the movie should be shown in the application

_director_id_: ID of the director that directed this movie

```
CREATE TABLE movie (
    title VARCHAR(150),
    poster_url VARCHAR(255),
    backdrop_url VARCHAR(255),
    plot VARCHAR(1000),
    validated BOOLEAN,
    director_id INTEGER,
    FOREIGN KEY(director_id) REFERENCES director(id)
)
```

### Director
The director table contains the name of a director

_name_: The name of the director

```
CREATE TABLE director (
    name VARCHAR(150)
)
```

### Genre
The genre table contains the name of a genre

_name_: The name of the genre

```
CREATE TABLE genre (
    name VARCHAR(150)
)
```

### Account
The account table contains information about a user of the application

_username_: The username of the user

_password_: The user's password

_role_: The user's role. Can be either _USER_ or _ADMIN_

```
CREATE TABLE account (
    username VARCHAR(144),
    password VARCHAR(144),
    role VARCHAR(144)
)
```

### Movie_Account

The movie_account table is a connection table between an account and a movie and is used for storing information about user's favorited movies

_movie_id_: ID of the movie that an account is linked to

_account_id: ID of the account that a movie is linked to

```
CREATE TABLE movie_account (
    movie_id INTEGER,
    account_id INTEGER,
    FOREIGN KEY(movie_id) REFERENCES movie(id),
    FOREIGN KEY(account_id) REFERENCES account(id)
)
```

### Movie_Genre

The movie_genre table is a connection table between a movie and a genre. It's used for storing the genres that a movie has.

_movie_id_: ID of the movie that a genre is linked to

_genre_id_: ID of the genre that a movie is linked to

```
CREATE TABLE movie_genre (
    movie_id INTEGER,
    genre_id INTEGER,
    FOREIGN KEY(movie_id) REFERENCES movie(id),
    FOREIGN KEY(genre_id) REFERENCES genre(id)
)
```
