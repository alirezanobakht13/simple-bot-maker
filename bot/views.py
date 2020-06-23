from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def home(request):
    pass

@login_required
def add_bot(request):
    pass

@login_required
def edit_bot(request,bot_id):
    pass

@login_required
def add_command(request,bot_id):
    pass

