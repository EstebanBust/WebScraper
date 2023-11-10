from django.db import models

#Guarda las url scrapeadas
class UrlsScraped(models.Model):
    url = models.URLField(unique=True)

    def __str__(self):
        return self.url
    
class Scraped(models.Model):
    title = models.CharField(max_length=200)
    urls = models.ManyToManyField(UrlsScraped, related_name='scraped' )
    autor = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.title

