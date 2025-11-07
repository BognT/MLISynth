from django.contrib import admin
from .models import Country, Treaty

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']
    search_fields = ['name', 'code']

@admin.register(Treaty)
class TreatyAdmin(admin.ModelAdmin):
    list_display = ['country1', 'country2', 'pdf_url']
    list_filter = ['country1', 'country2']