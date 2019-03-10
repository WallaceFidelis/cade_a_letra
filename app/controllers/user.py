from app import app
from app import db
from app.models.tables import Authorization, User
import requests
from flask import redirect, request, session
from flask_session.__init__ import Session

url_user = "https://api.spotify.com/v1/me"

@app.route("/user/update")
def user_update():
    if "authorization" not in session:
        return redirect("/")

    user_information = get_user_information()

    name = user_information['display_name']
    email = user_information['email']
    type = user_information['type']
    authorization_id = session['authorization']

    user = User(email, name, authorization_id, type)
    user.update_user()

    return redirect("/music")


def get_user_information():
    authorization = Authorization.query.filter_by(id=session["authorization"]).first()
    if authorization:
        headers = {'Authorization': 'Bearer ' + authorization.access_token}
        r = requests.get(url_user, headers=headers)
        
        data = r.json()
        return data  
    return None

