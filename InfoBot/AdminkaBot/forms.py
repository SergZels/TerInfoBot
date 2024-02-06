from django import forms
from .models import BotDataBase

# class ClientForm (forms.Form):
#     name = forms.CharField(max_length=100)
#     tel = forms.CharField(max_length=100)
#     locationName = forms.CharField(max_length=100)
#     locationAbout = forms.CharField(max_length=100)
#     locationAddres = forms.CharField(max_length=100)
#     mobNumber = forms.CharField(max_length=15)
#     work_schedule = forms.CharField(max_length=100)
#     email = forms.EmailInput()
#     SiteURL =forms.URLInput()
#     facebookURL=forms.URLInput()
#     InstagramURL=forms.URLInput()
#     #photo
#     heshTeg = forms.CharField(max_length=100)

class ClientForm (forms.ModelForm):
    class Meta:
        model = BotDataBase
       # fields = "__all__"
        fields = ['Photo','Name','About','address','tel','work_schedule','email','SiteURL','facebookURL',
                  'InstagramURL','heshTeg']

