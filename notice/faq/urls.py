from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.new, name='new'),
    path('detail/<int:blog_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('postcreate/', views.postcreate, name='postcreate'),
    path('update/<int:blog_id>/', views.update, name='update'),
    path('delete/<int:blog_id>/', views.delete, name='delete'),
    path('search', views.search, name='search'),
    path('management', views.management, name='management'),
    path('edit', views.edit, name='edit'),
    path('eamil', views.email, name='email'),
    path('edit_info', views.edit_info, name='edit_info'),
    path('majorpost', views.majorpost, name='majorpost'),
    path('newpost', views.newpost, name='newpost')
]
