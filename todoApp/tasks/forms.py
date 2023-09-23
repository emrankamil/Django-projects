from .models import Task
from django import forms

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'complete'] # '__all__' allow all fields