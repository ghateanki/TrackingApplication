from django.urls import path
from . import views
from .views import HomeView,ArticleDetailView,AddProjectView,UpdatePostView,DeletePostView

urlpatterns = [
    # path('', views.home,name="home"),
    path('', views.home, name="home"),
    path('article/<int:pk>',ArticleDetailView.as_view(),name="article-detail"),
    path('add_project/', views.add_project, name='add_project'),
    path('article/edit/<int:pk>',UpdatePostView.as_view(),name="update_post"),
    path('article/edit/<int:pk>/remove',DeletePostView.as_view(),name="delete_post"),
]