from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Job Searcher</h1>')


def about(request):
    return HttpResponse('<h1>About</h1>')
