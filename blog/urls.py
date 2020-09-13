from django.urls import path
from .views import *


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('search/', Search.as_view(), name='search'),
    path('category/<slug:slug>/', PostsByCategory.as_view(), name='category'),
    path('post/<slug:slug>/', DetailPost.as_view(), name='post'),
    path('tag/<slug:slug>/', PostsByTag.as_view(), name='tag'),
]