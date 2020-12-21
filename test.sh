#!/bin/bash
#!/bin/bash
echo "Running Heart Disease Prediction "
PROJECT_NAME="heart_disease_lr"
IN_HADOOP_INPUT_PATH="/${PROJECT_NAME}/input/"
OUT_HADOOP_OUTPUT_PATH="/${PROJECT_NAME}/output/"
DATA_FILE_PATH="../../test-data/framingham.csv"
Q2="./heart.py"


source ../../env.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r $IN_HADOOP_INPUT_PATH
/usr/local/hadoop/bin/hdfs dfs -mkdir -p $IN_HADOOP_INPUT_PATH
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal $DATA_FILE_PATH $IN_HADOOP_INPUT_PATH
/usr/local/spark/bin/spark-submit --master=spark://$SPARK_MASTER:7077 $Q2 hdfs://$SPARK_MASTER:9000$IN_HADOOP_INPUT_PATH

