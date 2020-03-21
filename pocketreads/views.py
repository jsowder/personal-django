from django.shortcuts import render
from django.utils.timezone import make_aware
import requests
import json
import pprint
from datetime import datetime
from django.conf import settings

# Create your views here.


def pocket_index(request, *args, **kwargs):
    GET_URL = "https://getpocket.com/v3/get"

    PARAMETERS = {
        "consumer_key": settings.POCKET_SECRET_CONSUMER_KEY,
        "access_token": settings.POCKET_SECRET_ACCESS_TOKEN,
        "sort": "newest",
        "detailType": "complete",
        "count": "3",
        # "state": "unread",
        # "favorite": "",
    }

    PARAMETERS.update(state="unread")
    unread = requests.get(
        url=GET_URL,
        params=PARAMETERS
    ).json()['list']

    PARAMETERS.update(state="archive")
    archive = requests.get(
        url=GET_URL,
        params=PARAMETERS
    ).json()['list']

    PARAMETERS.update(state="all", favorite="1")
    favorites = requests.get(
        url=GET_URL,
        params=PARAMETERS
    ).json()['list']

    context = {"pocket_unread": unread,
               "pocket_archive": archive,
               "pocket_favorites": favorites, }
    return render(request, "pocketreads/pocket-home.html", context)


def get_more(request, pocket_type):
    GET_URL = "https://getpocket.com/v3/get"
    PARAMETERS = {
        "consumer_key": settings.POCKET_SECRET_CONSUMER_KEY,
        "access_token": settings.POCKET_SECRET_ACCESS_TOKEN,
        "state": "unread",
        "sort": "newest",
        "detailType": "complete",
        "count": "30",
        # "favorite": "0",
    }
    if (pocket_type == "read"):
        PARAMETERS['state'] = "archive"
    elif (pocket_type == "unread"):
        PARAMETERS['state'] = "unread"
    elif (pocket_type == "favorites"):
        PARAMETERS['state'] = "read"
        PARAMETERS['favorite'] = "1"
    else:
        pass

    POCKET = requests.get(
        url=GET_URL,
        params=PARAMETERS
    ).json()['list']

    context = {
        "pocket": POCKET,
        "pocket_type": pocket_type
    }
    return render(request, "pocketreads/pocket-more.html", context)
