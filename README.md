## Movie Database

A movie database web-application to browse and search for movies as well 
as add them as favorites or adding new movies with admin priviledges.

Includes:
* Registration
* Login
* Browing and viewing movies
* Searching for movies
* Adding new movies and editing existing movie information with admin 
priviledges
* Adding movies as favorites
* Requesting a movie to be added as a normal user

[Click here to see the live application](https://movie-database-hy-2018.herokuapp.com)
* To access the application, register yourself an account by clicking the link on the login page
* You can try out administrative features by logging in with "admin" as username and password

[Usecases](https://github.com/Zentryn/MovieDatabase/blob/master/documentation/Usecases.md)

[Database Overview](https://github.com/Zentryn/MovieDatabase/blob/master/documentation/Database.png)

## Installing
To install the application, first clone the repository to your local machine
```
git clone git@github.com:Zentryn/MovieDatabase.git
```

Then create a virtual environment and activate it using
```
python3 -m venv venv
source venv/Scripts/activate
```

Then, install dependencies using
```
pip install -r requirements.txt
```

You can now start up the application by running _run.py_
```
python3 run.py
```
The application will now be running at _localhost:5000_

## Usage
To start using the application, register yourself an account via the link on the login page.

As a normal user you can browse existing movies and request new ones via the link in the navigation bar. Requested movies will be seen by administrators and can then be accepted by them. Normal users can also add movies as favorites which saves them to a personal 'library'.

Administrators can also edit and delete existing movies on their individual pages.

To create yourself an admin account, you have you connect to the database and create the account from there, using "ADMIN" as role. For example:
```
sqlite3 ./application/movies.db
INSERT INTO account (username, password, role) VALUES (wanted_username, wanted_password, 'ADMIN');
```
