from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import SearchForm
from django.shortcuts import redirect
from job_searcher.modules.IndeedScraper import IndeedScraper
from .models import Search


indeed = IndeedScraper()
indeed.search("Python Developer", "Santa Clara", "CA")


def home(request):
    context = {'results': indeed.get_results()}
    return render(request, 'job_searcher/home.html', context)

def result(request, pk):
    search = get_object_or_404(Search, pk=pk)
    results = indeed.search(search.description, search.city, search.state)
    return render(request, 'job_searcher/result.html', {'results': indeed.get_results()})
    # return render(request, 'job_searcher/result.html', {'results': results})


def search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.save()
            return redirect('job_searcher_result', pk=search.pk)
    else:
        form = SearchForm()
    return HttpResponse(render(request, 'job_searcher/search.html', {'title': 'Search', 'form': form}))


def about(request):
    return HttpResponse(render(request, 'job_searcher/about.html', {'title': 'About'}))
