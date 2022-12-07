from articles.models import Article
from django.shortcuts import render

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})

# def archive(request):
#     return render(request, 'templates/archive.html')
# Create your views here.
