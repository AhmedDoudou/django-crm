from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from agents.forms import AgentModelForm

from django.views import generic





class AgentListView(generic.ListView):
    template_name = "Agent/index.html"
    context_object_name = "agents"
    def get_queryset(self):
        request_organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=request_organisation)


    


class AgentCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "Agent/agent_create.html/"
    form_class = AgentModelForm
    def get_success_url(self):
        return reverse("agents:agent")
    
    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organisation =self.request.user.userprofile
        agent.save()
        return super(AgentCreateView, self).form_valid(form)


class AgentDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "Agent/agent_detail.html/"
    context_object_name = "agent"
    def get_queryset(self):
        request_organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=request_organisation)




class AgentUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "Agent/agent_update.html/"
    form_class = AgentModelForm
    def get_queryset(self):
        request_organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=request_organisation)
    def get_success_url(self):
        return reverse("agents:agent")

class AgentDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "Agent/delete_agent.html/"
    def get_queryset(self):
        request_organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=request_organisation)
    def get_success_url(self):
        return reverse("agents:agent")

