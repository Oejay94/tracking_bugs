from django.shortcuts import get_object_or_404, redirect, render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views import View

from projects.models import Project

from .models import Team
from .forms import TeamForm

class CreateTeamPage(View):
    def get(self, request):
        html = 'create_team.html'
        form = TeamForm()
        return render(request, html, {'form':form})
    
    def post(self, request):
        form = TeamForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            Team.objects.create(
                team_name=data['team_name'],
                team_bio=data['team_bio'],
                project_Manager=data['project_Manager'],
                product_Owner=data['product_Owner'],
                team_Lead=data['team_Lead'],
                full_Stack_Dev=data['full_Stack_Dev'],
                front_End_Dev=data['front_End_Dev'],
                back_End_Dev=data['back_End_Dev'],
                qA_Lead=data['qA_Lead'],
                qA_Dev=data['qA_Dev'],
                uI_designer=data['uI_designer'],
                uX_Designer=data['uX_Designer']
            )
            return HttpResponseRedirect(reverse('team_page'))


def edit_team_details(request, id):
    html = 'edit_team_details.html'
    team = get_object_or_404(Team, id)

    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            team = form.save(commit=False)
            team.save()
            return redirect('team_page', id=team.id)
    else:
        form = TeamForm(instance=team)
    return render(request, html, {'form':form})


def team_page(request, team_id):
    html = 'team_page.html'
    team = Team.objects.get(id=team_id)
    projects = Project.objects.filter(team=team)
    return render(request, html, {'team':team, 'projects':projects})