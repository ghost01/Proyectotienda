from django import forms
from .models import *
class gustos_form(forms.Form):
	correo = forms.EmailField(widget = forms.TextInput())
	titulo = forms.CharField(widget = forms.TextInput())
	texto = forms.CharField(widget = forms.Textarea())
	tiempo = forms.DateTimeField(widget = forms.TimeInput())
	

class agregar_producto_form(forms.ModelForm):
	class Meta:
		model = Producto
		fields = '__all__'