from principal_function import *

print("Adult")

generateFileandGraph(database_name="adult_train.csv", column_name="age", main_folder_name="Adult", value_range=[0,125])
generateFileandGraph(database_name="adult_train.csv", column_name="hours-per-week", main_folder_name="Adult", value_range=[0,100])

print("Irish")

generateFileandGraph(database_name="irishn_train.csv", column_name="Age", main_folder_name="Irishn", value_range=[0,125])
generateFileandGraph(database_name="irishn_train.csv", column_name="HighestEducationCompleted", main_folder_name="Irishn", value_range=[1,10])