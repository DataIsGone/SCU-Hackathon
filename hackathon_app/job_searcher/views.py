from django.shortcuts import render
from django.http import HttpResponse
from job_searcher.modules.IndeedScraper import IndeedScraper

indeed = IndeedScraper()
indeed.search("Python Developer", "Santa Clara", "CA")


def home(request):
    context = {'results': indeed.get_results()}
    return render(request, 'job_searcher/home.html', context)

def search(request):
    return HttpResponse(render(request, 'job_searcher/search.html', {'title': 'Search'}))

def about(request):
    return HttpResponse(render(request, 'job_searcher/about.html', {'title': 'About'}))
