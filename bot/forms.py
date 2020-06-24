from django import forms
from .models import Commands

class AddBot(forms.Form):
    name = forms.CharField(max_length=255,required=True,label='Name of your bot')
    tele = forms.CharField(max_length=255,required=True,label="Telegram token")
    bale = forms.CharField(max_length=255,required=True,label="Bale token")


class AddCommand(forms.Form):
    command = forms.CharField(max_length=50,required=True,label='Command name')
    reply = forms.CharField(required=True,label='Reply',widget=forms.Textarea)

    def __init__(self,*args,**kwargs):
        self.botid = kwargs.pop('botid',None)
        super(AddCommand , self).__init__(*args,**kwargs)

    def clean_command(self):
        botid = self.botid
        commands = Commands.objects.filter(bot__id=botid).filter(command=self.cleaned_data.get('command'))
        if commands:
            raise forms.ValidationError('this command already exists!')
        return self.cleaned_data.get('command')


