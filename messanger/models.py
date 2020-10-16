from django.db import models
from django.contrib.auth.models import User
from django_cryptography.fields import encrypt


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    content = encrypt(models.TextField())
