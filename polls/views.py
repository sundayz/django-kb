from django.shortcuts import render, get_object_or_404

# For the oopsies
from django.http import Http404

# For detail, results & votes templates
from django.http import HttpResponse, HttpResponseRedirect

# For the Question and Choice classes
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
