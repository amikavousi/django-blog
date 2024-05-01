from django.urls import path
from .views import index, show, author_show

urlpatterns = [
    path('index/', index, name='blog-index'),
    path('show/<int:id>', show, name='blog-show'),
    path('author-show/<int:user_id>', author_show, name='blog-author-show')
]
