from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class DataForm(forms.Form):

	year = forms.CharField(label= 'Year of purchase', widget=forms.NumberInput(attrs={'placeholder': '(e.g. 2020)'}))
	purchase_price = forms.FloatField(label='Purchase price (Lakhs)', widget=forms.NumberInput(attrs={'placeholder': '(e.g. 5.77)'}))
	kms_driven = forms.CharField(label='Total distance driven (KM)', widget=forms.NumberInput(attrs={'placeholder': '(e.g. 2071)'}))
