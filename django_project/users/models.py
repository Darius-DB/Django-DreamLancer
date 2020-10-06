from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    first_name = models.CharField(max_length=200, default='None')
    last_name = models.CharField(max_length=200, default='None')
    description = models.TextField(default='None')
    domain = models.CharField(max_length=200, default='None')
    years_of_experience = models.IntegerField(default=0)
    abilities_1 = models.CharField(max_length=200, default='None')
    abilities_2 = models.CharField(max_length=200, default='None')
    abilities_3 = models.CharField(max_length=200, default='None')
    abilities_4 = models.CharField(max_length=200, default='None')
    github_info = models.URLField(default='None')
    linkedin_info = models.URLField(default='None')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
