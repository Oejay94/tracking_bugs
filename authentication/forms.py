from django import forms
from django.contrib.auth.forms import UserCreationForm

from bug_tracker_users.models import BugTrackingUser

class CreateAccountForm(UserCreationForm):
    class Meta:
        model = BugTrackingUser
        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
            'role'
        ]
    def __init__(self, *args, **kwargs):
        super(CreateAccountForm, self).__init__(*args, **kwargs)

        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = None

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
