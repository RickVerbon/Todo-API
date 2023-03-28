from rest_framework.response import Response
from rest_framework import authentication, generics, permissions, status
from todo.models import Todo
from todo.serializes import TodoSerializer
from todo.permissions import IsOwnerOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token


# Create your views here.
class TodosListCreateAPIView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = TodoSerializer

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided"}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDestroyAPIView(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrReadOnly]

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer