from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

app = Dash(__name__)




app.layout = html.Div([
    html.H4('Analysis of Iris data using scatter matrix'),
    dcc.Dropdown(
        id="dropdown",
        options=['Timestamp','J-Type TC 1 (degF)', 'IR 1 (F)'],
        #value=['J-Type TC 1 (degF)', 'IR 1 (F)'],
        multi=True
    ),
    dcc.Graph(id="graph"),
])


@app.callback(
    Output("graph", "figure"), 
    Input("dropdown", "value"))
def update_bar_chart(dims):
    #df = px.data.iris() # replace with your own data source
    chart = pd.read_csv('dex-chart.csv')
    
    fig = px.line(chart, x = 'Timestamp',y = 'IR 1 (F)')
    fig = px.line(chart, x = 'Timestamp',y = 'IR 2 (F)')

        #chart, dimensions=dims)
    
    return fig


app.run_server(debug=True)