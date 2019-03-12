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


class Music(db.Model):
    __tablename__ = "Music"

    id = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String, nullable=False)
    music = db.Column(db.String, nullable=False)
    song_lyrics = db.Column(db.Text, nullable=False)
    searched_artist = db.Column(db.String, nullable=False)
    searched_music = db.Column(db.String, nullable=False)
    translate = db.Column(db.String)

    def __init__(self, artist, music, song_lyrics, searched_artist, searched_music, translate=None):
        self.artist = artist
        self.music = music
        self.song_lyrics = song_lyrics
        self.searched_artist = searched_artist
        self.searched_music = searched_music
        self.translate = translate

    def __repr__(self):
        return f'<Music {self.music}>'

    def insert_music(self):
        db.session.add(self)
        db.session.commit()

    def get_Music(artist, music):
        result = Music.query.filter_by(searched_artist=artist, searched_music=music).first()
        if result:
            print(result.translate)
            return result.music, result.artist, result.song_lyrics, result.translate
        return None, None, None, None
        