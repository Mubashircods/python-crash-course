import plotly.express as px
from die import Die


"""Creat D6"""
die_1 = Die()
die_2 = Die(10)

# make some rolls and result in list
results = []
for fill_list in range(50_000):
    result = die_1.fill() + die_2.fill()
    results.append(result)

# Chack the frequwency of D6
frequency = []
max_result = die_1.num_die + die_2.num_die
poss_result = range(2, max_result + 1)
for dies in poss_result:
    NOF = results.count(dies)
    frequency.append(NOF)

title = 'Results of  Rolling D6 and D10 at 50,000 times.'
label = {'x': 'Result', 'y': 'Frequency of result'}
fig = px.box(x=poss_result, y=frequency, title=title, labels=label)
fig.update_layout(xaxis_dtick=1)
fig.write_html('die_visuals.html')

