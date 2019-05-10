from django.shortcuts import render
from ArticleApp.models import Article
from django.views import generic


# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

class ArticleListView(generic.ListView):
    model = Article


class ArticleDetailView(generic.DetailView):
    model = Article

