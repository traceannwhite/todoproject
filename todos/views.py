from .models import Todo
from rest_framework import viewsets, permissions
from .serializers import TodoSerializer

# Create your views here.
class TodoViewSet(viewsets.ModelViewSet):
    ## Give it the main query for the index route 
    queryset = Todo.objects.all()
    #the serializer for serializing
    serializer_class = TodoSerializer
    ## optional permissions
    permission_classes = [permissions.AllowAny]
    
