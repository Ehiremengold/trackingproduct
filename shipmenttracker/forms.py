from django import forms
from .models import YourMessage


class YourMessageForm(forms.Form):

	class Meta:
		model = YourMessage
		fields = ['name', 'email', 'message', 'subject']
