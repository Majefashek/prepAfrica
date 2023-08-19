from rest_framework import serializers
from .models import Subjects,Enrollment, Unit, Lesson, LessonVideo
from authentication_app.serializers import CustomUserSerializer
from ProgressTrackkingApp.models import ProgressTracker

class SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    subject=SubjectsSerializer()
    class Meta:
        model = Enrollment
        fields = '__all__'



class LessonVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model=LessonVideo
        fields='__all__'



class LessonSerializer(serializers.ModelSerializer):
    videos = serializers.SerializerMethodField()
    completion_status = serializers.SerializerMethodField()
    completed_datetime = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = '__all__'

    def get_videos(self, lesson):
        videos = LessonVideo.objects.filter(lesson=lesson)
        serializer = LessonVideoSerializer(videos, many=True)
        return serializer.data

    def get_completion_status(self, lesson):
        user = self.context.get('user', None)
        if user:
            #return True
            is_completed = ProgressTracker.objects.filter(
                user=user,
                completed_lessons__id=lesson.id
            ).exists()
            return is_completed
        return None

    def get_completed_datetime(self, lesson):
        user = self.context.get('user', None)
        if user:
            progress_tracker = ProgressTracker.objects.filter(
                user=user,
                completed_lessons__id=lesson.id
            ).first()
            if progress_tracker:
                return progress_tracker.completed_datetime
        return None
    

class UnitSerializer(serializers.ModelSerializer):
    lessons = serializers.SerializerMethodField()
    completion_status = serializers.SerializerMethodField()
    completed_datetime = serializers.SerializerMethodField()
    class Meta:
        model = Unit
        fields = '__all__' 

    def get_lessons(self,unit):
        user = self.context.get('user', None)
        lessons=Lesson.objects.filter(unit=unit)
        serializer = LessonSerializer(lessons, many=True,context={'user':user})
        return serializer.data
    
    def get_completion_status(self,unit):
        user = self.context.get('user', None)
        if user:
            #return "mouse"
            is_completed = ProgressTracker.objects.filter(
                user=user,
                completed_units__id=unit.id
            ).exists()
            return is_completed
        return None
    
    def get_completed_datetime(self, unit):
        user = self.context.get('user', None)
        if user:
            progress_tracker = ProgressTracker.objects.filter(
                user=user,
                completed_units__id=unit.id
            ).first()
            if progress_tracker:
                return progress_tracker.completed_datetime
        return None