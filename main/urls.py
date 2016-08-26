from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$',views.Home.as_view(),name='home'),
	url(r'^movie/(?P<id>\d+)/$',views.DetailMovie.as_view(),name="detail_movie"),
]