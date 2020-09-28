from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import spotipy
import json


# Create your views here.
def search(request):
    extra = {}
    if request.user.is_authenticated:
        spotify_user = request.user.social_auth.get(provider='spotify')
        sp = spotipy.Spotify(auth=spotify_user.extra_data["access_token"])
        current_user = json.dumps(sp.current_user())
        current_song = json.dumps(sp.current_user_playing_track())
        extra = {}
        extra["current_user"] = current_user
        extra["current_song"] = current_song
        extra["access_token"] = spotify_user.extra_data["access_token"]
    return render(request, 'login/login.html', {'extra': extra})
