from django.urls import path
from .views import HomeView, ExpenseView, UserView, StoreView, SplashView
from . import views

app_name = 'track'
urlpatterns = [
    # ex: /polls/
    path('', SplashView.as_view()),
    path('in/', HomeView.as_view(), name='index'),
    path('expense/', ExpenseView.as_view(), name='expense'),
    path('user/<int:id>', UserView.as_view(), name='user'),
    path('instore/', StoreView.as_view(), name='store'),

    # ex: /polls/5/
]
