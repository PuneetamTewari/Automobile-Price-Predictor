from django.shortcuts import render
from django.http import HttpResponse
from .forms import DataForm

import pickle
import numpy as np 

#Loading the model
filename = 'C:\\Users\\Paresham Tewari\\Desktop\\price_predictor\\app\\automobile-price-prediction-DTRegressor-model.pkl'
regressor = pickle.load(open(filename, 'rb'))

def data(request):

	if request.method == 'POST':
		form = DataForm(request.POST)
		if form.is_valid():

			year = form.cleaned_data['year']
			purchase_price = form.cleaned_data['purchase_price']
			kms_driven = form.cleaned_data['kms_driven']

			info = np.array([[year,purchase_price,kms_driven]])
			prediction = regressor.predict(info)

			context = {'prediction': prediction}

			return render(request, 'result.html', context)
	else:
		form = DataForm()
	return render(request, 'form.html', {'form': form})
