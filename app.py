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
import dash_daq as daq



df = pd.read_csv('dex-chart.csv')

#date = df.iloc[0,0].split()[1]
maxLength = 100
xTemp = deque(maxlen = maxLength)
temp = deque(maxlen = maxLength)
temp2 = deque(maxlen = maxLength)
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

theme = {
    'dark': True,
    'detail': '#007439',
    'primary': '#00EA64',
    'secondary': '#6E6E6E',
}

gaugeSize = 150

app.layout = html.Div([
    
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
        
        #######################
        #Start of First Chart with temp ant RTD1
        html.Div([
            html.H5('Temperature for Gaugae and RTD'),
    		dcc.Graph(id = 'live-graph', animate = True),
    		dcc.Interval(
    			id = 'graph-update',
    			interval = 5000,
    			n_intervals = 1
    		),
            dcc.Slider(
                id='my-graph-slider-1',min=0,max=10,value=5
            ),
            ],
            className="graph__container",
        ),
        
        ## Temp Gauges#####################
        html.Table(
            html.Tr(
                [
                #Temp Gauge ######################
                html.Td(
                        [
                        
                        daq.Gauge(
                            id='my-gauge-1',
                            #label='Temp.',
                            color={"gradient":False,"ranges":{"green":[96,100],"yellow":[100,105],"red":[105,110]}},
                            label = {"label":'Temperature',"style":{"color":"black","font-size":"30px"}},
                            labelPosition='top',
                            showCurrentValue=True,
                            units='degF',
                            size=gaugeSize,
                            scale={'start': 95, 'interval': 1, 'labelInterval': 1},
                            max=110,min=96,value=98
                            ),
                        dcc.Interval(
                    		id = 'gauge-update1',
                    		interval = 5000,
                    		n_intervals = 1
                            ),
                    ]
                        ),
                
                #RTD1 Gauge ######################
                html.Td(
                        [
                            daq.Gauge(
                                id='my-gauge-RTD1',
                                color={"gradient":False,"ranges":{"green":[65,150],"yellow":[150,175],"red":[175,200]}},
                                label = {"label":'RTD1',
                                         "style":{"color":"black","font-size":"30px"}},
                                labelPosition='top',showCurrentValue=True,units='F',size=gaugeSize,
                                scale={'start': 65, 'interval': 5, 'labelInterval': 10},
                                max=200, min=65, value=98
                                ),
                            dcc.Interval(
                        		id = 'gauge-update-RTD1',
                        		interval = 5000,
                        		n_intervals = 1
                                )      
                            ]
                    ),
                
                #RTD2 Gauge ######################
                html.Td(
                        [
                            daq.Gauge(
                                id='my-gauge-RTD2',
                                color={"gradient":False,"ranges":{"green":[65,150],"yellow":[150,175],"red":[175,200]}},
                                label = {"label":'RTD2',
                                         "style":{"color":"black","font-size":"30px"}},
                                labelPosition='top',showCurrentValue=True,units='F',size=gaugeSize,
                                scale={'start': 65, 'interval': 5, 'labelInterval': 10},
                                max=200, min=65, value=98
                                ),
                            dcc.Interval(
                        		id = 'gauge-update-RTD2',
                        		interval = 5000,
                        		n_intervals = 1
                                )      
                        ]

                    ),
                
                #RTD3 Gauge ######################
                html.Td(
                        [
                            daq.Gauge(
                                id='my-gauge-RTD3',
                                color={"gradient":False,"ranges":{"green":[65,150],"yellow":[150,175],"red":[175,200]}},
                                label = {"label":'RTD3',
                                         "style":{"color":"black","font-size":"30px"}},
                                labelPosition='top',showCurrentValue=True,units='F',size=gaugeSize,
                                scale={'start': 65, 'interval': 5, 'labelInterval': 10},
                                max=200, min=65, value=98
                                ),
                            dcc.Interval(
                        		id = 'gauge-update-RTD3',
                        		interval = 5000,
                        		n_intervals = 1
                                )       
                        ]
                    )  ,
                ],style={"width": "100%", "font-weight": "bold"}
                ),
            ),
        
        
        ##Second chart with IR readings
        ###########################################
        html.Div([
            html.H5('IR Sensors'),
        		dcc.Graph(id = 'live-graph1', animate = True),
        		dcc.Interval(
        			id = 'graph-update1',
        			interval = 5000,
        			n_intervals = 1
        		),
                dcc.Slider(
                    id='my-graph-slider-2',min=0,max=10,value=5
                ),
            ],         
            className="graph__container",
        ),
        
        
        ##################################IR Gauges##########################
        ######IR1 Gauge
        html.Div([  #IR1
            daq.Gauge(
                id='my-gauge-2',
                color={'theme':'primary',"gradient":False,"ranges":{"blue":[50,130],"green":[130,400],"yellow":[400,500],"red":[500,550]}},
                label = {"label":'IR1',"style":{"color":"black","font-size":"25px"}},
                labelPosition='top',
                showCurrentValue=True,
                units='F',size=gaugeSize,
                scale={'start': 50, 'interval': 5, 'labelInterval': 50},
                max=550,min=50,value=98,

                ),
        dcc.Interval(
    		id = 'gauge-update2',
    		interval = 5000,
    		n_intervals = 1
    	),
        ],style={'display': 'inline-block','font-size':20,'color':'black'},
        ),
            
        ##############IR2 Gauge
        html.Div([
            daq.Gauge(
                id='my-gauge-3',
                color={"gradient":False,"ranges":{"blue":[50,130],"green":[130,400],"yellow":[400,500],"red":[500,550]}},
                label = {"label":'IR2',"style":{"color":"black","font-size":"25px"}},
                labelPosition='top',
                showCurrentValue=True,
                units='F',size=gaugeSize,
                scale={'start': 50, 'interval': 5, 'labelInterval': 50},
                max=550,min=50,value=98
                ),
        dcc.Interval(
    		id = 'gauge-update3',
    		interval = 5000,
    		n_intervals = 1
    	),
        ],style={'display': 'inline-block'},
        ),
        
        ##IR3
        html.Div([  #IR3
            daq.Gauge(
                id='my-gauge-4',
                color={"gradient":False,"ranges":{"blue":[50,130],"green":[130,400],"yellow":[400,500],"red":[500,550]}},
                label = {"label":'IR3',"style":{"color":"black","font-size":"25px"}},
                labelPosition='top',
                showCurrentValue=True,
                units='F',size=gaugeSize,
                scale={'start': 50, 'interval': 5, 'labelInterval': 50},
                max=550,min=50,value=98
                ),
        dcc.Interval(
    		id = 'gauge-update4',
    		interval = 5000,
    		n_intervals = 1
    	),
        ],style={'display': 'inline-block'},
        ),
        
        
        #IR4 Gauge
        html.Div([  #IR4
            daq.Gauge(
                id='my-gauge-5',
                color={"gradient":False,"ranges":{"blue":[50,130],"green":[130,400],"yellow":[400,500],"red":[500,550]}},
                label = {"label":'IR4',"style":{"color":"black","font-size":"25px"}},
                labelPosition='top',
                showCurrentValue=True,
                units='F',size=gaugeSize,
                scale={'start': 50, 'interval': 5, 'labelInterval': 50},
                max=550,min=50,value=98
                ),
        dcc.Interval(
    		id = 'gauge-update5',
    		interval = 5000,
    		n_intervals = 1
            )        
        ],style={'display': 'inline-block'},
        ),
        
        ##IR5
        html.Div([  #IR5
            daq.Gauge(
                id='my-gauge-6',
                color={"gradient":False,"ranges":{"blue":[50,130],"green":[130,400],"yellow":[400,500],"red":[500,550]}},
                label = {"label":'IR5',"style":{"color":"black","font-size":"25px"}},
                labelPosition='top',
                showCurrentValue=True,
                units='F',size=gaugeSize,
                scale={'start': 50, 'interval': 5, 'labelInterval': 50},
                max=550,min=50,value=98
                ),
        dcc.Interval(
    		id = 'gauge-update6',
    		interval = 5000,
    		n_intervals = 1
    	),
        ],style={'display': 'inline-block'},
        ),
        
        ##IR6
        html.Div([  #IR2
            daq.Gauge(
                id='my-gauge-7',
                color={"gradient":False,"ranges":{"blue":[50,130],"green":[130,400],"yellow":[400,500],"red":[500,550]}},
                label = {"label":'IR6',"style":{"color":"black","font-size":"25px"}},
                labelPosition='top',
                showCurrentValue=True,
                units='F',size=gaugeSize,
                scale={'start': 50, 'interval': 5, 'labelInterval': 50},
                max=550,min=50,value=98
                ),
        dcc.Interval(
    		id = 'gauge-update7',
    		interval = 5000,
    		n_intervals = 1
    	),
        ],style={'display': 'inline-block'},
        ),
        
        ##IR7
        html.Div([  #IR2
            daq.Gauge(
                id='my-gauge-8',
                color={"gradient":False,"ranges":{"blue":[50,130],"green":[130,400],"yellow":[400,500],"red":[500,550]}},
                label = {"label":'IR7',"style":{"color":"black","font-size":"25px"}},
                labelPosition='top',
                showCurrentValue=True,
                units='F',size=gaugeSize,
                scale={'start': 50, 'interval': 5, 'labelInterval': 50},
                max=550,min=50,value=98
                ),
        dcc.Interval(
    		id = 'gauge-update8',
    		interval = 5000,
    		n_intervals = 1
    	),
        ],style={'display': 'inline-block'},
        ),
        
        ##IR8
        html.Div([  #IR8
            daq.Gauge(
                id='my-gauge-9',
                color={"gradient":False,"ranges":{"blue":[50,130],"green":[130,400],"yellow":[400,500],"red":[500,550]}},
                label = {"label":'IR8',"style":{"color":"black","font-size":"25px"}},
                labelPosition='top',
                showCurrentValue=True,
                units='F',size=gaugeSize,
                scale={'start': 50, 'interval': 5, 'labelInterval': 50},
                max=550,min=50,value=98
                ),
        dcc.Interval(
    		id = 'gauge-update9',
    		interval = 5000,
    		n_intervals = 1
    	),
        ],style={'display': 'inline-block'},
        ),
        
        ##IR9
        html.Div([  #IR9
            daq.Gauge(
                id='my-gauge-10',
                color={"gradient":False,"ranges":{"blue":[50,130],"green":[130,400],"yellow":[400,500],"red":[500,550]}},
                label = {"label":'IR9',"style":{"color":"black","font-size":"25px"}},
                labelPosition='top',
                showCurrentValue=True,
                units='F',size=gaugeSize,
                scale={'start': 50, 'interval': 5, 'labelInterval': 50},
                max=550,min=50,value=98
                ),
        dcc.Interval(
    		id = 'gauge-update10',
    		interval = 5000,
    		n_intervals = 1
    	),
        ],style={'display': 'inline-block'},
        ),
        
        ##IR10
        html.Div([  #IR9
            daq.Gauge(
                id='my-gauge-11',
                color={"gradient":False,"ranges":{"blue":[50,130],"green":[130,400],"yellow":[400,500],"red":[500,550]}},
                label = {"label":'IR10',"style":{"color":"black","font-size":"25px"}},
                labelPosition='top',
                showCurrentValue=True,
                units='F',size=gaugeSize,
                scale={'start': 50, 'interval': 5, 'labelInterval': 50},
                max=550,min=50,value=98
                ),
        dcc.Interval(
    		id = 'gauge-update11',
    		interval = 5000,
    		n_intervals = 1
    	),
        ],style={'display': 'inline-block'},
        ),
        
            
    ]
)
#my-graph-slider-1
@app.callback(
	Output('live-graph', 'figure'),
	Input('graph-update', 'n_intervals'),
    Input('my-graph-slider-1', 'value')
)

