from django.contrib import admin
from django.urls import path
from . import views

app_name='cloud'

urlpatterns = [
    path('',views.HomepageView.as_view(),name="home"),
    path('<int:id>/', views.PartitionView,name="partition"),
    path('<int:id1>/<int:id2>/',views.FolderView,name="folder"),
    path('add/partition/',views.UserPartitionCreateView.as_view(),name="add_partition"),
    path('add/folder/<int:id>/',views.FolderCreateView.as_view(),name="add_Folder"),
    path('<int:id1>/<int:id2>/add/file/',views.FileCreateView.as_view(),name="add_File"),
    path('delete/partition/<int:pk>/',views.UserPartitionDeleteView.as_view(),name="delete_partition"),
    path('delete/Folder/<int:pk>/',views.FolderDeleteView.as_view(),name="delete_folder"),
    path('delete/file/<int:pk>/',views.FileDeleteView.as_view(),name="delete_file"),
    path('update/partition/<int:pk>/',views.UserPartitionUpdateView.as_view(),name="update_partition"),
    path('update/Folder/<int:pk>/',views.FolderUpdateView.as_view(),name="update_folder"),   
]
