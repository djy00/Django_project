from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView

class MainView(TemplateView):
    template_name = "inventory/main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = "Joon"
        return context

from django.views.generic.edit import FormView
from inventory.forms import CarForm
from django.urls import reverse_lazy, reverse
# FBV와 CBV의 Execution 타이밍이 다름
# CBV는 class가 호출되면 Execution이 되기 때문에 그냥 reverse를 사용하면 에러가 발생

class CarFormView(FormView):
    template_name = 'inventory/car_basic_form.html'
    form_class = CarForm
    # success_url ='/inventory'

    # # why can't we use reverse?
    # # because then reverse is called when the module is imported, before the urls have been loaded.
    # # class attributes are evaluated on import,
    # # success_url = reverse("inventory:main")
    # # Reverse_lazy is, as the name implies, a lazy implementation of the reverse URL resolver. Unlike the traditional reverse function, reverse_lazy won't execute until the value is needed.
    # # It is useful because it prevent Reverse Not Found exceptions when working with URLs that may not be immediately known.
    # # finally, reverse returns the str vs. reverse_lazy returns the object
    success_url = reverse_lazy("inventory:main")

    def form_valid(self, form):
        form.do_action()
        print(form.cleaned_data)
        return super().form_valid(form)
    

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from inventory.models import Car

class CarCreateView(CreateView):
    model = Car
    fields = ['brand', 'model', 'color', 'year'] # or "__all__"
    success_url = reverse_lazy("inventory:main")
    # template name should be <app>/<model>_form.html
    # e.g. car_form.html

    # optional
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.utils import timezone
    
# class CarListView(LoginRequiredMixin, ListView):
class CarListView(ListView):
    model = Car
    # optional
    paginate_by = 100  # if pagination is desired
    
    # template name should be <app>/<model>_list.html
    # e.g. car_list.html

    # optional
    # context_object_name = "car_list"

    # optional
    queryset = Car.objects.filter(brand__iexact="bmw")

    # optional
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


from django.views.generic.detail import DetailView

class CarDetailView(DetailView):
    model = Car


from django.views.generic.edit import UpdateView
class CarUpdateView(UpdateView):
    model = Car
    # optional
    fields = ['brand', 'model', 'color', 'year']
    success_url = reverse_lazy("inventory:car-list")

    # optional
    template_name_suffix = "_update_form"


from django.views.generic.edit import DeleteView

class CarDeleteView(DeleteView):
    model = Car
    success_url = reverse_lazy('inventory:car-list')

