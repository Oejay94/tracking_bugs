from django.db import models
from datetime import datetime

from bug_tracker_users.models import BugTrackingUser
from projects.models import Project

class Ticket(models.Model):
    #Variable to remove seconds and miliseconds from datetime.now()
    dt = datetime.now().replace(second=0,microsecond=0)

    #Variables for choices
    New = 'New'
    In_Progress = 'In Progress'
    Done = 'Done'
    Invalid = 'Invalid'

    TICKET_STATUS_CHOICES = [
        (New, 'New'),
        (In_Progress, 'In Progress'),
        (Done, 'Done'),
        (Invalid, 'Invalid')
    ]
    title = models.CharField(max_length=40)
    status = models.CharField(max_length=15, choices=TICKET_STATUS_CHOICES, default=New, null=True)
    body = models.TextField()
    date_created = models.DateTimeField(default=dt)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project', blank=True, null=True)
    created_by = models.ForeignKey(BugTrackingUser, on_delete=models.CASCADE, related_name='created_by', blank=True, null=True)
    assigned_to= models.ForeignKey(BugTrackingUser, on_delete=models.CASCADE, related_name='assigned_to', blank=True, null=True)
    completed_by = models.ForeignKey(BugTrackingUser, on_delete=models.CASCADE, related_name='completed_by', blank=True, null=True)

    def __str__(self):
        return self.title