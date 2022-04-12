from django.urls import path
from .views import BlogListView #Nos traemos la clase de view

app_name="blog"

urlpatterns = [
    path('', BlogListView.as_view(), name="home"),
]
 