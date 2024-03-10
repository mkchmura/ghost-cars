from django.contrib import admin
from django.urls import path
from main.views import index, cars, list, test, about, all, category

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path('cars/<slug:slug>/', cars, name='cars'),
    path('list', list, name='list'),
    path('test', test, name='test'),
    path('about', about, name='about'),
    path('all', all, name='all'),
    path('category/<slug:slug>/', category, name="category")
]
