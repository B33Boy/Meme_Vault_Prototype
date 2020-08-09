from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


@login.user_loader
def load_user(id):
    """Returns user object from id.

    Parameters
    ----------
    id : int
        the id of the targeted user

    Returns
    -------
    object
        User object

    """
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    """Defines the User schema.

    Attributes
    ----------
    id : db.Column
        int id
    username : db.Column
        string username
    password_hash : db.Column
        string password
    posts : db.relationship
        object that maps posts to a single user via adjacency list

    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    Posts = db.relationship('Post', backref='author', lazy='dynamic')

    def set_password(self, password):
        """hashes unhashed password.

        Parameters
        ----------
        password : string
            unhashed password

        Returns
        -------
        string
            hashed password

        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """checks if the hashed password matches the password in the parameter

        Parameters
        ----------
        password : string
            entered password to be matched with the unhashed password

        Returns
        -------
        boolean
            returns if password matched input

        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        """Allows object of type User to be printed.

        Returns
        -------
        string
            username of the user

        """
        return '<User {}>'.format(self.username)


class Post(db.Model):
    """Defines the Post schema

    Attributes
    ----------
    id : db.Column
        int id
    body : db.Column
        string body
    user_id : db.Column
        The user id that the post is mapped to

    """
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        """Allows object of type Post to be printed.

        Returns
        -------
        string
            the body field of the post

        """
        return '<Post {}>'.format(self.body)
