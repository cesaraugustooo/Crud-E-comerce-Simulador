from django.views.generic import TemplateView
from django.views.generic.list import ListView
from cadastros.models import produto

# Create your views here.
class Index(TemplateView):
    template_name="index.html"
class Index(ListView):
    model=produto
    template_name="index.html"