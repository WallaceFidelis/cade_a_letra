import requests
import json 
from app import app
from app import db
from app.controllers.spotify import *
from flask import redirect, request, session
from flask_session.__init__ import Session


@app.route("/music")
def get_music():
    if "authorization" not in session:
        return redirect("/")

    artist, music = get_currently_playing()
    if (artist == None and music == None):
        artist, music = get_most_recently_playing()

    data = {
        "artist": artist,
        "music": music
    }
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return  response