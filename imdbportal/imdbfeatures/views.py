from .forms import search_approx_name

from django.shortcuts import render

from .suggest_movies import get_movie_names_for
from .get_detail_movie_info import by_imdb_id as movie_info_by_imdb_id


# Create your views here.

def root_view(request):
	

	context = {

	}

	return render(request, 'index_page.html', context)

def search_by_name_view(request):
	
	this_form = search_approx_name()
	if 'name' in request.GET:
		print(request.GET)
		movies = get_movie_names_for(request.GET['name'])
		# print(movies, movies[movie_list[0]], sep='\n')

		context = {
		'form' : this_form,
		'movies' : movies,
		'has_suggestions' : 'True',

		}

		return render(request, 'by_name.html', context);


	context = {
		'form' : this_form,
		'has_suggestions' : '',
	}

	return render(request, 'by_name.html', context)

def search_by_imdb_id(request, imdb_id):
	data = movie_info_by_imdb_id(imdb_id)

	context = {
	"data" : data,
	}
	return render(request, 'by_imdb_id.html', context)

