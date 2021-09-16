from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.views import View

from bug_tracker_users.models import BugTrackingUser

from .forms import CreateAccountForm, LoginForm

class CreateAccountPage(View):
    def get(self, request):
        html = 'auth/create_account_page.html'
        form = CreateAccountForm()
        return render(request, html, {'form':form})
    
    def post(self, request):
        form = CreateAccountForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            new_user = BugTrackingUser.objects.create_user(
                username=data['username'],
                password=data['password1'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                role=data['role']
            )
            login(request, new_user)
            return HttpResponseRedirect(reverse('team_page'))
    

class LoginPage(View):
    def get(self, request):
        html = 'auth/login.html'
        form = LoginForm()
        return render(request, html, {'form':form})
    
    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('team_page'))


def logout_button(request):
    logout(request)
    return HttpResponseRedirect(request.GET.get('next', '/'))

def first_page(request):
    html = 'index.html'
    return render(request, html)