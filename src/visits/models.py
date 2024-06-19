from django.db import models

class Visit (models.Model):
    path = models.TextField(null=True, blank=True)
    timeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'visit number {self.id}'