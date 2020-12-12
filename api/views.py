from api import models, serializers
from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
    ListCreateAPIView,
    DestroyAPIView
)

# Create your views here.
class StudentListView(ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

class StudentDetailView(RetrieveUpdateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

class StudentDeleteView(DestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer



