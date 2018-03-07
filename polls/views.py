from django.shortcuts import render, get_object_or_404

# For the oopsies
from django.http import Http404

# For detail, results & votes templates
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import redirect

from polls.forms import SearchForm
from .models import Article, Category, Comment, UserProfile

from django.urls import reverse


def index(request):
    hot_articles = Article.objects.order_by('-date_created')[:5]
    context = {'hot_articles': hot_articles}
    return render(request, 'polls/index.html', context)

def detail(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
        userprofile = UserProfile.objects.get(pk=article.author.id)
        comment = Comment.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("Article does not exist")
    return render(request, 'polls/detail.html', {'article': article, 'userprofile':userprofile, 'comment': comment})

def search(request):
    # GET request handling
    query = request.GET.get('search')
    if query is not None:
        form = SearchForm(request.GET)
        if form.is_valid():
            clean_query = form.cleaned_data['search']
            articles = Article.objects.filter(name__icontains=clean_query)
            comments = Comment.objects.filter(comment__icontains=clean_query)
            context = {'articles': articles, 'comments': comments, 'search': clean_query}
            return render(request, 'polls/search.html', context)
        else:
            # TODO: messages
            return HttpResponseRedirect('/')
    else:
        # TODO: messages
        return HttpResponseRedirect('/')
