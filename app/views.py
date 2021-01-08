from django.shortcuts import render
from django.http import HttpResponse
from .forms import DataForm
import os

import pickle
import numpy as np 

#Loading the model
CURRENT_DIR = os.path.dirname(__file__)
model_file = os.path.join(CURRENT_DIR, 'automobile-price-prediction-DTRegressor-model.pkl')
regressor = pickle.load(open(model_file, 'rb'))

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
