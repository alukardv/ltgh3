from django import forms

from app1.models import VeteransAssistant, Region, TypeOfUser, UserTG


class UsersTGForm(forms.Form):
    full_name = forms.CharField(max_length=255, required=False)
    phone_number = forms.CharField(max_length=255, required=False)
    date_of_birth = forms.DateField(required=False)
    region = forms.ModelChoiceField(queryset=Region.objects.all(), required=False)
    type_of_user = forms.ModelChoiceField(queryset=TypeOfUser.objects.all(), required=False)
    time_create = forms.DateTimeField(required=False, widget=forms.TextInput(attrs={'type': 'datetime-local'}))


class QuestionForm(forms.Form):
    veterans_assistant = forms.ModelChoiceField(queryset=VeteransAssistant.objects.all(), required=False)
    user_gt = forms.CharField(max_length=255, required=False)
    text_question = forms.CharField(max_length=255, required=False)
    time_create = forms.DateTimeField(required=False, widget=forms.TextInput(attrs={'type': 'datetime-local'}))

