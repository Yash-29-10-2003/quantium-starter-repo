from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

sales_data = pd.read_csv('Pink Morsel.csv')

#Before and after price increase
sales_before_increase = sales_data[sales_data['Date'] < '2021-01-15']
sales_after_increase = sales_data[sales_data['Date'] >= '2021-01-15']

app = Dash(__name__)
app.layout = html.Div([
    html.H1("Sales Data Visualization"),
    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'Before Price Increase', 'value': 'before_increase'},
            {'label': 'After Price Increase', 'value': 'after_increase'}
        ],
        value='before_increase'
    ),
    dcc.Graph(id='sales-chart')
])

@app.callback(
    Output('sales-chart', 'figure'),
    [Input('dropdown', 'value')]
)

def update_chart(selected_value):
    if selected_value == 'before_increase':
        sales_fig = px.line(sales_before_increase, x='Date', y='Total Sale of Morsel', title='Sales Before Price Increase')
    else:
        sales_fig = px.line(sales_after_increase, x='Date', y='Total Sale of Morsel', title='Sales After Price Increase')
    return sales_fig

if __name__ == '__main__':
    app.run_server(debug=True)