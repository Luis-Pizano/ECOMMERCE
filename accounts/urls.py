from django.urls import include, path # type: ignore

from . import views

urlpatterns = [
    path('register/', views.register, name= 'register'),
    path('login/', views.login, name= 'login'),
    path('logout/', views.logout, name= 'logout'),
]
