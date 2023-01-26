from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class QuestionsFor10th(models.Model):
    # Q_id = models.AutoField()
    Q_name = models.CharField(max_length=3,default="q00")
    Question = models.CharField(max_length=300)
    op_1 = models.CharField(max_length=50)
    op_2 = models.CharField(max_length=50)
    op_3 = models.CharField(max_length=50)
    op_4 = models.CharField(max_length=50)
    correct_ans = models.CharField(max_length=1)
    # Q_Auto= models.AutoField()
    
    def __str__(self):
        return self.Question

class QuestionsFor12th(models.Model):
    # Q_id = models.AutoField()
    Q_name = models.CharField(max_length=3,default="q00")
    Question = models.CharField(max_length=300)
    op_1 = models.CharField(max_length=50)
    op_2 = models.CharField(max_length=50)
    op_3 = models.CharField(max_length=50)
    op_4 = models.CharField(max_length=50)
    correct_ans = models.CharField(max_length=1)
    # Q_Auto= models.AutoField()
    
    def __str__(self):
        return self.Question