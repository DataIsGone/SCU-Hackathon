from django.shortcuts import render
from django.http import HttpResponse

results = [
    {'listing_id': 'p123',
     'title': 'python dev',
     'url': 'https://www.indeed.com/somelisting',
     'company': 'Local big name company',
     'location': 'Right down the road',
     'summary': 'A fun python job!'
    },
    {'listing_id': 'p456',
     'title': 'Data Scientist',
     'url': 'https://www.indeed.com/this_other_listing',
     'company': 'Far away startup',
     'location': 'Across the country',
     'summary': 'A fun new job where you can do ML!'
    },
]


def home(request):
    context = {'results': results}
    return render(request, 'job_searcher/home.html', context)


def about(request):
    return HttpResponse(render(request, 'job_searcher/about.html'))
