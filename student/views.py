from rest_framework import generics
from rest_framework import viewsets

from .models import Student, Section
from .serializers import StudentSerializer, SectionSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class SectionStudentViewSet(generics.ListCreateAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        section_id = self.kwargs['section_id']
        return Student.objects.filter(section_id=section_id)

    def perform_create(self, serializer):
        section_id = self.kwargs['section_id']
        section = Section.objects.get(id=section_id)
        serializer.save(section=section)


