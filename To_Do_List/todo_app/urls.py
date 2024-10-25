from django.urls import path
from . import views

app_name='todo_app'

urlpatterns = [
    path('',views.TestPageView.as_view(), name='testpage'),
    path('todolist/',views.TodoListView.as_view(), name='todolist'),
    path('createtodo/',views.TodoCreateView.as_view(), name='todo-create'),

    # path('complit_todo/',views.TodoComplitView.as_view(), name='todo-complit'),
    # path('',TestPageView.as_view(), name='testpage'),
    
]