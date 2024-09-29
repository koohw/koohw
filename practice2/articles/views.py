from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
# 메인페이지
def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

# 게시글 생성
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        
        if form.is_valid():
            # 생성할 때는 instance=article 없음. article=form.save()
            article = form.save()
            return redirect('articles:detail', article.pk)
    
    else:
        form = ArticleForm()
    
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)

# 게시글 삭제
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


# 게시글 수정
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)

        if form.is_valid():
            # 수정할 때는 instance=article 있고, article.save()
            form.save()
            return redirect('articles:detail', article.pk)
        
    else:
        form = ArticleForm(instance=article)

    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)

    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)