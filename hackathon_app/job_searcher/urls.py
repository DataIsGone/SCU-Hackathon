from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='job_searcher_home'),
    path('search/', views.search, name='job_searcher_search'),
    path('about/', views.about, name='job_searcher_about'),
]
