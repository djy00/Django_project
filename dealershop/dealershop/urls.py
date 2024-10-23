from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    # path('', views.urlpage),
    path('admin/', admin.site.urls),
    path('inventory/', include('inventory.urls')),
    path('',RedirectView.as_view(url='inventory/'))
]
