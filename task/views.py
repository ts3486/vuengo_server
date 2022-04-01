from django.shortcuts import render

# Create your views here.
from .models import Task
from .serializer import TaskSerializer

from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class TaskViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    query = Task.objects.all()
    serialier_class = TaskSerializer