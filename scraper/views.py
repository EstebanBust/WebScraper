from django.http import HttpResponse
import requests, re
from bs4 import BeautifulSoup
from .models import Scraped, UrlsScraped
from django.shortcuts import render

def scrape_url(request):
    if request.method == 'POST':
        print(request.POST.get('url'))
        response = requests.get(request.POST.get('url'))

        if response.status_code == 200:
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            title = request.POST.get('titulo')
            
            author = request.POST.get('autor')
            
            if title and author:
                
                new_scraping = Scraped(title=title, autor=author)  
                new_scraping.save()

                scripts = soup.find_all('script')
                url_pattern = r'https:[^\s"]+'
                urls = []
                for script in scripts:
                    script_content = script.string
                    if script_content:

                        urls.extend(re.findall(url_pattern, script_content))

        
                for url in urls:
                    url_object, created = UrlsScraped.objects.get_or_create(url=url)
                new_scraping.urls.set(UrlsScraped.objects.filter(url__in=urls))

                return render(request,'scraper.html',{'error':"La información ha sido guardada en la base de datos."})
            return render(request,'scraper.html',{'error':'ingresa el titulo y el autor'})
        return render(request,'scraper.html',{'error':"Error al acceder a la URL: " + str(response.status_code)})
    else:
        return render(request,'scraper.html')