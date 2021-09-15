from django.db import models
from django.contrib.auth.models import AbstractUser

class BugTrackingUser(AbstractUser):
    #Variables for choices
    PROJECT_MANAGER = 'P.M.'
    PRODUCT_OWNER = 'P.O.'
    TEAM_LEAD = 'T.L.'
    FULL_STACK_DEV = 'F.S.D.'
    FRONT_END_DEV = 'F.E.D.'
    BACK_END_DEV = 'B.E.D.'
    QA_LEAD = 'Q.A.L.'
    QA_DEV = 'Q.A.D.'
    UI_DESIGNER = 'U.I.D.'
    UX_DESIGNER = 'U.X.D.'

    TEAM_ROLE_CHOICES = [
        (PROJECT_MANAGER, 'Project Manager'),
        (PRODUCT_OWNER, 'Product Owner'),
        (TEAM_LEAD, 'Team Lead'),
        (FULL_STACK_DEV, 'Full-Stack Dev'),
        (FRONT_END_DEV, 'Front-End Dev'),
        (BACK_END_DEV, 'Back-End Dev'),
        (QA_LEAD, 'QA Lead'),
        (QA_DEV, 'QA Dev'),
        (UI_DESIGNER, 'UI Designer'),
        (UX_DESIGNER, 'UX Designer')
    ]

    role = models.CharField(max_length=6, choices=TEAM_ROLE_CHOICES)
    
    def __str__(self):
        return self.username