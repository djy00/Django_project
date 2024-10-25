from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.urls import reverse_lazy

from todo_app.forms import Todoform
from todo_app.models import Todo


class TestPageView(TemplateView):
    template_name = "todo_app/test.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["latest_articles"] = Article.objects.all()[:5]
    #     return context

class TodoListView(ListView):
    model = Todo
    # queryset = Todo.objects.filter(complit__iexact='0')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class TodoCreateView(CreateView):
    model = Todo
    fields = ['todo_list','complit']
    
    success_url = reverse_lazy("todo_app:testpage")
    def form_valid(self, form):
        form.instance.date = timezone.now().date() 
        return super().form_valid(form)

# class TodoComplitView():
 

