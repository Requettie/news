from django.shortcuts import render
from django.views.generic import ListView
from .models import Article 


class ArticleListView(ListView): 
    model = Article
    template_name = "article_list.html"

class ArticleDetailView(DetailView):


class ArticleCreateView(CreateView):



class ArticleUpdateView(UpdateView):



class ArticleDeleteView(DeleteView):
    model = Article
    template
    

# Create your views here.
