from django.shortcuts import render

def index(request):
    return render(request, 'page/index.html', {})

def about(request):
    return render(request, 'page/about.html',{})

def blog(request):
    return render(request, 'page/blog.html', {})

def team(request):
    return render(request, 'page/team.html', {})

def contact(request):
    return render(request, 'page/contact.html', {})
