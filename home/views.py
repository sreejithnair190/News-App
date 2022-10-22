from django.shortcuts import render

from home.models import Articles
from .utils import get_news_from_api

# Create your views here.

def index(request):
    # url = 'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=6aa586a4814140aaab6c927d301c899a'
    # get_news_from_api(url)
    context={
        'articles' : Articles.objects.all()
    }
    return render(request, "home/index.html", context=context)