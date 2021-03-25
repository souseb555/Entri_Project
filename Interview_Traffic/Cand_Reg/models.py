from django.conf import settings
from django.db import models
from django.utils import timezone


class UserModel(models.Model):
    INTERVIEWER = 'IN'
    CANDIDATE = 'CA'
    Choices = [
        (INTERVIEWER, 'Interviewer'),
        (CANDIDATE, 'Candidate'),
    ]
    registration_type= models.CharField(
        max_length=2,
        choices=Choices,
        default=INTERVIEWER,
    )
    name = models.CharField(max_length=200)
    email_id = models.CharField(max_length=200)
    available_start_date = models.DateTimeField(default=timezone.now)
    available_end_date = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.name

   



