from django.shortcuts import render, HttpResponse


def home_page(request):
    return render(request, 'index.html')


def news(request):
    return render(request, 'news.html')


def news2(request):
    return render(request, 'news2.html')