def update_graph_temp(n,value):
    #used to set scale
    df2 = df[['J-Type TC 1 (degF)','RTD 1 (degF)','RTD 2 (degF)','RTD 3 (degF)']].copy()
    
    time = df.iloc[n,0].split()[1]
    
    time2 = time.split('.')[0]
    time1 = datetime.strptime(time2, '%H:%M:%S')
    
    width = value*.01
    
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

    fig.update_layout(xaxis=dict(range=[max(xTemp)-width,max(xTemp)+.0001]),
                  yaxis = dict(range = [df2.to_numpy().min()-5,df2.to_numpy().max()+5]),
                  paper_bgcolor="LightSteelBlue",
                  )
    
    return fig

@app.callback(
	Output('live-graph1', 'figure'),
	Input('graph-update1', 'n_intervals'),
    Input('my-graph-slider-2', 'value')
)
def update_graph_IR1(n,value):
    
    df2 = df[['IR 1 (F)','IR 2 (F)','IR 3 (F)','IR 4 (F)',
              'IR 5 (F)','IR 6 (F)','IR 7 (F)', 'IR 8 (F)',
              'IR 9 (F)','IR 10 (F)']].copy()
    
    width = value * .01
	
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
        xaxis = dict(range = [max(XIr1)-width,max(XIr1)+.0001]),
        yaxis = dict(range = [df2.to_numpy().min()+10,df2.to_numpy().max()+10]),
        paper_bgcolor="LightSteelBlue",
    )
    
    return fig

