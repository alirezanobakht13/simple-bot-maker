from django.shortcuts import render,HttpResponseRedirect,Http404,HttpResponse
from django.contrib.auth.decorators import login_required
from .models import BotTokens,Commands
from .forms import AddBot,AddCommand
import telegram
# Create your views here.


@login_required
def home(request):
    user = request.user
    bots = BotTokens.objects.filter(user__id=user.id)
    return render(request,'bot/home.html',{'bots':bots})

@login_required
def add_bot(request):
    user = request.user
    form = AddBot(request.POST or None)
    if form.is_valid():
        bot = BotTokens()
        bot.tele_token = form.cleaned_data.get('tele')
        bot.bale_token = form.cleaned_data.get('bale')
        try:
            tele = telegram.Bot(token=bot.tele_token)
            tele.setWebhook('https://42a38a4d9663.ngrok.io'+'/webhook/telegram/'+str(bot.tele_token))
        except:
            return HttpResponse("<h1>something wrong (probably token is wrong)</h1>")
       
        bot.bot_name = form.cleaned_data.get('name')
        bot.user = user
        bot.save()
        return HttpResponseRedirect("/")
    return render(request,'bot/add-bot.html',{"form":form})


@login_required
def bot_home(request,botid):
    user = request.user
    bot = BotTokens.objects.filter(user__id=user.id).filter(id=botid)
    if not bot:
        raise Http404('sorry no such bot exists')
    bot_commands = Commands.objects.filter(bot__id=botid)
    return render(request,'bot/bot-home.html',{
        'bot':bot[0],
        'bot_commands':bot_commands
    })


@login_required
def add_command(request,botid):
    user = request.user
    bot = BotTokens.objects.filter(id=botid).filter(user__id=user.id)
    if not bot:
        raise Http404('page not found!')
    form = AddCommand(data=request.POST or None,botid=botid)
    if form.is_valid():
        command = form.cleaned_data.get('command')
        reply = form.cleaned_data.get('reply')
        new_com = Commands()
        new_com.command = command
        new_com.reply = reply
        new_com.bot = bot.first()
        new_com.save()
        return HttpResponseRedirect(f'/bothome/{botid}/')
    return render(request,'bot/add-command.html',{'form':form})

@login_required
def command_delete(request,botid,comid):
    user = request.user
    bot = BotTokens.objects.filter(id=botid).filter(user__id=user.id)
    if not bot:
        raise Http404('page not found!')
    command = Commands.objects.filter(id=comid).first()
    command.delete()
    return HttpResponseRedirect(f'/bothome/{botid}/')