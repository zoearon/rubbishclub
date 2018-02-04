from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class User(db.Model):
    """ A user class """

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(30), nullable=False)
    resident_or_collector = db.Column(db.String(10), nullable=False)


    def __repr__(self):
        """ Shows this information when user object is printed """

        return '<User id={} email={}'.format(self.user_id, self.user_email)



class Resident(db.Model):
    """ A resident user """

    __tablename__ = 'residents'

    resident_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #Foreign key is the user ID
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    fname = db.Column(db.String(30), nullable=False)
    lname = db.Column(db.String(30), nullable=False)
    address = db.Column(db.String(150), nullable=False)
    can_size = db.Column(db.String(30), nullable=False)
    #'needs_pickup' is for a one day pickup.
    # Plans past MVP are to change this to a schedule w/ multiple day options
    needs_pickup = db.Column(db.Boolean, nullable=False)


    def __repr__(self):
        """ Shows this information when resident object is printed """

        return '<Resident id={} fname={} needs_pickup={}'.format(self.resident_id,
                                                             self.fname,
                                                             self.needs_pickup)


class GarbageCollector(db.Model):
    """ A garbage collector """

    __tablename__ = 'garbage_collectors'

    collector_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    fname = db.Column(db.String(30), nullable=False)
    lname = db.Column(db.String(30), nullable=False)


    def __repr__(self):
        """ Shows this information when garbage collector object is printed """

        return '<GarbageCollector id={} fname={}'.format(self.collector_id,
                                                         self.fname)





















