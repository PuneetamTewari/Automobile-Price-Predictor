import numpy as np 

class Linear_Regression_Model:
	def __inint__(self):
		self.X = X
		self.y = y
		self.theta = theta
		self.alpha = alpha
		self.Num_Iter = Num_Iter
		self.Reg_term = Reg_term
		self.X_val = X_val
		self.y_val = y_val

	def CostFunction(self,X, y, theta):
		number_of_training_examples = len(X)
		hypothesis_func = np.dot(X,np.transpose(theta))
		Cost_function = (sum(np.square(hypothesis_func - y))/(2*number_of_training_examples))
		return Cost_function

	def Normalize_Features(self,X):
		X_norm = X
		s = (X,2)
		Mu = np.zeros(np.shape(s))
		sigma = np.zeros(np.shape(s))

		Mu = np.mean(X)
		sigma = np.std(X)
		X_norm = np.divide((X-Mu),sigma)
		return X_norm

	def GradientDescent(self,X,y,theta,alpha,Num_Iter):
		number_of_training_examples = len(y)
		CostFunc_history = np.zeros(Num_Iter)
		for i in range(Num_Iter):
			Errors = np.dot(X,np.transpose(theta))-y
			theta_update = alpha*(np.dot((np.transpose(X)),Errors))/number_of_training_examples
			theta -= np.transpose(theta_update)
			temp =  self.CostFunction(X, y, theta)
			CostFunc_history[i] = temp[0]
		return theta, CostFunc_history

	def Regularized_Linear_Regression(self,X,y,theta,Reg_term):
		number_of_training_examples = len(y)
		Cost_fn = 0
		Gradient = np.zeros(np.shape(theta))

		Error = (np.dot(X,np.transpose(theta)) - y)
		R = (Reg_term/(2*number_of_training_examples))
		Cost_fn = (np.sum(np.square(Error))*(1/(2*number_of_training_examples))) + (np.sum(np.square(theta[1:])))*R 		
		Gradient = (np.dot(np.transpose(X),Error))/number_of_training_examples		
		Gradient[1:] = Gradient[1:]  + (Reg_term*(theta[1:]))/number_of_training_examples

		return Cost_fn, Gradient

	def predict(self, X, theta):
		predictions= []
		for row in X:
			pred = theta[-1,0]*row[0] + theta[-1,1]*row[1] + theta[-1,2]*row[2] + theta[-1,3]*row[3]
			predictions.append(pred)
		return predictions
		