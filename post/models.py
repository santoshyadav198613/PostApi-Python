from django.db import models


# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    body = models.CharField(max_length=200, blank=False, null=False)

    class Meta:
        pass
