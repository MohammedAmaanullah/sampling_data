import pandas as pd
import statistics
import random 
import csv
import plotly.figure_factory as ff

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
fig=ff.create_distplot([data],['reading_time'],show_hist=False)
fig.show()
dataset=[]
for i in range(0,100):
  random_index = random.randint(0,len(data))
  value= data[random_index]
  dataset.append(value)
mean = statistics.mean(dataset)
stdev = statistics.stdev(dataset)
print(mean,stdev)
def RandomSetOfMean(counter):
  dataset=[]
  for i in range(0,counter):
    random_index = random.randint(0,len(data))
    value= data[random_index]
    dataset.append(value)
  mean = statistics.mean(dataset)
  stdev = statistics.stdev(dataset)
  print(mean,stdev)
  return mean
def ThousandCounter():
  mean_list=[]
  for i in range(0,1000):
    setofmeans = RandomSetOfMean(100)
    mean_list.append(setofmeans)
  stdev=statistics.stdev(mean_list)
  print(stdev)  
ThousandCounter()  