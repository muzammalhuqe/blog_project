from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register('blog_list', views.BlogViewset)
router.register('category', views.CategoryViewset)
router.register('comment', views.CommentViewset)
# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    # path('post/', views.BlogViewset.as_view(), name = 'post'),
    # path('category/', views.CategoryViewset.as_view()),
    # path('comment/', views.CommentViewset.as_view()),
]
