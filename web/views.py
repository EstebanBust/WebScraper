from django.shortcuts import render
from scraper.models import Scraped, UrlsScraped
# Create your views here.
def home(request):
    mangas = Scraped.objects.all()
    return render(request,'home.html',{'mangas': mangas})

def detalle(request, id):
    manga = Scraped.objects.get(id=id)
    return render(request, 'detail.html', {'manga':manga})