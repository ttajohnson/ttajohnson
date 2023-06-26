from django.shortcuts import render
from .forms import MovieSearchForm

featured_movie_list = [
    {
        "img_src": "https://images.thedirect.com/media/article_full/amazing-spider-man-3-andrew-garfield-movie-mcu.jpg",
        "img_alt": "...",
        "active": True
    },
    {
        "img_src": "https://static1.colliderimages.com/wordpress/wp-content/uploads/2022/11/avatar-the-way-of-water-poster.jpg",
        "img_alt": "...",
        "active": False
    }
]

def index(request):
    context = {
        "featured_movies": featured_movie_list,
        "form": MovieSearchForm()
    }
    return render(request, 'index.html', context)