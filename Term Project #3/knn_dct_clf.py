import pandas as pd  
from pandas import DataFrame as df  
import numpy as np  
import matplotlib.pyplot as plot  
from sklearn.neighbors import KNeighborsClassifier  
from sklearn.model_selection import KFold  
from sklearn import metrics  
from sklearn.metrics import accuracy_score  
from sklearn import tree  
from sklearn.preprocessing import LabelEncoder  
  
def readDataset():  
    global df  
    df = pd.read_csv("LiverPatient.csv")  
    #print(df.head())  
  
def allocateValues():  
    enc = LabelEncoder()  
    enc.fit(df['gender'])  
    df['gender'] = enc.transform(df['gender'])  
    # X = df[['age','gender','TB','DB','alkphos','sgpt','sgot','TP','ALB','A_G']]  
    # Y = df['class']  
    global X  
    global Y  
    X = df.iloc[:, [0,9]].values  
    Y = df.iloc[:, 10].values  
  
def crossValidation(classifier):  
    global acc  
    global mae  
    global mse  
    global rmse  
      
    acc = np.array([ ])  
    mae = 0  
    mse = 0  
    rmse = 0  
      
    ns = 10  
    crossValidation = KFold(n_splits=ns)  
      
      
    for train_index, test_index in crossValidation.split(X):  
        X_train, X_test = X[train_index], X[test_index]  
        Y_train, Y_test = Y[train_index], Y[test_index]  
        classifier.fit(X_train,Y_train)  
        prediction = classifier.predict(X_test)  
        acc = np.append(acc, [accuracy_score(Y_test, prediction)], axis = 0)  
      
        mae = mae + metrics.mean_absolute_error(Y_test, prediction)  
        mse  = mse + metrics.mean_squared_error(Y_test, prediction)  
        rmse = rmse + np.sqrt(metrics.mean_squared_error(Y_test, prediction))  
  
       
    acc = np.mean(acc)  
    mae = mae/ns  
    mse = mse/ns  
    rmse = rmse/ns  
      
    print('Accuracy',acc)  
    print('Mean Absolute Error: ',mae)  
    print('Mean Squared Error',mse)  
    print('Root Mean Squared Error',rmse)  
    print('\n')  
  
def testClassifiers():  
    knn = KNeighborsClassifier(n_neighbors=20)   
    dct = tree.DecisionTreeClassifier()  
    print('For KNN : ')  
    crossValidation(knn)  
      
    global k_acc  
    global k_mae  
    global k_mse  
    global k_rmse  
      
    global d_acc  
    global d_mae  
    global d_mse  
    global d_rmse  
      
    k_acc = acc  
    k_mae = mae  
    k_mse = mse  
    k_rmse = rmse  
      
    print('For Decision Tree : ')  
    crossValidation(dct)  
      
    d_acc = acc  
    d_mae = mae  
    d_mse = mse  
    d_rmse = rmse  
  
def illustrateResult():  
    n_groups = 4  
    knn_bar = (k_acc*100, k_mae*100, k_mse*100, k_rmse*100)  
    dct_bar = (d_acc*100, d_mae*100, d_mse*100, d_rmse*100)  
  
# create plot  
    fig, ax = plot.subplots()  
    index = np.arange(n_groups)  
    bar_width = 0.35  
    opacity = 0.8  
  
    rects1 = plot.bar(index, knn_bar, bar_width,  
    alpha=opacity,  
    color='b',  
    label='KNN')  
  
    rects2 = plot.bar(index + bar_width, dct_bar, bar_width,  
    alpha=opacity,  
    color='g',  
    label='Decision Tree')  
  
    plot.xlabel('Classifiers')  
    plot.ylabel('')  
    plot.title('KNN vs Decision Tree')  
    plot.xticks(index + bar_width, ('Accuracy', 'MAE', 'MSE', 'RMSE'))  
    plot.legend()  
  
    plot.tight_layout()  
    plot.show()  
  
#Main  
readDataset()  
allocateValues()  
testClassifiers()  
illustrateResult()  