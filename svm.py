from sklearn import svm
from sklearn import metrics
import csv

#load and read cvs file
file = open("training1.csv", "r")
training1 = list(csv.reader(file, delimiter=","))
file.close()
file = open("training2.csv", "r")
training2 = list(csv.reader(file, delimiter=","))
file.close()
file = open("testing1.csv", "r")
testing1 = list(csv.reader(file, delimiter=","))
file.close()
file = open("testing2.csv", "r")
testing2 = list(csv.reader(file, delimiter=","))
file.close()

#Create svm Classifier
clf1 = svm.SVC(kernel='linear') # Linear Kernel for dataset1
clf2 = svm.SVC(kernel='linear') # Polynomial Kernel for dataset2


#Train the model using the training sets
clf1.fit(training1)
clf2.fit(training2)


#Predict the response for test dataset
pred1 = clf1.predict(testing1)
pred2 = clf2.predict(testing2)

#Model accuracy
print("Accuracy:",metrics.accuracy_score(tesing1, pred1))
print("Accuracy:",metrics.accuracy_score(tesing2, pred2))
