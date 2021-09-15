from django.shortcuts import get_object_or_404, render, reverse, HttpResponseRedirect, redirect
from django.views import View

from .models import Project
from .forms import ProjectForm

from tickets.models import Ticket


class ProjectFormPage(View):
    def get(self, request):
        html = 'create_projects.html'
        form = ProjectForm()
        return render(request, html, {'form':form})
    
    def post(self, request):
        form = ProjectForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            Project.objects.create(
                title=data['title'],
                description=data['description']
            )
            return HttpResponseRedirect(reverse('team_page'))


def edit_project_details(request, id):
    html = 'edit_project_details.html'
    project = get_object_or_404(Project, id)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            return redirect('project_page', id=project.id)
    else:
        form = ProjectForm(instance=project)
    return render(request, html, {'form':form})

def project_page(request, project_id):
    html = 'project_page.html'
    project = Project.objects.get(id=project_id)
    tickets = Ticket.objects.filter(project=project)
    return render(request, html, {'project':project, 'tickets':tickets})

