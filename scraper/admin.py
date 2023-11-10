from django.contrib import admin
from .models import Scraped, UrlsScraped

admin.site.register(Scraped)
admin.site.register(UrlsScraped)