from app import app
from app import db
from app.models.tables import Authorization
import requests
from flask import redirect, request, session
from flask_session.__init__ import Session
from datetime import timedelta

url_authorize = "https://accounts.spotify.com/authorize"
url_redirect_login = "http://localhost:3000/spotify-login"
url_tokem = "https://accounts.spotify.com/api/token"

client_id = "client_id"
client_secret = "client_secret"

param_client_id = "client_id=" + client_id
response_type = "code"
scopes = "user-read-currently-playing user-read-recently-played user-read-email"


@app.route("/login")
def login():
    if "authorization" in session:
        return redirect("/music")

    url = f'{url_authorize}?&client_id={client_id}&response_type={response_type}&redirect_uri={url_redirect_login}&scope={scopes}'
    return redirect(url)


@app.route("/spotify-login")
def spotify_login():
    code = request.args.get("code")

    r = requests.post(url_tokem, 
        data = {
            "grant_type":"authorization_code",
            "code": code,
            "client_id":client_id,
            "client_secret":client_secret,
            "redirect_uri":url_redirect_login
        })
    
    data = r.json()
    if 'error' in data:
        return redirect("/")  #to-do página de erro

    access_token = data['access_token'] 
    token_type = data['token_type'] 
    expires_in = data['expires_in']
    refresh_token = data['refresh_token']
    scope = data['scope']
    authorization = Authorization(access_token, token_type, expires_in, refresh_token, scope)
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=59)
    session["authorization"] = authorization.create_authorization()

    return redirect("/user/update")
