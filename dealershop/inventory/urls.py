from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('', views.MainView.as_view(),name='main'),
    path('car/', views.CarFormView.as_view(),name="car")
]
