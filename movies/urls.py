from django.urls import path, include
from .views import MoviesView, MovieDetailView, AddReview, ActorView, FilterMoviesView, JsonFilterMoviesView

urlpatterns = [
    path('', MoviesView.as_view(), name='list'),
    path('filter/', FilterMoviesView.as_view(), name='filter'),
    path('json-filter/', JsonFilterMoviesView.as_view(), name='json_filter'),
    path('<slug:slug>/', MovieDetailView.as_view(), name='movie_detail'),
    path('review/<int:pk>/', AddReview.as_view(), name='add_review'),
    path('actor/<str:slug>/', ActorView.as_view(), name='actor_detail'),
]
