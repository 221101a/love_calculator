from django.db import models

# Create your models here.
class User(models.Model):
    user_name=models.CharField(max_length=20,null=False)
    user_love=models.CharField(max_length=20,null=False)
    def __str__(self):
        return self.user_name
