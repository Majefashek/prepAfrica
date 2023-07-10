from django.shortcuts import render, redirect
from .models import Subjects, Unit, Lesson
from django.views import View

class ManageSubjects(View):
    template_name = "subjects/manage_subjects.html"

    def get(self, request):
        subjects = Subjects.objects.all()
        return render(request, self.template_name, {'subjects': subjects})


class AddSubject(View):
    template_name = "subjects/add_subject.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        title = request.POST.get('title')
        enrolled_users = request.POST.getlist('enrolled_users')
        exam_type_id = request.POST.get('exam_type')

        subject = Subjects.objects.create(title=title, exam_type_id=exam_type_id)

        for user_id in enrolled_users:
            subject.enrolled_user.add(user_id)

        return redirect('manage_subjects')


class RemoveSubject(View):

    def get(self, request, subject_id):
        subject = Subjects.objects.get(id=subject_id)
        subject.delete()
        return redirect('manage_subjects')


class ViewUnits(View):
    template_name = "subjects/view_units.html"

    def get(self, request, subject_id):
        subject = Subjects.objects.get(id=subject_id)
        units = Unit.objects.filter(subject=subject)
        return render(request, self.template_name, {'subject': subject, 'units': units})


class ViewLessons(View):
    template_name = "subjects/view_lessons.html"

    def get(self, request, unit_id):
        unit = Unit.objects.get(id=unit_id)
        lessons = Lesson.objects.filter(subject=unit.subject)
        return render(request, self.template_name, {'unit': unit, 'lessons': lessons})

