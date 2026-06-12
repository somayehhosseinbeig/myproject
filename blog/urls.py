from django.urls import path
from blog.views import *
from . import views

app_name = 'blog'

urlpatterns = [
    path('',views.blog_view, name='index'),
    path('single',blog_single, name='single')
]
