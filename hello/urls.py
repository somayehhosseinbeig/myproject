from django.urls import path
from . import views
# from hello.views import * در صورتی که این مدلی بنویسیم دیگه نمی خواد نام
# views.indexرا بنویسیم 
#path("", index, name = "index")  

urlpatterns = [
    path("", views.index, name = "index"),
    path("<str:name>", views.greet, name = "greet"),
    path("somayeh", views.somayeh, name = "somayeh"),
    path("arnika", views.arnika, name = "arnika")
]