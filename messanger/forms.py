from django import forms

from messanger.models import Message


class NewMsgForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ['sender']
