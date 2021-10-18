from os import stat
import plotly.figure_factory as pff
import statistics
import pandas as pd
import csv
import random
import plotly.graph_objects as pgo

df=pd.read_csv('medium_data.csv')
data=df['claps'].tolist()

pop_mean=statistics.mean(data)
pop_stdev=statistics.stdev(data)
print(" Population Mean = ",pop_mean)

def random_set_mean(counter):
    dataset=[]

    for i in range(0,counter):
        index=random.randint(0,len(data))
        value=data[index]
        dataset.append(value)
    
    mean=statistics.mean(dataset)
    return(mean)

def show_graph(mean_list):
    data=mean_list
    mean=statistics.mean(data)

    graph=pff.create_distplot([data],['Temp'],show_hist=False)
    graph.show()

def setup():
    mean_list=[]

    for i in range (0,100):
        set_of_means=random_set_mean(30)
        mean_list.append(set_of_means)
    
    show_graph(mean_list)
    print("Sampling Mean = ",statistics.mean(mean_list))

setup()