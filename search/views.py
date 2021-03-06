from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth import logout;
import spotipy
import json


# Create your views here.
def search(request):
    extra = {}
    if request.user.is_authenticated:
        spotify_user = request.user.social_auth.get(provider='spotify')
        current_user = None
        try:
            sp = spotipy.Spotify(auth=spotify_user.extra_data["access_token"])
            current_user = sp.current_user()
        except:
            return redirect("search:reval")

        last_played = sp.current_user_recently_played(limit=1)["items"][0]["track"]["uri"]
        extra["last_played"] = last_played
        extra["current_user"] = current_user
        extra["access_token"] = spotify_user.extra_data["access_token"]

    return render(request, 'login/login.html', {'extra': extra})


def reval(request):
    logout(request)
    return redirect("search:search")
