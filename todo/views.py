from django.views.generic.base import TemplateView
from .models import Task

# Create your views here.


class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = Task.objects.all()
        return context
