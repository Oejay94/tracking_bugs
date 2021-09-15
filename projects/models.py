from django.db import models

from teams.models import Team

class Project(models.Model):
    #name of project
    title = models.CharField(max_length=40)

    #describe the project. It's MVP, it's scretch goals, ect
    description = models.TextField()

    #assign a team of users to this project
    team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True)

    #add tickets to project
    tickets = models.ForeignKey('tickets.Ticket', related_name='tickets', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title