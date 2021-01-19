from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, \
    category_view, like_view,search_view


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('category/<str:category>/', category_view, name='category'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add-post/', AddPostView.as_view(), name='add-post'),
    path('add-category/', AddCategoryView.as_view(), name='add-category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update-post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete-post'),
    path('like/<int:pk>', like_view, name='like-post'),
    path('search/', search_view, name="search-post")
]
