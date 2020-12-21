# Spark_Logistics_Regression


Heart Disease Prediction using Logistic Regression

Logistic regression is a type of regression analysis in statistics used for prediction of outcome of a categorical dependent variable from a set of predictor or independent variables. In logistic regression the dependent variable is always binary. Logistic regression is mainly used to for prediction and also calculating the probability of success.
In this part, Logistic Regression is used to pinpoint the most relevant/risk factors of heart disease as well as predict the overall risk. We use the Framingham Heart dataset (https://www.kaggle.com/amanajmera1/framingham-heart-study-dataset) for the study. 


INSTRUCTIONS: 
NOTE: these files were orignally run on a Google Cloud Compute cluster(3 nodes) with Hadoop and Spark installed. 

- create a fold within your Spark environment 

- put the data file: 'framingham.csv', python file: 'heart.py', and shell script: 'test.sh' inside the folder. 

- run 'test.sh' with ./test.sh

*****************************************************************************************************
Alternatively: 

- 'heart.py'can also be run on a Spark shell by specifying the data file path in place of 'sys.argv[1]'on line 17. 

