from django.http import JsonResponse
import telegram
import json
from .models import BotTokens,Commands
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def api_respond(request,app,token):
    bot = None
    bot_db = None
    if app == 'telegram':
        bot = telegram.Bot(token=token)
        bot_db = BotTokens.objects.filter(tele_token=token)
        if not bot_db:
            return JsonResponse({'sucess':False})
    elif app == 'bale':
        bot = telegram.Bot(token=token,base_url="https://tapi.bale.ai/")
        bot_db = BotTokens.objects.filter(bale_token=token)
        if not bot_db:
            return JsonResponse({'sucess':False})
    bot_db = bot_db.first()
    commands = Commands.objects.filter(bot__id=bot_db.id)
    update = telegram.Update.de_json(json.loads(request.body),bot)

    chat_id = update.message.chat.id
    text = update.message.text.encode('utf-8').decode()

    reply = commands.filter(command=text)
    if not reply:
        bot.send_message(chat_id=chat_id,text="command not found")
    else:
        reply=reply.first().reply
        bot.send_message(chat_id=chat_id,text=reply)
    
    return JsonResponse({'sucess':True})

