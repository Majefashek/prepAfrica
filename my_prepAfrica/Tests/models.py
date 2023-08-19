from django.db import models
from SubjectSelection.models import Subjects,Unit,Lesson

class Test(models.Model):
    title = models.CharField(max_length=100,null=True)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, blank=True, null=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, blank=True, null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, blank=True, null=True)
    score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    correct_answers = models.PositiveIntegerField(blank=True, null=True)
    wrong_answers = models.PositiveIntegerField(blank=True, null=True)
    skipped=models.PositiveBigIntegerField(blank=True,null=True)
   
    def __str__(self):
       return self.title
   

class Question(models.Model):
    title=models.CharField(max_length=50,null=True)
    test = models.ForeignKey(Test, related_name='questions', on_delete=models.CASCADE)
    question_text = models.TextField()
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['test', 'id'], name='question_belongs_to_test')
        ]
    def __str__(self):
        return self.title



class Option(models.Model):
    title = models.CharField(max_length=100,null=True)
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    option_text = models.CharField(max_length=300)
    explanation = models.CharField(max_length=1000)
    is_correct = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['question'], condition=models.Q(is_correct=True), name='unique_correct_option')
        ]
    def __str__(self):
        return self.title