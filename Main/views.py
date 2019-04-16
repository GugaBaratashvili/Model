
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

class SimulationPage(TemplateView):
    template_name = 'simulation.html'
