from django.urls import path
# from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView
from . import views


urlpatterns = [
    path('',views.home,  name='signup'),
   
]