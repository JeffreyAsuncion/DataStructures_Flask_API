from sqlite3 import Connection as SQLite3Connection
from datetime import datetime
from sqlalchemy import event
from sqlalchemy.engine import Engine
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# app variable that points to a Flask Instance
app = Flask(__name__)

# to have local file as our database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlitedb.file"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = 0 

# configure sqlite3 to enforce foreign key contraints
@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()

# instance of DB # connects our ORM with our Flask application
db = SQLAlchemy(app)
now = datetime.now()


# ORM Object Relational Model : treats database as object
# table classes need to inherit db.Model
# model
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(50))
    posts = db.relationship("BlogPost")

class BlogPost(db.Model):
    __tablename__ = "blog_post"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    body = db.Column(db.String(200))
    date = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


# routes
@app.route("/user", methods=["POST"])
def create_user():
    pass

@app.route("/user/descending_id", methods=["GET"])
def get_all_users_descending():
    pass

@app.route("/user/ascending_id", methods=["GET"])
def get_all_users_ascending():
    pass

@app.route("/user/<user_id>", methods=["GET"])      # we get to pass a user_id in the url and pass it to the get_one_user
def get_one_user(user_id):
    pass


@app.route("/user/<user_id>", methods=["DELETE"])      # we get to pass a user_id in the url and pass it to the delete_user
def delete_user(user_id):
    pass


@app.route("/blog_post/<user_id>", methods=["POST"])
def create_blog_post(user_id):
    pass


@app.route("/user/<user_id>", methods=["GET"])
def get_all_blog_post(user_id):
    pass

@app.route("/blog_post/<blog_post_id>", methods=["GET"])
def get_one_blog_post(blog_post_id):
    pass

@app.route("/blog_post/<blog_post_id>", methods=["DELETE"])
def delete_blog_post(blog_post_id):
    pass

if __name__ == "__main__":
    app.run(debug=True)





