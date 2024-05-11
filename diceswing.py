import numpy as np
import pandas as pd
from scipy.special import binom

import random

from bokeh.layouts import column, row
from bokeh.models import Button, ColumnDataSource, Legend, Select, TextInput
from bokeh.palettes import Colorblind
from bokeh.plotting import figure, curdoc, show


def prob(s, n, d):
    # https://math.stackexchange.com/questions/2290090/probability-that-the-sum-of-k-dice-is-n
    return sum(
        (-1)**k * binom(n, k) * binom(s - k*d - 1, n-1)
        for k in range((s-n)//d+1)
    )/d**n

p = figure(width=800, height=800, title="Yo waddup?")
p.xaxis.axis_label = "Sum"
p.yaxis.axis_label = "Prob."


legend = dict()

for c, (n, d) in zip(Colorblind[8], (
    (20,  3),
    (10,  6),
    ( 6, 10),
    ( 3, 20),
)):
    source = ColumnDataSource(data=pd.DataFrame([
        [_r, prob(_r, n, d)] for _r in range(1, n*d+1)
    ], columns=["r", "p"]))
    l = p.line(source=source, x="r", y="p", color=c)
    m = p.scatter(source=source, x="r", y="p", color=c)
    legend[f"{n}d{d}"] = [l, m]

p.add_layout(Legend(items=[(k, v) for k, v in legend.items()], location=(5, 30)))

show(p)

