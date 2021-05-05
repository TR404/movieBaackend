from rest_framework import generics
from rest_framework.response import Response
from .serializer import ProjectSerializer
from .models import Project
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class ProjectCreateApi(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    authClass = [BasicAuthentication]
    permiClass = [IsAuthenticated]
    
class ProjectApi(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
    
class ProjectUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    authClass = [BasicAuthentication]
    permiClass = [IsAuthenticated]
    
class ProjectDeleteApi(generics.DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    authClass = [BasicAuthentication]
    permiClass = [IsAuthenticated]
