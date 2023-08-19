from django.shortcuts import render, redirect
from .models import Subjects, Unit, Lesson,Enrollment
from django.views import View
from rest_framework import generics
from .serializers import SubjectsSerializer,UnitSerializer,LessonSerializer,EnrollmentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication 
from django.db.models import OuterRef, Exists
from ProgressTrackkingApp.models import ProgressTracker

class EnrollSubject(APIView):

    authentication_classes = [JWTAuthentication]  # Use JWT Authentication
    permission_classes = [IsAuthenticated]
    def post(self,request,**kwargs):
        subjectId=kwargs['subject_id']
        subject=Subjects.objects.get(id=subjectId)
        user = request.user
        try:
            Enrolled = Enrollment.objects.get(user=user, subject=subject)
            return Response({'Error':'Already Enrolled'})
        except Enrollment.DoesNotExist:
            enrollmentObj=Enrollment.objects.create(user=user,subject=subject)
            EnrollmentSerialized=EnrollmentSerializer(enrollmentObj)
            EnrolledSubject=EnrollmentSerialized.data
            return Response({'sucess':'Enrolled'})
     
            
        

class GetEnrolledSubject(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]  # Use JWT Authentication
    permission_classes = [IsAuthenticated]
    serializer_class=EnrollmentSerializer
    def get_queryset(self):
        user=self.request.user
        EnrolledSubject=Enrollment.objects.filter(user=user,subject__isnull=False)
        return EnrolledSubject
        


class ViewSubjects(generics.ListAPIView):
    #authentication_classes = [JWTAuthentication]  # Use JWT Authentication
    #permission_classes = [IsAuthenticated]
    queryset = Subjects.objects.all()
    serializer_class = SubjectsSerializer

class ViewUnits(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]  # Use JWT Authentication
    permission_classes = [IsAuthenticated]
    serializer_class = UnitSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user
        return context


    def get_queryset(self):
        user = self.request.user
        subject_id = self.kwargs['subject_id']
        subject=Subjects.objects.get(id=subject_id)
        
        # Initialize the UnitSerializer with the context {'user': user}
        return Unit.objects.filter(subject=subject)
class ViewLessons(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]  # Use JWT Authentication
    permission_classes = [IsAuthenticated]
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
    