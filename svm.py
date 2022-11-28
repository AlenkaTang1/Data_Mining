from sklearn import svm
from sklearn import metrics


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
