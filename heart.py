from __future__ import print_function
import sys
from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import VectorAssembler, StandardScaler
from pyspark.ml.linalg import Vectors 
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.sql.functions import isnan, when, count, col

reload(sys) 
sys.setdefaultencoding('utf8')
if __name__ == "__main__":

	spark = SparkSession.builder.appName("heart_disease_lr").getOrCreate()

	data = spark.read.option("header","true").option("inferSchema", "true").csv(sys.argv[1])

	data.show(10)
	oldCount = data.count()
	data.columns 
	data.printSchema() #check datatypes


	str_cols = ['education','cigsPerDay', 'BPMeds', 'totChol', 'BMI', 'heartRate','glucose']

	for column in str_cols:
		data = data.withColumn(column, data[column].cast('double')).dropna()

	newCount = data.count()

	print(oldCount-newCount, "rows are removed due to NA values after tranforming the string columns to double type columns")

	# check null values in data
	print('Check for null values in df')
	data.select([count(when(isnan(c) | col(c).isNull(), c)).alias(c) for c in data.columns]).show()

	#show inbalanced data 
	print('The dataset has an inbalanced distribution of target labels:', data.groupBy('TenYearCHD').count().show())

	feat_cols = ['male', 'age', 'education', 'currentSmoker', 'cigsPerDay', 'BPMeds',\
	'prevalentStroke', 'prevalentHyp', 'diabetes', 'totChol', 'sysBP', 'diaBP', 'BMI', 'heartRate', 'glucose']

	vec_assem = VectorAssembler(inputCols = feat_cols, outputCol = 'features')

	new_data = vec_assem.transform(data)

	scaler = StandardScaler(inputCol = 'features', outputCol='scaledFeat', withStd=True, withMean=True)

	norm_data = scaler.fit(new_data).transform(new_data)

	train, test = norm_data.randomSplit([0.8,0.2])

	lr = LogisticRegression(labelCol='TenYearCHD', featuresCol='scaledFeat',\
	 family="multinomial").fit(train)

	train_acc = lr.summary.accuracy
	print('Train accuracy is', str(train_acc))


	pred= lr.transform(test)
	pred.show(10)

	evaluator = MulticlassClassificationEvaluator(\
		labelCol='TenYearCHD', predictionCol="prediction", metricName="accuracy")
	test_acc = evaluator.evaluate(pred)

	print('Test accuracy is', str(test_acc))


	spark.stop()

