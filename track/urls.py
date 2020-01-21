from django.urls import path
from .views import HomeView
from . import views

app_name = 'track'
urlpatterns = [
    # ex: /polls/
    path('', HomeView.as_view(), name='index'),
    # ex: /polls/5/
]
