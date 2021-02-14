from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    body_text = models.TextField()
    date = models.DateField()

    def __str__(self):  # return the default names
        return self.title

