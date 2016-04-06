from django.contrib import admin

from films.models import Film


class FilmAdmin(admin.ModelAdmin):
    model = Film
    list_display = ('name', 'rating',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Film, FilmAdmin)
