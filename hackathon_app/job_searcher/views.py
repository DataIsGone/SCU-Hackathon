from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse(render(request, 'job_searcher/home.html'))


def about(request):
    return HttpResponse('<h1>About</h1>')
