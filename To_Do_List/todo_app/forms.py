from django import forms

class Todoform(forms.Form):
    todo_list = forms.CharField()
    date =forms.DateTimeField()
    complit = forms.BooleanField()
    