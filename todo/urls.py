
from django.urls import path
from todo.views import TodoDetailView, TodoListCreateView

urlpatterns = [
    path('', TodoListCreateView.as_view(), name="todo-list"),
    path('<int:pk>/', TodoDetailView.as_view(), name="todo-detail")

]