@app.callback(Output('my-gauge-1', 'value'), 
              Input('gauge-update1', 'n_intervals'))
def update_gauge2(n):
    value = df.iloc[n,2]
    return value

@app.callback(Output('my-gauge-2', 'value'), 
              Input('gauge-update2', 'n_intervals'))
def update_gauga3(n):
    value = df.iloc[n,3]
    return value

@app.callback(Output('my-gauge-3', 'value'), 
              Input('gauge-update3', 'n_intervals'))
def update_gauga4(n):
    value = df.iloc[n,4]
    return value

@app.callback(Output('my-gauge-4', 'value'), 
              Input('gauge-update4', 'n_intervals'))
def update_gauga5(n):
    value = df.iloc[n,5]
    return value

@app.callback(Output('my-gauge-5', 'value'), 
              Input('gauge-update5', 'n_intervals'))
def update_gauge6(n):
    value = df.iloc[n,6]
    return value

@app.callback(Output('my-gauge-6', 'value'), 
              Input('gauge-update6', 'n_intervals'))
def update_gauga7(n):
    value = df.iloc[n,7]
    return value

@app.callback(Output('my-gauge-7', 'value'), 
              Input('gauge-update7', 'n_intervals'))
def update_gauga8(n):
    value = df.iloc[n,8]
    return value

