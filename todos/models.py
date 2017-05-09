from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone

class TodoItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    created = models.DateTimeField(default=timezone.now)
    progress = models.SmallIntegerField(default=0)
    #owner = models.ForeignKey('auth.User')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('todo:detail', kwargs={'pk': self.pk})
