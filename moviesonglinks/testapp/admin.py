from django.contrib import admin
from testapp.models import Movie
class MovieAdmin(admin.ModelAdmin):
    list_display=["name","link"]
admin.site.register(Movie,MovieAdmin)
# Register your models here.
