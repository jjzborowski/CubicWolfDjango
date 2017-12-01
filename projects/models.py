from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200, blank=False)
    date = models.DateField(blank=False)
    desc = models.TextField(blank=True)
    owner = models.ForeignKey(
        'auth.User',
        related_name='snippets',
        on_delete=models.CASCADE,
        null=True
        )

    def __str__(self):
        return self.title
