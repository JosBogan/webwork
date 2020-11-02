from django.urls import path
from .views import RegisterView, ListView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('users/', ListView.as_view()),
    path('login/', LoginView.as_view()),
]