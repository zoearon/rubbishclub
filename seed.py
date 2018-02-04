
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


    res1 = Resident(user_id=user1.user_id,
                    fname='bob',
                    lname='bobbertson',
                    address='462 Powell St, San Francisco, CA 94102',
                    can_size='standard',
                    needs_pickup=False)

    res2 = Resident(user_id=user2.user_id,
                    fname='sally',
                    lname='sallerson',
                    address='450 Sutter St, San Francisco, CA 94102',
                    can_size='standard',
                    needs_pickup=False)

    res3 = Resident(user_id=user3.user_id,
                    fname='gramps',
                    lname='grandparent',
                    address='398 Market St, San Francisco, CA 94111',
                    can_size='standard',
                    needs_pickup=False)

    res4 = Resident(user_id=user4.user_id,
                    fname='gran',
                    lname='grandparent',
                    address='44 Montgomery St, San Francisco, CA 94104',
                    can_size='standard',
                    needs_pickup=False)

    res5 = Resident(user_id=user5.user_id,
                    fname='five',
                    lname='fiverson',
                    address='789 Mission St, San Francisco, CA 94103',
                    can_size='standard',
                    needs_pickup=False)

    db.session.add(res1)
    db.session.add(res2)
    db.session.add(res3)
    db.session.add(res4)
    db.session.add(res5)

    db.session.commit()


if __name__ == '__main__':

  #db.create_all() inside connect_to_db()
  connect_to_db(app)

  load_users()
