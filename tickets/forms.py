from django import forms

from .models import Ticket

from bug_tracker_users.models import BugTrackingUser

#Form to create a new ticket. It inherets the specified fields from the Ticket Model
class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'title',
            'body'
        ]

#Form to update a ticket and assign a user to it
class UpdateTicketForm(forms.Form):
    title = forms.CharField(max_length=40)
    body = forms.CharField(widget=forms.Textarea())
    assigned_to = forms.ModelChoiceField(queryset=BugTrackingUser.objects.all())

#Form to 'complete' a ticket and assign a user to the completed field
class CompleteTicketForm(forms.Form):
    title = forms.CharField(max_length=40)
    body = forms.CharField(widget=forms.Textarea())
    completed_by = forms.ModelChoiceField(queryset=BugTrackingUser.objects.all())