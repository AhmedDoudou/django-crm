from django.db import models
from django import forms
from leads.form import Agent



class AgentModelForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = (
            'user',
        )