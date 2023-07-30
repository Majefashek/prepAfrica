from rest_framework import serializers
from .models import Subjects,Enrollment, Unit, Lesson, LessonVideo
from authentication_app.serializers import CustomUserSerializer

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

class UnitSerializer(serializers.ModelSerializer):
    #lessons:LessonSerializer(many=True, read_only=True)
    lessons = serializers.SerializerMethodField()
    class Meta:
        model = Unit
        fields = '__all__'  
    def get_lessons(self, unit):
        lessons = Lesson.objects.filter(unit=unit)
        serializer = LessonSerializer(lessons, many=True)
        return serializer.data



class LessonSerializer(serializers.ModelSerializer):
    videos=serializers.SerializerMethodField()
    #Videos:LessonSerializer(many=True, read_only=True) 
    class Meta:
        model = Lesson
        fields = '__all__'
    def get_videos(self, lesson):
        lessons = LessonVideo.objects.filter(lesson=lesson)
        serializer = LessonVideoSerializer(lessons, many=True)
        return serializer.data      
