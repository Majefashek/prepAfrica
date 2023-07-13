from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from .models import Question,Test,Option 
from django.urls import reverse
from django.shortcuts import get_object_or_404, render,redirect
from django.core.paginator import Paginator
from django.views import View
from django.http import JsonResponse
import json



class MyTestView(View):
    template_name='Tests/ViewTests.html'
    def get(self,request):
        tests=Test.objects.all()
        return render(request,self.template_name,{'tests':tests})

class TestEvaluationView(View):
    def get(self, request, test_id):
        test = get_object_or_404(Test, id=test_id)
        questions = Question.objects.filter(test=test).order_by('id')
        options=Option.objects.all()
        total_questions = questions.count()
        paginator = Paginator(questions, 1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'test': test,
            'page_obj': page_obj,
            'total_questions': total_questions,
            'question':questions,
            'options':options,
            'paginator':paginator
        }
        
        return render(request, 'Tests/Test.html', context)


    def post(self, request, test_id):
        test = get_object_or_404(Test, id=test_id)
        questions = Question.objects.filter(test=test).order_by('id')
        total_questions = questions.count()
        data = json.loads(request.body)
        answers = data.get('answers', {})
        correct_options = Option.objects.filter(question__test_id=test_id, is_correct=True)
        correct_answers=0
        skipped=0
        wrong_answers=0
        for question_id, selected_option_id in answers.items():
            # Check if the selected option is correct for the respective question
            if correct_options.filter(question_id=question_id, id=selected_option_id).exists():
                correct_answers += 1
            elif answers[question_id]=='':
                skipped+=1
            else:
                wrong_answers+=1
        score = (correct_answers / total_questions) * 100
        test.score = score
        test.correct_answers = correct_answers
        test.wrong_answers = wrong_answers
        test.save()  
        return JsonResponse({'testId':test_id})    
          
class ViewTestResult(View):
    def get(self,request,test_id):
        test=get_object_or_404(Test,id=test_id)
        return render(request, 'Tests/evaluate_test.html',{'test':test})
