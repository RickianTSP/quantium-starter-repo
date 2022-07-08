from dash import Dash, html, dcc
import csv
import plotly.express as px
import pandas as pd

app = Dash(__name__)

with open("./data/Filtered_Data.csv") as csv_file_r:
    csv_reader = csv.reader(csv_file_r, delimiter=',')
    date = []
    sales = []
    for row in csv_reader:
        if row:
            date.append(row[1])
            sales.append(row[0])

df = pd.DataFrame({
    "Date": date,
    "Sales": sales,
})

fig = px.line(df, x="Date", y="Sales")

app.layout = html.Div(children=[
    html.H1(children='Sales ($) vs Date'),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)