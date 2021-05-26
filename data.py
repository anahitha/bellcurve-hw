from os import stat
import statistics
import pandas as pd
import plotly.express as px
import csv
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go

test = input("Which score do you want (math score, reading score, or writing score)? ")
data = pd.read_csv('exam.csv')
dlist = data[test].tolist()
mean = sum(dlist)/len(dlist)
median = statistics.median(dlist)
mode = statistics.mode(dlist)
stdev = statistics.stdev(dlist)
sd1start, sd1end = mean - stdev, mean + stdev
sd2start, sd2end = mean - (2*stdev), mean + (2*stdev)
sd3start, sd3end = mean - (3*stdev), mean + (3*stdev)
dlist1 = [result for result in dlist if result>sd1start and result<sd1end]
dlist2 = [result for result in dlist if result>sd2start and result<sd2end]
dlist3 = [result for result in dlist if result>sd3start and result<sd3end]
per1 = len(dlist1)/len(dlist)*100
per2 = len(dlist2)/len(dlist)*100
per3 = len(dlist3)/len(dlist)*100
print("Mean is ", mean)
print("Mode is ", mode)
print("Median is ", median)
print(per1, "% is in one standard deviation of the mean")
print(per2, "% is in two standard deviations of the mean")
print(per3, "% is in three standard deviations of the mean")