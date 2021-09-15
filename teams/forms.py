from django import forms

from .models import Team

#Form to create a team.
class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'