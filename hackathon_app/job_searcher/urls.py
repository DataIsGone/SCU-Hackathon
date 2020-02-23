from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='job_searcher_home'),
    path('about/', views.about, name='job_searcher_about'),
]
