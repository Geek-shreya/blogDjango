from django.urls import path
from . import views 

urlpatterns = [
    # API to postComment 
    path('postComment', views.postComment, name='postComment'),
    
    path('', views.blogHome, name='blogHome'),  
    path('<str:slug>', views.blogPost, name='blogPost'),
]
