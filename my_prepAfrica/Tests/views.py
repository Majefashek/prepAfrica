from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from .models import Question,Test,Option 
from django.urls import reverse
from django.shortcuts import get_object_or_404, render,redirect
from django.core.paginator import Paginator
from django.views import View


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
        #return render(request, 'Tests/evaluate_test.html')
        
        question_id = request.POST.get('question_id')
        selected_option_id = request.POST.get('selected_option')
        request.session.setdefault('answers', {})[question_id] = selected_option_id

        test = get_object_or_404(Test, id=test_id)
        questions = Question.objects.filter(test=test).order_by('id')
        total_questions = questions.count()
        paginator = Paginator(questions, 1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        answers = request.session.get('answers')
        if page_obj.has_next():
            next_page_number = page_obj.next_page_number()
            redirect_url = reverse('evaluate_test', args=[test_id]) + f'?page={next_page_number}'
            return redirect(redirect_url)


        correct_answers = sum(
            1 for question_id, selected_option_id in answers.items()
            if Question.objects.filter(
                id=question_id, options__id=selected_option_id, options__is_correct=True
            ).exists()
        )
        wrong_answers = total_questions - correct_answers

        
        score = (correct_answers / total_questions) * 100
        test.score = score
        test.correct_answers = correct_answers
        test.wrong_answers = wrong_answers
        test.save()

        context = {
            'test': test,
            'page_obj': page_obj,
            'total_questions': total_questions,
            'incorrect': wrong_answers}

        return render(request, 'Tests/evaluate_test.html', context)
