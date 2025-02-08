from django.contrib import admin
from django.urls import path
from todos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/', views.todo_list, name='todo_list'),
    path('todos/create/', views.create_todo, name='create_todo'),
    path('todos/<int:id>/', views.todo_detail, name='todo_detail'),
    path('todos/<int:id>/delete/', views.delete_todo, name='delete_todo'),
    path('api/todos/', views.api_todo_list, name='api_todo_list'),
    path('api/todos/<int:id>/', views.api_todo_detail, name='api_todo_detail'),
]
