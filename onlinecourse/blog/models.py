from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()

    # image =
    # author =

    def __str__(self):
        return self.title
