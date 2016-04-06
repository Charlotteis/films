from django.shortcuts import render, redirect
from films.forms import FilmForm
from films.models import Film


def index(request):
    films = Film.objects.all().order_by('rating').reverse()
    return render(request, 'index.html', {
        'films': films,
    })


def film_detail(request, slug):
    film = Film.objects.get(slug=slug)
    return render(request, 'films/film_detail.html', {
        'film': film,
    })


def edit_film(request, slug):
    film = Film.objects.get(slug=slug)
    form_class = FilmForm

    if request.method == 'POST':
        form = form_class(data=request.POST, instance=film)

        if form.is_valid():
            form.save()
            return redirect('film_detail', slug=film.slug)
    else:
        form = form_class(instance=film)

    return render(request, 'films/edit_film.html', {
        'film': film,
        'form': form,
    })



def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
