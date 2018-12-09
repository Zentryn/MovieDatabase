## Use Cases
This is a web application for adding, modifying, browsing, searching and otherwise handling movies.

The main page of the application shows a list of all movies that the application has. The movies are fetched with the following SQL query:
```
SELECT * FROM movie;
```

When clicking on a movie, the user enters the movie's page where they can see the artwork for the movie and some general information about the movie. The information about the specific movie is gotten with:
```
SELECT * FROM movie WHERE movie.id = (?);
```

From the movie's page the user can add the movie as a favorite, which will save it to their own library. The movie is added as a favorite with the following SQL query:
```
INSERT INTO movie_account (movie_id, account_id)
VALUES (?, ?);
```

Or alternatively, if the user is un-favoriting the movie, the following query is used:
```
DELETE FROM movie_account
WHERE movie_id = (?)
AND account_id = (?);
```

The user's favorited movies are shown in the "My Favorites" -tab, which simply lists all movies that a user has added to their favorites. The favorite movies are fetched with:
```
SELECT movie.* FROM movie, movie_account, account
WHERE movie_account.movie_id = movie.id
AND movie_account.account_id = account.id;
```

Normal users can also request new movies to be added to the application, which will then be seen by administrators. The movie requests are added into the database with:
```
INSERT INTO movie (title, poster_url, backdrop_url, director_id, plot, validated)
VALUES (?, ?, ?, ?, ?, False);
```

Administrators can then view the requested movies and make them visible to the application. The following query is used:
```
UPDATE movie
SET validated = True
WHERE movie.id = (?);
```

Administrators can also add movies that will be shown in the application straight away. The same query is used as when a normal user requests a new movie, but the _validated_ flag is set to _True_.

The application also features a search function. Movies can be searched using the title of the movie as well as names of genres and directors. The search is done with the following query:
```
SELECT movie.id FROM movie, genre, director, movie_genre
WHERE (
  movie_genre.movie_id = movie.id
  AND movie_genre.genre_id = genre.id
  AND genre.name = (?)
)
OR (
  movie.director_id = director.id
  AND director.name = (?)
)
OR movie.title = (?)
```
