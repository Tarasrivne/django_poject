from django.urls import path
from . import views


urlpatterns = [
    # path('', views.home, name="home"),
    # path('about/', views.about, name="about"),
    # path('Menu/', views.Menu, name="Menu"),
    # path('book/', views.book, name="book"),
    # path('home/', views.form_view),
    # path('about/', views.about),
    # path('menu/', views.menu),
    # path('menu', views.menu_id),

    path('home_ex/', views.home, name='home_ex'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]