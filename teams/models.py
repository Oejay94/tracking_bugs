from django.db import models

from bug_tracker_users.models import BugTrackingUser

class Team(models.Model):
    #give the team an awesome name!
    team_name = models.CharField(max_length=70)

    #describe the team!
    team_bio = models.TextField(blank=True, null=True)

    #Roles in team
    project_manager = models.ForeignKey(BugTrackingUser, on_delete=models.CASCADE, related_name='project_manager', blank=True, null=True)
    product_owner = models.ForeignKey(BugTrackingUser, on_delete=models.CASCADE, related_name='product_owner', blank=True, null=True)
    team_lead = models.ForeignKey(BugTrackingUser, on_delete=models.CASCADE, related_name='team_lead', blank=True, null=True)
    full_stack_dev = models.ForeignKey(BugTrackingUser, on_delete=models.CASCADE, related_name='full_stack_dev', blank=True, null=True)
    front_end_dev = models.ForeignKey(BugTrackingUser, on_delete=models.CASCADE, related_name='front_end_dev', blank=True, null=True)
    back_end_dev = models.ForeignKey(BugTrackingUser, on_delete=models.CASCADE, related_name='back_end_dev', blank=True, null=True)
    qa_lead = models.ForeignKey(BugTrackingUser, on_delete=models.CASCADE, related_name='qa_lead', blank=True, null=True)
    qa_dev = models.ForeignKey(BugTrackingUser, on_delete=models.CASCADE, related_name='qa_dev', blank=True, null=True)
    ui_designer = models.ForeignKey(BugTrackingUser, on_delete=models.CASCADE, related_name='ui_designer', blank=True, null=True)
    ux_designer = models.ForeignKey(BugTrackingUser, on_delete=models.CASCADE, related_name='ux_designer', blank=True, null=True)

    def __str__(self):
        return self.team_name