@app.callback(Output('my-gauge-8', 'value'), 
              Input('gauge-update8', 'n_intervals'))
def update_gauga9(n):
    value = df.iloc[n,9]
    print(df['IR 8 (F)'].max(),df['IR 8 (F)'].min())

    return value

@app.callback(Output('my-gauge-9', 'value'), 
              Input('gauge-update9', 'n_intervals'))
def update_gauga10(n):
    value = df.iloc[n,10]
    return value

@app.callback(Output('my-gauge-10', 'value'), 
              Input('gauge-update10', 'n_intervals'))
def update_gauga11(n):
    value = df.iloc[n,11]
    return value

@app.callback(Output('my-gauge-11', 'value'), 
              Input('gauge-update11', 'n_intervals'))
def update_gauga12(n):
    value = df.iloc[n,12]
    return value

@app.callback(Output('my-gauge-RTD1', 'value'), 
              Input('gauge-update-RTD1', 'n_intervals'))
def update_gauge_rtd1(n):
    value = df.iloc[n,13]
    return value

@app.callback(Output('my-gauge-RTD2', 'value'), 
              Input('gauge-update-RTD2', 'n_intervals'))
def update_gauge_rtd2(n):
    value = df.iloc[n,14]
    return value

@app.callback(Output('my-gauge-RTD3', 'value'), 
              Input('gauge-update-RTD3', 'n_intervals'))
def update_gauge_rtd3(n):
    value = df.iloc[n,15]
    return value



if __name__ == '__main__':
	app.run_server(debug=True)
