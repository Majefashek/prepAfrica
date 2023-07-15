from django.shortcuts import render, redirect
from .models import Subjects, Unit, Lesson
from django.views import View
from rest_framework import generics
from .serializers import SubjectsSerializer,UnitSerializer,LessonSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

class ViewSubjects(generics.ListAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectsSerializer

#class AddSubject(generics.CreateAPIView):
#    serializer_class = SubjectsSerializer

class ViewUnits(generics.ListAPIView):
    serializer_class = UnitSerializer

    def get_queryset(self):
        subject_id = self.kwargs['subject_id']
        return Unit.objects.filter(subject_id=subject_id)

class ViewLessons(generics.ListAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self):
        unit_id = self.kwargs['unit_id']
        return Lesson.objects.filter(subject__unit__id=unit_id)
    
class SearchView(APIView):
    def get(self, request, **kwargs):
        querystring = kwargs['query']
        Units= Unit.objects.filter(title__icontains=querystring)
        subjects= Subjects.objects.filter(title__icontains=querystring)
        unit_serialized = UnitSerializer(Units, many=True)
        subject_serialized = SubjectsSerializer(subjects, many=True)
        data = {
            "units": unit_serialized.data,
            "subjects": subject_serialized.data
        }
        return Response(data)
    