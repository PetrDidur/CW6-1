from django import forms
from django.forms import ModelForm

from mailing.models import Mailing


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form_control'


class MailingForm(ModelForm):

    class Meta:
        model = Mailing
        fields = '__all__'





