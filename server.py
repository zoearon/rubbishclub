from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

#from model import connect_to_db, db, User, Favorite, Dog, Shelter, Breed

import os

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


@app.route('/login')
def login():
    """ login for residents and collectors """

    return render_template("login.html")


@app.route('/profile')
def view_profile():
    """ Resident profile page """

    return render_template("res_profile.html")


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