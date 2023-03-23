import dash
from dash.dependencies import Output, Input
from dash import dcc 
from dash import html
#import plotly
import plotly.graph_objs as go
from collections import deque
import pandas as pd
from plotly.subplots import make_subplots
from datetime import datetime



df = pd.read_csv('dex-chart.csv')

#date = df.iloc[0,0].split()[1]
maxLength = 50
xTemp = deque(maxlen = maxLength)
temp = deque(maxlen = maxLength)
XIr1 = deque(maxlen = maxLength)
ir1 = deque(maxlen = maxLength)   #time
ir2 = deque(maxlen = maxLength)   #time
ir3 = deque(maxlen = maxLength)   #time
ir4 = deque(maxlen = maxLength)   #time
ir5 = deque(maxlen = maxLength)   #time
ir6 = deque(maxlen = maxLength)   #time
ir7 = deque(maxlen = maxLength)   #time
ir8 = deque(maxlen = maxLength)   #time
ir9 = deque(maxlen = maxLength)   #time
ir10 = deque(maxlen = maxLength)   #time
rtd1 = deque(maxlen = maxLength)   #time
rtd2 = deque(maxlen = maxLength)   #time
rtd3 = deque(maxlen = maxLength)   #time




app = dash.Dash(__name__)

app.title = "Sensor Monitor"

colors = {
    'background': '#111111',
    'text': '#7FDBFF',
    'header': '#076299',
}

app.layout = html.Div(children = [
    
        # header
        html.Div(
            [
                html.Div(
                    [
                        html.H2("Vantage Thermoforming Sensor Monitor", className="app__header__title"),
                        html.P(
                            "This app monitors thermoforming sensors",
                            className="app__header__title--grey",
                        ),
                    ],
                    className="graph__container",
                ),
            ],
            className="app__header",
        ),
        
        html.Div([
            html.H4(children='Temp'),
    		dcc.Graph(id = 'live-graph', animate = True),
    		dcc.Interval(
    			id = 'graph-update',
    			interval = 5000,
    			n_intervals = 1
    		),
            ],
            className="app__header__desc",
        ),
        html.Div([
            html.H4(children='IR1'),
        		dcc.Graph(id = 'live-graph1', animate = True),
        		dcc.Interval(
        			id = 'graph-update1',
        			interval = 5000,
        			n_intervals = 100
        		),
            ],         
            className="graph__container",
        ),
        
    ]
    
)

@app.callback(
	Output('live-graph', 'figure'),
	[ Input('graph-update', 'n_intervals') ]
)

def update_graph_temp(n):
    #used to set scale
    df2 = df[['J-Type TC 1 (degF)','RTD 1 (degF)','RTD 2 (degF)','RTD 3 (degF)']].copy()
    
    time = df.iloc[n,0].split()[1]
    
    time2 = time.split('.')[0]
    time1 = datetime.strptime(time2, '%H:%M:%S')
    
    h = time1.hour
    m = time1.minute
    s = time1.second
    t = h + m/60 + s/3600
    print(t, df.iloc[n,2],df.iloc[n,15])
    
    xTemp.append(t)
    temp.append(df.iloc[n,2])
    rtd1.append(df.iloc[n,13])
    rtd2.append(df.iloc[n,14])
    rtd3.append(df.iloc[n,15])

    fig = make_subplots()

    trace1 = go.Scatter(x=list(xTemp), y=list(temp),mode='lines+markers',name = 'Temp')
    trace2 = go.Scatter(x=list(xTemp), y=list(rtd1),mode='lines+markers',name = 'RTD1')
    trace3 = go.Scatter(x=list(xTemp), y=list(rtd2),mode='lines+markers',name = 'RTD2')
    trace4 = go.Scatter(x=list(xTemp), y=list(rtd3),mode='lines+markers',name = 'RTD3')

    fig.add_trace(trace1)
    fig.add_trace(trace2)
    fig.add_trace(trace3)
    fig.add_trace(trace4)

    fig.update_layout(xaxis=dict(range=[max(xTemp)-0.01,max(xTemp)+.0001]),
                  yaxis = dict(range = [df2.to_numpy().min()-5,df2.to_numpy().max()+5]))
    
    return fig

@app.callback(
	Output('live-graph1', 'figure'),
	[ Input('graph-update1', 'n_intervals') ]
)
def update_graph_IR1(n):
    
    df2 = df[['IR 1 (F)','IR 2 (F)','IR 3 (F)','IR 4 (F)',
              'IR 5 (F)','IR 6 (F)','IR 7 (F)', 'IR 8 (F)',
              'IR 9 (F)','IR 10 (F)']].copy()
	
    time = df.iloc[n,0].split()[1]
    
    time2 = time.split('.')[0]
    time1 = datetime.strptime(time2, '%H:%M:%S')
    h = time1.hour
    m = time1.minute
    s = time1.second
    t = h + m/60 + s/3600

    XIr1.append(t)
    ir1.append(df.iloc[n,3])
    ir2.append(df.iloc[n,4])
    ir3.append(df.iloc[n,5])
    ir4.append(df.iloc[n,6])
    ir5.append(df.iloc[n,7])
    ir6.append(df.iloc[n,8])
    ir7.append(df.iloc[n,9])
    ir8.append(df.iloc[n,10])
    ir9.append(df.iloc[n,11])
    ir10.append(df.iloc[n,12])
    
    fig = make_subplots()
    
    
    trace1 = go.Scatter(x=list(XIr1), y=list(ir1),mode='lines+markers',name = 'IR1')
    trace2 = go.Scatter(x=list(XIr1), y=list(ir2),mode='lines+markers',name = 'IR2')
    trace3 = go.Scatter(x=list(XIr1), y=list(ir3),mode='lines+markers',name = 'IR3')
    trace4 = go.Scatter(x=list(XIr1), y=list(ir4),mode='lines+markers',name = 'IR4')
    trace5 = go.Scatter(x=list(XIr1), y=list(ir5),mode='lines+markers',name = 'IR5')
    trace6 = go.Scatter(x=list(XIr1), y=list(ir6),mode='lines+markers',name = 'IR6')
    trace7 = go.Scatter(x=list(XIr1), y=list(ir7),mode='lines+markers',name = 'IR7')
    trace8 = go.Scatter(x=list(XIr1), y=list(ir8),mode='lines+markers',name = 'IR8')
    trace9 = go.Scatter(x=list(XIr1), y=list(ir9),mode='lines+markers',name = 'IR9')
    trace10 = go.Scatter(x=list(XIr1), y=list(ir10),mode='lines+markers',name = 'IR10')

    
    fig.add_trace(trace1)
    fig.add_trace(trace2)
    fig.add_trace(trace3)
    fig.add_trace(trace4)
    fig.add_trace(trace5)
    fig.add_trace(trace6)
    fig.add_trace(trace7)
    fig.add_trace(trace8)
    fig.add_trace(trace9)
    fig.add_trace(trace10)

    
    fig.update_layout(
        xaxis = dict(range = [max(XIr1)-.015,max(XIr1)+.0001]),
        yaxis = dict(range = [df2.to_numpy().min()+10,df2.to_numpy().max()+10])
    )
    
    
    return fig



if __name__ == '__main__':
	app.run_server(debug=True)
