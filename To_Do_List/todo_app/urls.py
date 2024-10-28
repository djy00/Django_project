from django.urls import path
from . import views

app_name='todo_app'

urlpatterns = [
    path('',views.TestPageView.as_view(), name='testpage'),
    path('todolist/',views.TodoListView.as_view(), name='todolist'),
    path('createtodo/',views.TodoCreateView.as_view(), name='todo-create'),
    path('detail_todo/<int:pk>',views.TodoDetailView.as_view(), name='todo-detail'),
    path('update/<int:pk>',views.TodoUpdateView.as_view(), name='todo-update'),
    path('delete/<int:pk>',views.TodoDeleteView.as_view(),name='todo-delete')

    # path('complit_todo/',views.TodoComplitView.as_view(), name='todo-complit'),
    # path('',TestPageView.as_view(), name='testpage'),
    
]