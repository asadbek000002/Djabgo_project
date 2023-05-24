from django.urls import path
from .views import List_view, Detail_view, Create_view, Update_view, Delete_view

urlpatterns = [
    path('', List_view.as_view(), name='home'),
    path('post/<int:pk>/', Detail_view.as_view(), name='post_detail'),
    path('post/new', Create_view.as_view(), name='post_new'),
    path('post/<int:pk>/update', Update_view.as_view(), name='post_update'),
    path('post/<int:pk>/delete', Delete_view.as_view(), name='post_delete'),
]