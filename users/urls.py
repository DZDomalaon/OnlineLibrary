from django.urls import path
from . import views
from books.views import SearchBookView, FilterBookView

app_name = 'users'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/',views.LogoutView.as_view(), name='logout'),
    path('homepage/', views.HomePageView.as_view(), name='homepage'),
    path('register/', views.RegisterView.as_view(), name='register'),  
    path('<int:pk>/ownedbooks', views.OwnedBooksView.as_view(), name='ownedbooks'),
    path('<int:pk>/borrowedbooks', views.BorrowedBooksView.as_view(), name='borrowedbooks'),
    path('<int:pk>/edituser', views.EditUserView.as_view(), name='edituser'),
    path('search/', SearchBookView.post, name='search'),
    path('filter/', FilterBookView.post, name='filter'),
]