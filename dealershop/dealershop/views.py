from django.shortcuts import render

def urlpage(request):
    return render(request,'main.html')