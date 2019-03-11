import requests
import json 
from app import app
from app.controllers.spotify import *
from app.controllers.vagalume import *
from app.models.tables import Music
from flask import redirect, request, session, render_template
from flask_session.__init__ import Session

@app.route("/music")
def get_music():
    if "authorization" not in session:
        return redirect("/")

    searched_artist, searched_music = get_currently_playing()
    if (searched_artist == None and searched_music == None):
        searched_artist, searched_music = get_most_recently_playing()

    music, artist, song_lyrics = search_music(searched_artist, searched_music)
    song_lyrics = song_lyrics.split("\n")
    return render_template('music.html', 
                        music=music, 
                        artist=artist, 
                        searched_artist=searched_artist, 
                        searched_music=searched_music, 
                        song_lyrics=song_lyrics)


def search_music(searched_artist, searched_music):

    music, artist, song_lyrics = Music.get_Music(searched_artist, searched_music)
    if(music == None):
        music, artist, song_lyrics = get_music_vagalume(searched_artist, searched_music)
        if music :
            Music(artist, music,song_lyrics, searched_artist, searched_music).insert_music()    

    return music, artist, song_lyrics
