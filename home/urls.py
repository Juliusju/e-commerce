from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('signup/', views.registerPage, name='signup'),
    path('signin/', views.loginPage, name='signin'),
]