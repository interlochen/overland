from django.db import models
from django.forms import ModelForm
from django.core.validators import RegexValidator

class Application(models.Model):
	names = models.CharField(max_length=30)
	useremail = models.EmailField(blank=False)
	phone_regex = RegexValidator(regex=r'^\+?\d{9,15}$', message="Phone number must be entered in the format: '+999999999")
	phone = models.CharField(validators=[phone_regex], blank=True, max_length=15)
	year = models.IntegerField(default=2015)
	make = models.CharField(max_length=30)
	model = models.CharField(max_length=30)

class ApplyForm(ModelForm):
	class Meta:
		model = Application
		fields = ['names', 'useremail', 'year', 'make', 'model', 'phone']