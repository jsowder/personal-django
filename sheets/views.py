from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .funs import initialize_sheets
from django.conf import settings
import os
import pickle
import datetime

# Create your views here.


def activity_view(request, *args, **kwargs):
    SHEETS_RANGE = 'Sheet1!A2:E'
    sheets = initialize_sheets()

    result = sheets.values().get(spreadsheetId=settings.ACTIVITY_SHEET_SECRET_ID,
                                 range=SHEETS_RANGE).execute()
    values = result.get('values', [])

    if not values:
        activity = {"0": {"title": "No activities found."}}
    else:
        activity = dict()
        i = 0
        for row in values:
            activity[i] = {
                "source": row[0],
                "value": row[1],
                "timestamp": datetime.datetime.strptime(row[2], '%m/%d/%Y %H:%M:%S'),
                "url": row[3],
            }
            i += 1

    context = {
        "activities": activity
    }

    return render(request, "sheets/activity.html", context)
