from django.db import models
from django import forms
from leads.form import Agent , User
class AgentModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password'
        )