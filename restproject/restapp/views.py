from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated ,AllowAny
from django.contrib.auth import get_user_model


from .serializers import Todoserializer , UserSerializers
from .models import Todo


class TodoViewset(viewsets.ModelViewSet):
    permission_classes =(IsAuthenticated,)
    queryset= Todo.objects.all().order_by('-date_created')
    serializer_class=Todoserializer

class CompletedTodoViewset(viewsets.ModelViewSet):
    queryset= Todo.objects.all().order_by('-date_created').filter(completed=True)
    serializer_class=Todoserializer

class DueTodoViewset(viewsets.ModelViewSet):
    queryset= Todo.objects.all().order_by('-date_created').filter(completed=False)
    serializer_class=Todoserializer

class CreateUserview(CreateAPIView):
    model=get_user_model()
    permission_classes=(AllowAny,)
    serializer_class=UserSerializers