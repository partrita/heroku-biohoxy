from django.urls import path
from . import views

app_name = "page"

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("team", views.team, name="team"),
    # path('blog', views.blog, name='blog'),
    path("contact", views.contact, name="contact"),
]
