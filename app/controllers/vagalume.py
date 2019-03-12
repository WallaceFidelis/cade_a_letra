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
        return None, None, "Letra não encontrada =(", None
    else : 
        song_lyrics = result["mus"][0]["text"]
        artist = result["art"]["name"]
        music = result["mus"][0]["name"]
        translate = None
        if "translate" in result["mus"][0] and result["mus"][0]["translate"][0]["lang"] == 1:
            translate = result["mus"][0]["translate"][0]["text"]
        return music, artist, song_lyrics, translate

