"""
URL configuration for cars_reviews_better project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.custom_logout_view, name='logout'),
    path('cars_reviews_admin/', views.cars_reviews_admin_view, name='cars_reviews_admin'),
    path('category_view/', views.category_view, name='category_view'),
    path('single_view/', views.single_view, name='single_view'),
    path('set_cookie_consent/', views.set_cookie_consent, name='set_cookie_consent'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('contact.html', views.contact, name="contact"),
    path('lista_noticias/', views.lista_noticias, name='lista_noticias'),
    path('noticias_imdb/', views.home_imdb, name='noticias_imdb'),
    path('motorpasion/', views.motorpasion_view, name='motorpasion'),
    path('carscoops/', views.carscoops_view, name='carscoops'),
    path('insideevs/', views.insideevs_view, name='insideevs'),
    path('carmagazine/', views.carmagazine_view, name='carmagazine'),
    path('autocar/', views.autocar_view, name='autocar'),
    path('autonews/', views.autonews_view, name='autonews'),
    path('buscar_noticias/', views.buscar_noticias, name='buscar_noticias'),
    path('populate-noticias/', views.populate_noticias, name='populate_noticias'),
]
