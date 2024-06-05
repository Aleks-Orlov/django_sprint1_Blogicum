from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/postst/<int:id>/', views.post_detail, name='post_detail'),
    path('blog/category/<slug:category_slug>/', views.category_post, name='category_post'),
]