from django.shortcuts import render, get_object_or_404
from django.http import (HttpResponse,HttpResponseRedirect)
from django.urls import reverse
from .models import Question, Choice
from django.db.models import F


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "home/index2.html", context)

# def index(request):
#     # return HttpResponse("Hello, world. You're at the polls index.")
#     # return HttpResponseRedirect(
#     #     reverse('detail', args=[1]))
#     # return HttpResponseRedirect(
#     #     reverse('detail', kwargs={'question_id': 1}))
#     ctx = {
#         "greetings": "Hello there!",
#         "location": {
#             "city": "Seoul",
#             "country": "South Korea"
#         },
#         "languages": ["Korean", "English"]
#     }
#     return render(request, 'home/index.html', context=ctx)


def detail(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request, "home/detail.html", {"question": question})

def results(request, question_id):
    # 객체가 존재하지 않을 경우 404 에러를 발생 => 404 에러 페이지로 이동
    question = get_object_or_404(Question,pk=question_id)
    return render(request, "home/results.html", {"question": question})

def vote(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except(KeyError, Choice.DoesNotExist):
        return render(
            request,
            "home/detail.html",
            {
                'question':question,
                'error_message': "You didn't select a choice."
            }
        )
    else:
        # F: 데이터베이스 필드간의 직접 비교 또는 필드 값을 참조하여 업데이트할 때 사용되는 표현식
        selected_choice.votes = F("votes")+1
        selected_choice.save()
        return HttpResponseRedirect(reverse("home:results", args=(question.id,)))
    