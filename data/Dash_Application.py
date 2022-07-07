from dash import Dash, html, dcc, Input, Output
import csv
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('Filtered_Data.csv')
df = df.sort_values(by="Date")

app.layout = html.Div(children=[
    html.Div([
        html.H1(children='Sales($) vs Date'),
        dcc.RadioItems(
            ['north', 'east', 'south', 'west', 'all'],
            'All',
            id='region',
            inline=True
            )
        ], style = {'text-align': 'center'}),
    
        html.Div([
            dcc.Graph(
                id='output_graph',
            )
        ])
])

@app.callback(
    Output('output_graph', 'figure'),
    Input('region', 'value'))
def update_graph(region_name):
    if region_name != 'all':
        filtered_df = df[df['Region'] == region_name]
    else :
        filtered_df = df

    fig = px.line(filtered_df, x="Date", y="Sales")
    fig.update_layout(transition_duration=500)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)