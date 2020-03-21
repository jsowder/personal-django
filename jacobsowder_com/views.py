from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
import random
# from blog import models as blog_models


def index_view(request, *args, **kwargs):
    context = {
        "accentcolor":  "white",
        "accentqualifier": "",
        "bodystyle": "",
    }
    return render(request, "jacobsowder_com/home.html", context)


def error_404(request, *args, **kwargs):
    context = {}
    return render(request, 'jacobsowder_com/404.html', context)
