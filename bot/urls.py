from django.urls import path
from .views import (
    add_bot,
    add_command,
    home,
    bot_home,
    command_delete
)
from .webhook import api_respond


urlpatterns = [
    path('',home),
    path('addbot/',add_bot),
    path("bothome/<int:botid>/",bot_home),
    path("bothome/<int:botid>/add-command/",add_command),
    path('bothome/<int:botid>/delete-command/<int:comid>/',command_delete),
    path("webhook/<str:app>/<str:token>",api_respond),
]