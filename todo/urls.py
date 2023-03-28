
from django.urls import path
from todo.views import TodosListCreateAPIView, TodoDestroyAPIView

urlpatterns = [
    path('', TodosListCreateAPIView.as_view(), name="list-todos"),
    path('<int:pk>/delete', TodoDestroyAPIView.as_view(), name="delete-todo")
]