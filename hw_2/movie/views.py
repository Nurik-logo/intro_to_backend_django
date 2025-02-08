from django.shortcuts import render, get_object_or_404
from .models import Movie
from django.http import JsonResponse

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie/movie_list.html', {'movies': movies})

def movie_detail(request, id):
    movie = get_object_or_404(Movie, id=id)
    return render(request, 'movie/movie_detail.html', {'movie': movie})

def api_movie_list(request):
    movies = Movie.objects.all().values()
    return JsonResponse(list(movies), safe=False)

def api_movie_detail(request, id):
    movie = get_object_or_404(Movie, id=id)
    return JsonResponse({'title': movie.title, 'description': movie.description, 'producer': movie.producer, 'duration': movie.duration})
