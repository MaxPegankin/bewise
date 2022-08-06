from flask import Flask

from rest_app.database import db_session, init_db


app = Flask(__name__)

import rest_app.views
from dotenv import load_dotenv
load_dotenv('../.env')


init_db()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


