from django.contrib import admin
from .models import Genre,Movie


class Genre_Admin(admin.ModelAdmin):
    list_display = ('id' , 'name')


class Movie_Admin(admin.ModelAdmin):
    exclude = ('Date_created' ,)
    list_display = ('id' , 'title','number_in_stuck','daily_rate','genre')

# Register your models here.
admin.site.register(Genre, Genre_Admin)
admin.site.register(Movie , Movie_Admin)  