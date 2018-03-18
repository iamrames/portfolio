from django import forms
from  .models import formModel

class MyForm(forms.ModelForm):
	Message = forms.CharField(widget=forms.Textarea)
	class Meta:
		model = formModel
		fields = "__all__"
