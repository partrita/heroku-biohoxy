from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path("blog/", include("blog.urls")),
    path("admin/", admin.site.urls),
    path("", include("page.urls")), 
]
