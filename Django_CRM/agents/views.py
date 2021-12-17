from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Lead , Agent
from agents.models import AgentModelForm

from django.views import generic





class AgentListView(generic.ListView):
    template_name = "Agent/index.html"
    queryset = Agent.objects.all()
    context_object_name = "agents"


class AgentCreateView(generic.CreateView):
    template_name = "Agent/agent_create.html/"
    form_class = AgentModelForm
    def get_success_url(self):
        return reverse("agents:agent")
    