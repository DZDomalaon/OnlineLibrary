from django.urls import path
from . import views 

app_name = 'books'
urlpatterns = [
    path('createbook/', views.BookView.post, name='createbook'),
    path('<int:pk>/bookpage', views.BookView.get, name='bookpage'),
    # path('<int:pk>/postpage/addcomment', views.CommentView.post, name='addcomment'),
    # path('<int:pk>/postpage/updatecomment', views.CommentView.update_comment, name='updatecomment'),
    # path('<int:pk>/postpage/deletecomment', views.CommentView.delete, name='deletecomment'),
    path('<int:pk>/bookpage/editbook', views.BookView.update_book, name='editbook'),
    path('<int:pk>/bookpage/deletebook', views.BookView.delete, name='deletebook'),
]