from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('tweet_list/', views.tweet_list, name='tweet_list'),
    path('create/', views.tweet_create, name='tweet_create'),
    path('edit/<int:pk_id>/', views.tweet_edit, name='tweet_edit'), 
    path('delete/<int:pk_id>/', views.tweet_delete, name='tweet_delete'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.userlogout, name='logout'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    # path('contact_me', views.contact_me, name='contact_me' ),

]