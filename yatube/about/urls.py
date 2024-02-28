from django.urls import path

from .views import AuthorView, TechView

app_name = 'about'

urlpatterns = [
    path('author/', AuthorView.as_view(), name='author'),
    path('tech/', TechView.as_view(), name='tech'),
]
