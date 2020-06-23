from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here.

class BotTokens(models.Model):
    bot_name = models.CharField(max_length=255)
    tele_token = models.CharField(max_length=255)
    bale_toket = models.CharField(max_length=255)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.bot_name)

class Commands(models.Model):
    command = models.CharField(max_length=255)
    reply = models.TextField()
    bot = models.ForeignKey(BotTokens,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.command)