# DataStructures_Flask_API
This API uses different Data Structure


python -m venv flask_venv

To activate virtual env
. flask_venv/bin/activate

To deactivate the venv
deactivate

To check if the venv is activated
env | grep VIRTUAL_ENV

pip install Flask

check if venv is activated
env | grep VIRTUAL_ENV

then install pkgs
sudo apt-get install sqlite3

python server.py (and check for error and install apropiate pkgs)

pip install SQLAlchemy
pip install flask-sqlalchemy



we need a visual tool to see our sqlite
http://sqlitebrower.org/dl/
sudo apt-get update
sudo apt-get install sqlitebrowswer

Next we need to generate our database in the cli by running python and create our db tables based on our models
>>>from server import db
>>>db.create_all()  # will create our database  defined in our tables (db models)
>>>exit()
ls (to see the sqlitedb.file)

Open sqlitebrowser
go to folder and search sqlitedb.file (its there just might not populate to window)

examine the tables we created




timestamp 15:43
