from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class User(db.model):
    """A user class"""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(30), nullable=False)
    resident_or_collector = db.Column(db.Boolean, nullable=False)


    def __repr__(self):
        """Shows this information when user object is printed"""

        return '<User id={} email={}'.format(self.user_id, self.user_email)



