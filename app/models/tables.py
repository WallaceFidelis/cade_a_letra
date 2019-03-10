from app import db
from datetime import datetime


class Authorization(db.Model):

    __tablename__ = "authorization"

    id = db.Column(db.Integer, primary_key=True)
    access_token = db.Column(db.String, nullable=False)
    token_type = db.Column(db.String, nullable=False)
    expires_in = db.Column(db.Integer, nullable=False)
    refresh_token = db.Column(db.String, nullable=False)
    scope = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, access_token, token_type, expires_in, refresh_token, scope):
        self.access_token = access_token
        self.token_type = token_type
        self.expires_in = expires_in
        self.refresh_token = refresh_token
        self.scope = scope
        self.created_at = datetime.now()

    def __repr__(self):
        return f'<Authorization {self.id}>'

    def create_authorization(self):
        db.session.add(self)
        db.session.commit()
        return self.id


class User(db.Model):
    __tablename__ = "user"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    type = db.Column(db.String)
    authorization_id = db.Column(db.Integer, nullable=False)

    def __init__(self, email, name, authorization_id, type="-"):
        self.name = name
        self.email = email
        self.type = type
        self.authorization_id = authorization_id


    def __repr__(self):
        return f'<User {self.name}>'

    
    def update_user(self):
        user = User.query.filter_by(email=self.email).first()
        if user:
            user.name = self.name
            user.type = self.type
            user.authorization_id = self.authorization_id
        else: 
            user = self
        db.session.add(user)
        db.session.commit()
