import numpy as np
import random

from bokeh.layouts import column, row
from bokeh.models import Button, ColumnDataSource, Select, TextInput
from bokeh.plotting import figure, curdoc


def roll_die(d=20):
    result = random.randrange(start=1, stop=d+1, step=1)
    #print(f"Rolled a D{d} and got {result}")
    return result

def roll_dice(n=1, d=20, normalize=False):
    for _ in range(n):
        yield roll_die(d=d)

p = figure(width=800, height=800, title="Yo waddup?")
p.xaxis.axis_label = "Sum"
p.yaxis.axis_label = "Prob."

l = p.line(source=ColumnDataSource(data=dict(zip("rp", [[], []]))), x="r", y="p")

def plot_roll_stats():
    n, d = 1, 20  # TODO
    N = 10000
    x = np.array(list(roll_dice(n=N, normalize=True)))
    r, c = np.unique(x, return_counts=True)
    p = c/N
    new_data = dict(zip("rp", [r, p]))
    l.data_source.data = new_data

roll_input = TextInput(value="1d20", title="Roll: ")
roll_button = Button(label="No whammy!", button_type="primary")
roll_button.on_event("button_click", plot_roll_stats)

curdoc().add_root(column(row(roll_input, roll_button), p))

