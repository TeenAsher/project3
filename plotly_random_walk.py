# Using the library Plotly to make a random walk
# TeenAsher

from plotly.graph_objs import Bar, Layout
from plotly import offline
from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

x_values = list(rw.x_values)
y_values = list(rw.y_values)
data = [Bar(x=x_values, y=y_values)]

x_axis_config = {'title': ''}
y_axis_config = {'title': ''}
my_layout = Layout(title='Random walk', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='random_walk.html')
