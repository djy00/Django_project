from django.db import models
from django.core.validators import (
    MaxLengthValidator,
    MinLengthValidator,
    MinValueValidator,
    MaxValueValidator
)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    owner = models.CharField(
        max_length=200,
        # default='all' #오류를 방지하기 위해 디폴트값을 설정할 수 있음
        blank=True,
        validators=[
            MinLengthValidator(3),
            MaxLengthValidator(10)
        ]
    )
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Survey(models.Model):
    user_name = models.CharField(max_length=200)    #이런 방식은 DB차원에서 제약을 거는것
    user_age = models.IntegerField(
        validators=[
            MinValueValidator(1),               #validator 방식은 유효성 검사같은 제약, DB에서 오류가 나기전 검사를 통해 오류 방지
            MaxValueValidator(100)])

    def __str__(self):
        return f"{self.user_name}_{self.user_age}"