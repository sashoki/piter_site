from django.shortcuts import render, render_to_response, redirect
from p_site.models import Article, Comments, Category, Keywords, Author, Home
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import HttpResponse, Http404
from forms import CommentForm, KeywordsForm
from django.core.context_processors import csrf
from django.contrib import auth
from django.core.paginator import Paginator


def index(request):
    return render(request, 'index.html')


def articles(request, page_number=1):
    keywords_form = KeywordsForm
    args = {}
    all_articles = Article.objects.all()
    current_page = Paginator(all_articles, 2)
    args['articles'] = current_page.page(page_number)
    args['projects'] = Category.objects.all()
    args['keywords'] = Keywords.objects.all()
    args['username'] = auth.get_user(request).username
    args['authors'] = Author.objects.all()
    args['form_keywords'] = keywords_form
    return render(request, 'articles.html', args)

def article(request, article_id=1):
    comment_form = CommentForm
    keywords_form = KeywordsForm
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args['projects'] = Category.objects.all()
    args['category'] = Category.objects.filter(id=article_id)
    args['comments'] = Comments.objects.filter(comments_article_id=article_id)
    args['n_comments'] = args['comments'] .count()
    args['keywords'] = Keywords.objects.all()
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    args['authors'] = Author.objects.all()
    args['form_keywords'] = keywords_form
    return render(request, 'article1.html', args)

def addlike(request, article_id):
    try:
        if article_id in request.COOKIES:
            return_path = request.META.get('HTTP_REFERER', '/')
            return redirect(return_path)
        else:
            article = Article.objects.get(id=article_id)
            article.article_like += 1
            article.save()
            return_path = request.META.get('HTTP_REFERER', '/')
            response = redirect(return_path)
            response.set_cookie(article_id, "test")
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')

def addcomment(request, article_id):
    if request.POST and ("pause" not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_author = request.user
            comment.comments_article = Article.objects.get(id=article_id)
            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
    return redirect('/articles/get/%s/' % article_id)

def article_cat(request, category_id=1):
    keywords_form = KeywordsForm
    args = {}
    args['projects'] = Category.objects.all()
    args['category'] = Category.objects.get(id=category_id)
    args['articles'] = Article.objects.filter(category_id=category_id)
    args['username'] = auth.get_user(request).username
    args['keywords'] = Keywords.objects.all()
    args['form_keywords'] = keywords_form
    branch_categories = args['category'].get_descendants(include_self=True)
    args['category_articles'] = Article.objects.filter(category__in=branch_categories).distinct()
    args['authors'] = Author.objects.all()
    return render(request, 'article_cat.html', args)

def keywords(request):
    keywords_form = KeywordsForm
    return_path = request.META.get('HTTP_REFERER', '/')
    args= {}
    args['authors'] = Author.objects.all()
    args['keywords'] = Keywords.objects.all()
    args['projects'] = Category.objects.all()
    args['username'] = auth.get_user(request).username
    args['form_keywords'] = keywords_form
    args.update(csrf(request))
    if request.POST:
        key = request.POST.get('name', '')
        args['key_name'] = key
        args['articles'] = Article.objects.filter(keywords__name__exact=key)
        if args['articles']:
            return render(request, 'keywpage.html', args)
        else:
            return render(request, 'keywpage_no.html', args)
    else:
        return render(return_path)

def authors(request, id):
    keywords_form = KeywordsForm
    args= {}
    args['authors'] = Author.objects.all()
    args['author_s'] = Author.objects.get(id=id)
    args['articles'] = Article.objects.filter(author__name__exact=args['author_s'])
    args['projects'] = Category.objects.all()
    args['username'] = auth.get_user(request).username
    args['form_keywords'] = keywords_form
    return render(request, 'author_page.html', args)

def home(request):
    keywords_form = KeywordsForm
    args= {}
    args['articles'] = Article.objects.all()
    args['authors'] = Author.objects.all()
    args['projects'] = Category.objects.all()
    args['username'] = auth.get_user(request).username
    args['homes'] = Home.objects.all()
    args['form_keywords'] = keywords_form
    return render(request, 'home.html', args)