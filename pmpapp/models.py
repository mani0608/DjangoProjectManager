from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    profile_picture = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.user.username


class ProjectInfo(models.Model):
    name = models.TextField(max_length=250, blank=False)
    duration = models.IntegerField(blank=False, default=0)
    start_date = models.DateField('Project Start Date')
    project_model = models.TextField(blank=False, max_length=50)
    current_resource_count = models.IntegerField(blank=False, default=0)

    def __str__(self):
        return self.name
