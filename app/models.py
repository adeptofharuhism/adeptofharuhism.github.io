from django.db import models
#после создания модели нужно будет мигрировать
class NewUser(models.Model):
    username = models.TextField(max_length=50)
    password = models.TextField(max_length=50)
    email = models.TextField(blank=True,default='')
    first_name = models.TextField(max_length=50,blank=True,default='')
    last_name = models.TextField(max_length=50,blank=True,default='')

    def __str__(self):
        return self.username

class AuthUser(models.Model):
    username = models.TextField(max_length=50)
    password = models.TextField(max_length=50)

    def __str__(self):
        return self.username