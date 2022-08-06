from flask import Flask

from rest_app.database import db_session, init_db
from flask_bootstrap import Bootstrap
import os

app = Flask(__name__)
bootstrap = Bootstrap(app)

import rest_app.views
from dotenv import load_dotenv
load_dotenv('../.env')


init_db()

app.config['SECRET_KEY'] = os.environ.get("FLASK_FORMS_SECRET_KEY")

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


