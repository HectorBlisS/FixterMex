from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Movie

class Home(View):
	def get(self,request):
		template_name="main/list.html"
		context={
		'movies':Movie.objects.all()
		}
		return render(request,template_name,context)

class DetailMovie(View):
	def get(self,request,id):
		template_name = 'main/detail_movie.html'
		movie = get_object_or_404(Movie,id=id)
		horarios = movie.shows.all()
		context = {
		'movie':movie,
		'horarios':horarios
		}
		return render(request,template_name,context)






