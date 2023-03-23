from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)


app.layout = html.Div([
    html.H4('Stock price analysis'),
    dcc.Graph(id="time-series-x-time-series-chart"),
    html.P("Select stock:"),
    dcc.Dropdown(
        id="time-series-x-ticker",
        options=["IR 1 (F)", "IR 2 (F)", "IR 3 (F)","J-Type TC 1 (degF)"],
        value="IR 1 (F)",
        clearable=False,
    ),
])


@app.callback(
    Output("time-series-x-time-series-chart", "figure"), 
    Input("time-series-x-ticker", "value"))
def display_time_series(ticker):
    df = pd.read_csv('dex-chart.csv')

    fig = px.line(df, x='Timestamp', y=ticker)
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
