## Use guide
To start using the application, register yourself an account via the link on the login page.

As a normal user you can browse existing movies and request new ones via the link in the navigation bar. Requested movies will be seen by administrators and can then be accepted by them. Normal users can also add movies as favorites which saves them to a personal 'library'.

Administrators can also edit and delete existing movies on their individual pages.

To create yourself an admin account, you have you connect to the database and create the account from there, using "ADMIN" as role. For example:
```
sqlite3 ./application/movies.db
INSERT INTO account (username, password, role) VALUES (wanted_username, wanted_password, 'ADMIN');
```
