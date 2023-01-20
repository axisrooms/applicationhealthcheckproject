from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author':'Prathap',
        'Title':'My app',
        'age': 22
    },
    {
        'author':'Vara lakshmi',
        'Title':'My app 2',
        'age': 22
    }

]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'webapp/home.html', context)


def about(request):
    return render(request, 'webapp/about.html')


