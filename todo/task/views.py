from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .serializers import TaskSerializer, TaskDetailSerializer, TaskCreateSerializer
from .permissions import IsOwner, isAdminOrReadOnly
from .models import Task
from django.shortcuts import get_object_or_404

# a.	GET /api/todo/ - получение списка задач содержащий поля ID, Заголовок, Срок исполнения, Выполнено
# b.	GET /api/todo/<id:int>/ - возвращает все данные по задаче с указанным ID, возвращаются все поля
# c.	POST /api/todo/ - создание новой задачи (новая задача не может быть сразу выполненной, игнорируем поле Выполнено)
# d.	PATCH /api/todo/<id:int>/ - редактирование задачи
# e.	DELETE /api/todo/<id:int>/ - редактирование задачи
# f.	POST /api/todo/<id:int>/execute/ - ручка для пометки задачи выполненной (опционально)

class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,IsOwner)
    
    def get_queryset(self):
        return self.request.user.tasks.all()
    def get_serializer_class(self):
        if self.action in ('retrieve', 'destroy', 'patch', 'update'):
            return TaskDetailSerializer
        if self.action in ('create',):
            return TaskCreateSerializer
        return TaskSerializer
