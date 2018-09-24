from announcement.models import News

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model

# permission
from django.contrib.auth.decorators import login_required

User = get_user_model()


#=== Section dynamic content ===#
def news(request):
    news_list = News.objects.all().filter(status='published').values()
    context = []
    for news in news_list:
        context.append(news)
    context = {
        'news_list': context
    }
    return render(request, "news.html", context)

#=== Section static content ===#
def about_us(request):
    return render(request, "about_us.html")

def abstract(request):
    return render(request, "abstract.html")

def accommodation(request):
    return render(request, "accommodation.html")

def committee(request):
    return render(request, "committee.html")

def contact(request):
    return render(request, "contact.html")

def convention_venue(request):
    return render(request, "convention_venue.html")

def excursion(request):
    return render(request, "excursion.html")

def general_information(request):
    return render(request, "general_information.html")

def index(request):
    return render(request, "index.html")

def programs(request):
    return render(request, "programs.html")

def registration(request):
    return render(request, "registration.html")

def schedule(request):
    return render(request, "schedule.html")

def speakers(request):
    return render(request, "speakers.html")

def visa(request):
    return render(request, "visa.html")
