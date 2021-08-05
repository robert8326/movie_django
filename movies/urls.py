from django.urls import path, include
from .views import MoviesView, MovieDetailView

urlpatterns = [
    path('', MoviesView.as_view(), name='list'),
    path('<slug:slug>/', MovieDetailView.as_view(), name='movie_detail')
]
