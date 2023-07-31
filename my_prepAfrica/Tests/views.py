from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import generics,status
from .models import Test, Question, Option,Unit,Subjects,Lesson
from .serializers import TestSerializer, QuestionSerializer,OptionSerializer
from rest_framework.exceptions import NotFound


class MyTestView(generics.ListAPIView):
    queryset=Test.objects.all()
    serializer_class=TestSerializer

class MyUnitTests(APIView):
    def get(self, request, **kwargs):
        try:
            unit_id = kwargs.get('unit_id')
            unit = Unit.objects.get(id=unit_id)
            test = Test.objects.filter(unit=unit)
            test_serialized = TestSerializer(test)
            return Response({'test': test_serialized})
        except Unit.DoesNotExist:
            raise NotFound('Unit not found.')
        except Test.DoesNotExist:
            raise NotFound('Test not found.')
        

class MySubjectTests(APIView):
    def get(self, request, **kwargs):
        try:
            subject_id = kwargs.get('subject_id')
            subject = Subjects.objects.get(id=subject_id)
            test = Test.objects.filter(subject=subject)
            test_serialized = TestSerializer(test, many=True)
            return Response({'test': test_serialized.data})
        except Subjects.DoesNotExist:
            raise NotFound('Unit not found.')
        except Test.DoesNotExist:
            raise NotFound('Test not found.')
class MyLessonTests(APIView):
    def get(self,request,**kwargs):
        try:
            lesson_id = kwargs.get('lesson_id')
            subject = Lesson.objects.get(id=lesson_id)
            test = Test.objects.select_related('unit').get(unit=unit)
            test_serialized = TestSerializer(test)
            return Response({'test': test_serialized.data})
        except Subjects.DoesNotExist:
            raise NotFound('Unit not found.')
        except Test.DoesNotExist:
            raise NotFound('Test not found.')



class Myoptions(generics.ListAPIView):
    queryset=Option.objects.all()
    serializer_class=OptionSerializer

class MyQuestions(generics.ListAPIView):
    queryset=Question.objects.all()
    serializer_class=QuestionSerializer
   
   

class TestEvaluationView(APIView):
    def get(self, request, test_id):
        test = get_object_or_404(Test, id=test_id)
        questions = Question.objects.filter(test=test).order_by('id')
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)


    def post(self, request, test_id):
        test = get_object_or_404(Test, id=test_id)
        questions = Question.objects.filter(test=test).order_by('id')
        total_questions = questions.count()
        data = request.data
        answers = data.get('answers', {})
        #answers=json.loads(MYanswers)

        correct_options = Option.objects.filter(question__test_id=test_id, is_correct=True)
        correct_answers = 0
        skipped = 0
        wrong_answers = 0
        for question_id, selected_option_id in answers.items():
            # Check if the selected option is correct for the respective question
            if correct_options.filter(question_id=question_id, id=selected_option_id).exists():
                correct_answers += 1
            elif answers[question_id] == '':
                skipped += 1
            else:
                wrong_answers += 1
        score = (correct_answers / total_questions) * 100
        test.score = score
        test.correct_answers = correct_answers
        test.wrong_answers = wrong_answers
        test.save()
        testserialized=TestSerializer(test)
        mytest=testserialized.data
        return Response(mytest)


class ViewTestResult(generics.RetrieveAPIView):
    queryset=Test.objects.all()
    serializer_class=TestSerializer