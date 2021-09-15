from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views import View

from .models import Ticket
from .forms import TicketForm, UpdateTicketForm, CompleteTicketForm

class CreateTicketPage(View):
    def get(self, request):
        html = 'create_ticket.html'
        form = TicketForm()
        return render(request, html, {'form':form})
    
    def post(self, request):
        form = TicketForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            Ticket.objects.create(
                title=data['title'],
                body=data['body'],
                created_by=request.user
            )
            return HttpResponseRedirect(reverse('project_page'))


class UpdateTicketPage(View):
    def get(self, request):
        html = 'update_ticket.html'
        form = UpdateTicketForm()
        return render(request, html, {'form':form})
    
    def post(self, request, ticket_id):
        form = UpdateTicketForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            Ticket.objects.filter(id=ticket_id).update(
                title=data['title'],
                body=data['body'],
                assigned_to=data['assigned_to'],
                status='In Progress'
            )
            return HttpResponseRedirect(reverse('project_page'))


class CompleteTicketPage(View):
    def get(self, request):
        html = 'complete_ticket.html'
        form = CompleteTicketForm()
        return render(request, html, {'form':form})
    
    def post(self, request, ticket_id):
        form = CompleteTicketForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            Ticket.objects.filter(id=ticket_id).update(
                assigned_to=None,
                completed_by=request.user,
                status='Done',
                title=data['title'],
                body=data['body']
            )
            return HttpResponseRedirect(reverse('project_page'))


def ticket_detail_page(request, ticket_id):
    html = 'ticket.html'
    ticket = Ticket.objects.get(id=ticket_id)
    return render(request, html, {'ticket':ticket})
