import requests
from app import app
from app import db
from app.models.tables import Authorization
from flask import redirect, request, session
from flask_session.__init__ import Session


url_currently_playing = "https://api.spotify.com/v1/me/player/currently-playing"
url_recently_played = "https://api.spotify.com/v1/me/player/recently-played"

def get_currently_playing():
    if "authorization" not in session:
        return None, None

    authorization = Authorization.query.filter_by(id=session['authorization']).first()
    headers = {'Authorization': 'Bearer ' + authorization.access_token}
    r = requests.get(url_currently_playing, headers=headers)
    
    if r.text == "":
        return None, None
    elif 'error' in r.json() and r.json()['error']['status'] == 401:
        session.pop("authorization")
        return None, None

    data = r.json()
    if "currently_playing_type" in data and data["currently_playing_type"] == "ad":
        return None, None
        
    artist = data["item"]["artists"][0]["name"]
    music = data["item"]["name"]
    return artist, music

def get_most_recently_playing():
    if "authorization" not in session:
        return None, None

    authorization = Authorization.query.filter_by(id=session['authorization']).first()
    headers = {'Authorization': 'Bearer ' + authorization.access_token}
    r = requests.get(url_recently_played, headers=headers)
    
    if (r.text == ""):
        return None, None  
    elif 'error' in r.json() and r.json()['error']['status'] == 401:
        session.pop("authorization")
        return None, None

    data = r.json()
    artist = data["items"][0]["track"]["artists"][0]["name"]
    music = data["items"][0]["track"]["name"]
    return artist, music        