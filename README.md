### Django Notion Page
✅https://dji00.notion.site/django-10aa108359b480aabb58d5c2f2122aab?pvs=4
### 최근 업로드
😊24-10-17: Form: Django Form을 활용 데이터 추가 & 투표 페이지 제작   
😊24-10-15: Model & Database    
😊24-10-11: templates  
  
### 데이터추가 코드(shell)
```
from home.models import Question, Choice
from django.utils import timezone

# 질문 추가
q1 = Question.objects.create(question_text="What is your favorite sport?", pub_date=timezone.now())
q2 = Question.objects.create(question_text="Which social media platform do you use most frequently?", pub_date=timezone.now())
q3 = Question.objects.create(question_text="Which fruit do you eat most often?", pub_date=timezone.now())

# 선택지 추가 - 첫 번째 질문에 대한 선택지
Choice.objects.create(choice_text="Soccer", votes=0, question=q1)
Choice.objects.create(choice_text="Basketball", votes=0, question=q1)
Choice.objects.create(choice_text="Swimming", votes=0, question=q1)
Choice.objects.create(choice_text="Tennis", votes=0, question=q1)
Choice.objects.create(choice_text="Running", votes=0, question=q1)

# 선택지 추가 - 두 번째 질문에 대한 선택지
Choice.objects.create(choice_text="Facebook", votes=0, question=q2)
Choice.objects.create(choice_text="Instagram", votes=0, question=q2)
Choice.objects.create(choice_text="Twitter", votes=0, question=q2)
Choice.objects.create(choice_text="TikTok", votes=0, question=q2)
Choice.objects.create(choice_text="LinkedIn", votes=0, question=q2)

# 선택지 추가 - 세 번째 질문에 대한 선택지
Choice.objects.create(choice_text="Apple", votes=0, question=q3)
Choice.objects.create(choice_text="Banana", votes=0, question=q3)
Choice.objects.create(choice_text="Grape", votes=0, question=q3)
Choice.objects.create(choice_text="Orange", votes=0, question=q3)
Choice.objects.create(choice_text="Strawberry", votes=0, question=q3)

```
