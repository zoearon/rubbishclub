
from model import User, Resident, GarbageCollector
from model import connect_to_db, db
from server import app

def load_users():
    """ Loads sample users into the db """

    #Delete to prevent duplicates:
    User.query.delete()
    Resident.query.delete()
    GarbageCollector.query.delete()

    #these will be the residents:
    # (passwords not secure because they're just examples)

    user1 = User(email='bob@gmail.com',
                 password='password',
                 resident_or_collector='resident')

    user2 = User(email='sally@gmail.com',
                 password='mypassword',
                 resident_or_collector='resident')

    user3 = User(email='grandpa@gmail.com',
                 password='worldsbestgrandpa',
                 resident_or_collector='resident')

    user4 = User(email='grandma@gmail.com',
                 password='ilovegrandpa',
                 resident_or_collector='resident')

    user5 = User(email='user5@gmail.com',
                 password='pass',
                 resident_or_collector='resident')

    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.add(user4)
    db.session.add(user5)

    db.session.commit()


if __name__ == '__main__':

  #db.create_all() inside connect_to_db()
  connect_to_db(app)

  load_users()
