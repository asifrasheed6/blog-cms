from django.urls import path
from . import views

app_name = 'cms'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('posts/<int:pk>/', views.PostView.as_view(), name='post'),
]

