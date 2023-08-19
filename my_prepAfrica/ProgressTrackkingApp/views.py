from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import generics,status
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404, render
from django.views import View
from .models import ProgressTracker, Unit, Lesson
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication 



class UpdateProgressView(APIView):
    authentication_classes = [JWTAuthentication]  # Use JWT Authentication
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user 
        recently_completed_unit_id = request.POST.get('completed_unit_id')
        recently_completed_lesson_id = request.POST.get('completed_lesson_id')
        responses=[]
        progress_tracker, created = ProgressTracker.objects.get_or_create(user=user)
        if recently_completed_unit_id:
            unit_completed = Unit.objects.get(id=recently_completed_unit_id)
            progress_tracker.completed_units.add(unit_completed)
            responses.append('unit completed updated')
        if recently_completed_lesson_id:
            lesson_completed = Lesson.objects.get(id=recently_completed_lesson_id)
            progress_tracker.completed_lessons.add(lesson_completed)
            responses.append('lesson completed updated')
            
        return Response(responses)

            