from __future__ import division, print_function
import numpy as np
import pandas as pd
import pygal

data = pd.read_csv('2016-first-quarter-citations.csv')
data = data.dropna(how='any')
listx = data.groupby('Cited Person Age').size()
listy = listx.keys()
listz = listy+1
list = zip(listx,listy,listz)
hist = pygal.Histogram()
hist.add('#Citations-Age',list)
hist.render_to_file('AgeHist.svg')

