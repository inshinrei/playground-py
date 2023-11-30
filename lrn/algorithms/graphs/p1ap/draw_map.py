import csv
from bokeh.sampledata import us_states
from bokeh.plotting import *

us_states = us_states.data.copy()
del us_states['HI']
del us_states['AK']

state_xs = [us_states[code]['lons'] for code in us_states]
state_ys = [us_states[code]['lats'] for code in us_states]
p = figure(title='the five largest cities in texas', toolbar_location='left', plot_width=1100, plot_height=700)
p.patches(state_xs, state_ys, fill_alpha=0.0, line_color='#884444', line_width=1.5)
x = []
y = []
with open('../data/latlongs-cluster1.csv', 'r') as latlongs_file:
    reader = csv.reader(latlongs_file, delimiter=',')
    for row in reader:
        x.append(float(row[3]))
        y.append(float(row[2]))

p.circle(x, y, size=6, color='navy', alpha=1)
output_file('cluster1.html')
show(p)
