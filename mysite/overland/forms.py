from django import forms

class Apply(forms.Form):
	names = forms.CharField(max_length=30)
	useremail = forms.EmailField(required=True)
	year = forms.IntegerField(default=4)
	make = forms.CharField(max_length=30)
	model = forms.CharField(max_length=30)