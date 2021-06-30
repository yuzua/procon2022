from django.db import models

# Create your models here.
class Sample(models.Model):

    LEVEL_SET = (
        ('easy', "初級"),
        ('normal', "中級"),
        ('hard', "上級"),
    )

    fullname = models.CharField(max_length=32)
    level = models.CharField(choices=LEVEL_SET, default='easy', max_length=8)
    score = models.IntegerField()
    is_checked =  models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)