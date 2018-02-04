from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, User, Resident, GarbageCollector

import os
from model import db

#from helper_funcs import find_labels, find_datasets

app = Flask(__name__)

app.secret_key = "ABC"

app.jinja_env.undefined = StrictUndefined

tom_tom_key=os.environ["TOM_TOM_KEY"]


@app.route('/')
def index():
    """Homepage."""


    return render_template("homepage.html")

@app.route('/register')
def register():
    """ register new residents and collectors """

    return render_template("register.html")


@app.route('/register-success', methods=['POST'])
def register_process():
    """Process registration."""
    # Get form variables

    fname = request.form["fname"]
    lname = request.form["lname"]
    address = request.form["address"]
    can_size = request.form["can_size"]
    needs_pickup = request.form["needs_pickup"]

    #UPDATE DB

    return redirect("/")
 

@app.route('/login', methods=['GET'])
def login():
    """ login for residents and collectors """

    return render_template("login.html")


@app.route('/login', methods=['POST'])
def check_user():
    """ log the user in """

    # get the email from the post form
    email = request.form.get("email")
    password = request.form.get("password")

    active_user = db.session.query(User).filter(User.email == email,
                                                User.password == password).first()

    if active_user:
        flash("Login Successful")
        session['user'] = active_user.user_id
        if active_user.resident_or_collector == "resident":
            return redirect('/profile')
        elif ctive_user.resident_or_collector == "collector":
            return redirect('/collector')
    flash("Login Failed")
    return redirect('/login')

@app.route('/profile')
def view_profile():
    """ Resident profile page """

    return render_template("res_profile.html")

@app.route('/collector')
def directions():
    """ Collector page """

    return render_template("collector.html")

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True
    app.jinja_env.auto_reload = True
    app.config["TEMPLATES_AUTO_RELOAD"] = True

  #  connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="127.0.0.1")