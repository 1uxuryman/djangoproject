from django.shortcuts import render , HttpResponse
import datetime

# Create your views here.


def about_view(request):
    return render(request, 'about.html')


def date_view(request):
    date_time = datetime.datetime.now()
    html = "<b>DATE:</b> %s" % date_time
    return HttpResponse(html)
