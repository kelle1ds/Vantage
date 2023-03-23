import dash
from dash import dcc
from dash import html
from dash.dependencies import Output, Input

from pandas_datareader.data import DataReader
import time
from collections import deque
import plotly.graph_objs as go
import random
import pandas as pd

app = dash.Dash('vehicle-data')

max_length = 50
times = deque(maxlen=max_length)
temps = deque(maxlen=max_length)
ir1 = deque(maxlen=max_length)
ir2 = deque(maxlen=max_length)




data_dict = {"Temperature":temps,
             "IR1": ir1,
             "IR1": ir1,
             }

df = pd.read_csv('dex-chart.csv')


def update_obd_values(times, temp, ir1, ir2):

    times.append(time.time())
    if len(times) == 1:
        #starting relevant values
        temp.append(df[0,2])
        ir1.append(df[0,3])
        ir2.append(df[0,4])
    else:
        for data_of_interest in [temps, ir1, ir2]:
            data_of_interest.append(data_of_interest[-1]+data_of_interest[-1]*random.uniform(-0.0001,0.0001))

    return times, oil_temps, intake_temps, coolant_temps, rpms, speeds, throttle_pos

times, oil_temps, intake_temps, coolant_temps, rpms, speeds, throttle_pos = update_obd_values(times, oil_temps, intake_temps, coolant_temps, rpms, speeds, throttle_pos)

app.layout = html.Div([
    html.Div([
        html.H2('Vehicle Data',
                style={'float': 'left',
                       }),
        ]),
    dcc.Dropdown(id='vehicle-data-name',
                 options=[{'label': s, 'value': s}
                          for s in data_dict.keys()],
                 value=['Coolant Temperature','Oil Temperature','Intake Temperature'],
                 multi=True
                 ),
    html.Div(children=html.Div(id='graphs'), className='row'),
    dcc.Interval(
        id='graph-update',
        interval=100),
    ], className="container",style={'width':'98%','margin-left':10,'margin-right':10,'max-width':50000})


@app.callback(
    Output('graphs','children'),
    [Input('vehicle-data-name', 'value'), 
    Input('graph-update', 'n_intervals')]
)

def update_graph(data_names,intervals):
    graphs = []
    update_obd_values(times, oil_temps, intake_temps, coolant_temps, rpms, speeds, throttle_pos)
    if len(data_names)>2:
        class_choice = 'col s12 m6 l4'
    elif len(data_names) == 2:
        class_choice = 'col s12 m6 l6'
    else:
        class_choice = 'col s12'


    for data_name in data_names:

        data = go.Scatter(
            x=list(times),
            y=list(data_dict[data_name]),
            name='Scatter',
            fill="tozeroy",
            fillcolor="#6897bb"
            )

        graphs.append(html.Div(dcc.Graph(
            id=data_name,
            animate=True,
            figure={'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(times),max(times)]),
                                                        yaxis=dict(range=[min(data_dict[data_name]),max(data_dict[data_name])]),
                                                        margin={'l':50,'r':1,'t':45,'b':1},
                                                        title='{}'.format(data_name))}
            ), className=class_choice))

    return graphs



external_css = ["https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css"]
for css in external_css:
    app.css.append_css({"external_url": css})

external_js = ['https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js']
for js in external_css:
    app.scripts.append_script({'external_url': js})


if __name__ == '__main__':
    app.run_server(debug=True)