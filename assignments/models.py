from django.db import models

class Assignment(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    document = models.FileField(upload_to='assignments/')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
