from django.shortcuts import render, HttpResponse, get_object_or_404
import datetime
from . import models
# Create your views here.


def about_view(request):
    return render(request, 'about.html')


def date_view(request):
    date_time = datetime.datetime.now()
    html = "<b>DATE:</b> %s" % date_time
    return HttpResponse(html)

def films_view(request, id):
    film = get_object_or_404(models.Film, id=id)
    return render(request, 'film.html')

def film_show(request):
    shows = models.Film.objects.all()
    return render(request, "films_show.html", {"shows":shows})

def films(request , id):
    # film = models.Film.objects.all()
    film = get_object_or_404(models.Film, id=id)
    return render(request, "films.html", {"film":film})


def rewiev(request , id):
    rewiev = get_object_or_404(models.Rewiev.objects.filter(id_pole=id))
    return render(request, "rewievs_film.html",{"rewiev":rewiev})


