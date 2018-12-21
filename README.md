# Kondor

To get started download python 3.x create a virtual environment and clone this repo.

Then run:

`pip install -r requirements.txt`

Then install postgres and create a database named kondor.

You should make a new user in postgres for the database called kondorAdmin.

Make the following your password:
i*5wQ9KCWNe638758U$Lfd7FI3MP2Q

Alternatively, you could use whatever username and password you like just change this line the config.py file:

SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://kondorAdmin:i*5wQ9KCWNe638758U$Lfd7FI3MP2Q@127.0.0.1:5432/kondor"

Delete the migrations folder then run:

`flask db init`

This should create a new folder called migrations.


Then run:
```
flask db migrate
flask db upgrade
```

The tables should now be created in the kondor database.

Finally just run:

`python run.py`
