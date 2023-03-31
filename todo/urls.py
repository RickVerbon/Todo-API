
from django.urls import path
from todo.views import TodosListCreateAPIView, TodoDestroyAPIView, TodoUpdateView, TodoDetailView

urlpatterns = [
    path('', TodosListCreateAPIView.as_view(), name="list-todos"),
    path('<int:pk>/delete', TodoDestroyAPIView.as_view(), name="delete-todo"),
    path('<int:pk>/update', TodoUpdateView.as_view(), name="update-todo"),
    path('<int:pk>/detail', TodoDetailView.as_view(), name="detail-todo")
]