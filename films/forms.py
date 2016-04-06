from django.forms import ModelForm

from films.models import Film


class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ('name', 'rating',)
