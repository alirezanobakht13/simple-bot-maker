from django.contrib import admin

from .models import BotTokens,Commands
# Register your models here.

admin.site.register(BotTokens)
admin.site.register(Commands)