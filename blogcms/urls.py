from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'cms'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('posts/<int:pk>/', views.PostView.as_view(), name='post'),
    path('profile/<int:pk>/', login_required(views.Profile.as_view()), name='profile'),
    path('comment/', views.addComment, name='comment'),
]

