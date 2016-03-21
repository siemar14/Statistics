
import numpy as np

#Loads and parses the training and testing dataset files into separate NumPy ndarrays. 
#create four separate arrays:

#2D array of floats for storing testing example attribute values
test_set_att=np.loadtxt('iris-testing-data.csv', delimiter=",", usecols=(0,1,2,3), dtype=float)

#2D array of floats for storing training example attribute values
train_set_att=np.loadtxt('iris-training-data.csv', delimiter=",", usecols=(0,1,2,3), dtype=float)

#1D array of strings for storing training example class labels
train_set_label=np.loadtxt('iris-training-data.csv', delimiter=",", usecols=[4], dtype=str)

#1D array of strings for storing testing example class labels
test_set_label=np.loadtxt('iris-testing-data.csv', delimiter=",", usecols=[4], dtype=str)



"""This function iterates over the range of training examples and 
computing the index of the closest training example by using the
Euclidean Distance.After finding the closest index, the found training example 
are inputted into a new 1D array containing the predicted labels 
for the corresponding index.
"""
def classify(train,test,train_labels):
    predicted_values=[]
    for i in range(len(train)):
        euclideanDist = np.sqrt(np.sum((test[i] - train)**2, axis=1))
        min_dist=np.argmin(euclideanDist)
        predicted_values.append(train_labels[min_dist])
    return predicted_values

"""This function goes through the array of class labels for testing examples 
and compare them to predicted values found in the classify function
It counts how many matches you get. Outputs the number of matches and divides 
by the number of testing examples as a percentage.
Prints the output.
"""

def getAccuracy(test_labels, predictions):
	correct = 0
	print "#, True, Predicted"
	for x in range(len(test_labels)):
	   print x+1,test_labels[x],predictions[x]
	   if test_labels[x]==predictions[x]:
		correct += 1
	acc= correct/float(len(test_labels)) * 100.0
	return acc

##Call the functions and print the accuracy

predicted_values=classify(train_set_att,test_set_att,train_set_label)
acc=getAccuracy(test_set_label,predicted_values)
print "Accuracy:", acc,"%"


