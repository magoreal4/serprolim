from django.db.models.base import Model
from django.views.generic import TemplateView

from main.models import Banner, Cliente, Faq


class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        banners = Banner.objects.all()
        clientes = Cliente.objects.all()
        faqs = Faq.objects.all()
    
        return {'banners': banners, 
        'clientes': clientes, 
        'faqs': faqs
        }