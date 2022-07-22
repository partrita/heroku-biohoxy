from django.shortcuts import render

def index(request):
    return render(request, 'page/index.html', {})

def about(request):
    return render(request, 'page/about.html',{})

# cc

def team(request):
    return render(request, 'page/team.html', {})

def contact(request):
    return render(request, 'page/contact.html', {})
