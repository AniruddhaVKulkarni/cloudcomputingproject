## Programming Assignment 2

### 		Name: Aniruddha Kulkarni
###		SID: 31488800
###		UCID: avk37

##	Import Python Libraries

from pyspark import SparkContext
from pyspark import SQLContext
from pyspark.ml import Pipeline
from pyspark.ml.feature import Imputer
from pyspark.ml.feature import StandardScaler
from pyspark.ml.feature import StringIndexer
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.feature import VectorIndexer
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.mllib.evaluation import MulticlassMetrics
from pyspark.mllib.util import MLUtils
from pyspark.sql import DataFrame
from pyspark.sql import SparkSession
from pyspark.sql.functions import when


##	Spark Session Creation
Session_Spark = SparkSession.builder.master("local").appName("ProgrammingAssignment2").config("spark.some.config.option","some-value").getOrCreate()

##	Dataset Interpretation
Data_Raw = Session_Spark.read.csv('TrainingDataset.csv',header='true', inferSchema='true', sep=';')
Data_Value = Session_Spark.read.csv('ValidationDataset.csv',header='true', inferSchema='true', sep=';')

##	Feature Column Creation
ColumnsFeature = [c for c in Data_Raw.columns if c != 'quality']
Builder = VectorAssembler(inputCols=ColumnsFeature, outputCol="features")
Transform_Input = Builder.transform(Data_Raw)
Transform_Input.cache()

##	Validation Dataset Conversion
ValidateFeature = [c for c in Data_Value.columns if c != 'quality']
ValidateBuilder = VectorAssembler(inputCols=ValidateFeature, outputCol="features")
ValueTransformed = ValidateBuilder.transform(Data_Value)

##	Random Forest Model Creation
RandomDecisionForest = RandomForestClassifier(labelCol="quality", featuresCol="features", numTrees=10)
RandomModelCreation = RandomDecisionForest.fit(Transform_Input)

##	Assessment
Assess = RandomModelCreation.transform(ValueTransformed)

##	Assess F1 Score
Critic1 = MulticlassClassificationEvaluator(
    labelCol="quality", predictionCol="prediction", metricName="f1")
Efficiency = Critic1.evaluate(Assess)
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print(" F1 Score \n")
print("Test Error = %g" % (1.0 - Efficiency))

DataTransformed = RandomModelCreation.transform(ValueTransformed)
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print(Critic1.getMetricName(), 'Accuracy :', Critic1.evaluate(DataTransformed))
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("~~~~~~~~~~~~~~~~<<EOF>>~~~~~~~~~~~~~~~~\n\n")


