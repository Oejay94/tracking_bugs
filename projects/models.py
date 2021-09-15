from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()

    def __str__(self):
        return self.title