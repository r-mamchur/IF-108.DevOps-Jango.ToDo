from django import forms

from .models import ToDo, CFG_States

class TodoForm(forms.ModelForm):
#     state = CFG_States.objects.first()
#    details = forms.CharField(
#        max_length=4000,
#        help_text='The max length of the text is 4000.')

    class Meta:
        model = ToDo
        fields = ['title', 'due', 'state', 'details']