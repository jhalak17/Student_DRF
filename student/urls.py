from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, SectionViewSet, SectionStudentViewSet

ROUTER = DefaultRouter(trailing_slash=False)
ROUTER.register(r"sections", SectionViewSet, basename="sections")
ROUTER.register(r"students", StudentViewSet, basename="students")

urlpatterns = [
    path("", include(ROUTER.urls)),
    path("section/<int:section_id>/students", 
         SectionStudentViewSet.as_view(), 
         name="section-student-list"),
]