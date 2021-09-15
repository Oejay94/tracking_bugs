from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views import View

from .models import Ticket
from .forms import TicketForm

class CreateTicketPage(View):
    def get(request):
        html = 'creat_ticket.html'
        form = TicketForm()
        return render(request, html, {'form':form})
    
    def post(request):
        form = TicketForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            Ticket.objects.create(
                title=data['title'],
                body=data['body'],
                created_by=request.user
            )
            return HttpResponseRedirect(reverse('project_page'))


def ticket_detail_page(request, ticket_id):
    html = 'ticket.html'
    ticket = Ticket.objects.get(id=ticket_id)
    return render(request, html, {'ticket':ticket})
