from django.db import models

# Create your models here.


class userinfo(models.Model):
    name = models.CharField(max_length=256, null=True)
    user_code = models.CharField(max_length=256, null=True)
    phone_number = models.CharField(max_length=256, null=True)
    location = models.CharField(max_length=128, null=False)
    education = models.CharField(max_length=256, null=True)

    def __str__(self):
        return self.name
