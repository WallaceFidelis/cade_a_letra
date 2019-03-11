import requests

api_key = "api_key"
url_search = "https://api.vagalume.com.br/search.php"



def get_music_vagalume(artist, music):
    url = f"{url_search}?art={artist}&mus={music}&apikey={api_key}" 
    r = requests.get(url)
    if "502 Bad Gateway" in r.text:
        return None, None, "Letra não encontrada =("

    result = r.json()
    if "notfound" in result["type"]:
        return None, None, "Letra não encontrada =("
    else : 
        song_lyrics = result["mus"][0]["text"]
        artist = result["art"]["name"]
        music = result["mus"][0]["name"]
        return music, artist, song_lyrics

def get_translation_song_lyrics(artist, music):
    result = lyrics.find(artist, music)
    translation = result.get_translation_to('pt-br')

    if not translation:
        return music, 'Translation not found'
    else:
        return translation.name, translation.lyric
