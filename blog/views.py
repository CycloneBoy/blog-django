from django.shortcuts import render, get_object_or_404
from .models import BlogArticles


def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request, "blog/titles.html", {"blogs": blogs})


def blog_articles(request, article_id):
    #article = BlogArticles.objects.get(pk=article_id)
    article = get_object_or_404(BlogArticles, pk=article_id)
    publish = article.publish
    return render(request, "blog/content.html", {"article": article, "publish": publish})
