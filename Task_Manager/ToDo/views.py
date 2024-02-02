from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from rest_framework.exceptions import PermissionDenied
from django_filters import rest_framework as filters


class TaskFilter(filters.FilterSet):
    class Meta:
        model = Task
        fields = ['status']

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = TaskFilter

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        if serializer.instance.user != self.request.user:
            # No permitir que el usuario modifique tareas de otros usuarios
            raise PermissionDenied("No tienes permiso para modificar esta tarea.")
        serializer.save()
