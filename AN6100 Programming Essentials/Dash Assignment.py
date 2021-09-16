# Web Assignment Part 1/2
# Date:     2021 Aug 01
# Author:   Yuan Liben
# Group:    B
# Index Number: 43
# Organisation: Nanyang Business School, NTU
# Program:  MSBA
# Course:   AN6100-Programming Essentials
# --------------------------------------------
# Question1: The analysis goal and why use this way of presentation for the goal.
# Answer1: The analysis goal of this dashboard design is, by observing our sales amount and profit to a
#          specific customer on a yearly, monthly or daily scale, the dashboard will help us to understand
#          more about our sales trend and profit trend to this certain customer. In other words, how our
#          sales amount and profit amount to this selected customer performs in different time periods.
#          To fit this goal, I set an interactive dashboard. By selecting the customer and the time period,
#          users are able to view our sales amount, cost and profit to this customer in that period of time
#          in a bar chart. Users can also select All in times dropdown choices to view our sales performance
#          in a specific month over the 10 years.

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

df = pd.read_csv('WebAssignment.csv')
df['CustomerID'] = df['CustomerID'].map(lambda x: x.upper())
unicustomerID = sorted(list(set(df.loc[:, 'CustomerID'])))
year = list(range(2011, 2022))
year.insert(0, 'All')
month = list(range(1, 13))
month.insert(0, 'All')
day = list(range(1, 32))
day.insert(0, 'All')
ex_style = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets= ex_style)
app.layout = html.Div([
    html.H1(children='Business Intelligent Interactive Dashboard',
            style={'textAlign': 'center'}),
    html.Div(children='Please select your preferred customer ID and time period. '
                      'You can select All time periods if you want.',
             style={'textAlign': 'center'}),
    html.Div(children='Yuan Liben',
             style={'textAlign': 'center'}),
    html.Div(children='02 Aug 2021',
             style={'textAlign': 'center'}),
    html.Label('CustomerID'),
    dcc.Dropdown(options=[{'label': i, 'value': i} for i in unicustomerID], id='CusID', value='IJ01'),
    html.Label('Year'),
    dcc.Dropdown(options=[{'label': i, 'value': i} for i in year], id='returnY', value=year[1]),
    html.Label('Month'),
    dcc.Dropdown(options=[{'label': i, 'value': i} for i in month], id='returnM', value=month[1]),
    html.Label('Day'),
    dcc.Dropdown(options=[{'label': i, 'value': i} for i in day], id='returnD', value=3),
    dcc.Graph(id='bar-chart'),
])

@app.callback(
    Output('bar-chart', 'figure'),
    [Input('CusID', 'value'),
     Input('returnY', 'value'),
     Input('returnM', 'value'),
     Input('returnD', 'value')])
def genarate_gragh(CusID, returnY, returnM, returnD):
    if returnY != 'All':
        if returnM != 'All':
            if returnD != 'All':
                df1 = df.loc[(df.CustomerID == CusID) & (df.YYYY == returnY) & (df.MM == returnM) & (df.DD == returnD), ['Amount', 'Cost']]
            else:
                df1 = df.loc[(df.CustomerID == CusID) & (df.YYYY == returnY) & (df.MM == returnM), ['Amount', 'Cost']]
        else:
            if returnD != 'All':
                df1 = df.loc[(df.CustomerID == CusID) & (df.YYYY == returnY) & (df.DD == returnD), ['Amount', 'Cost']]
            else:
                df1 = df.loc[(df.CustomerID == CusID) & (df.YYYY == returnY), ['Amount', 'Cost']]
    else:
        if returnM != 'All':
            if returnD != 'All':
                df1 = df.loc[(df.CustomerID == CusID) & (df.MM == returnM) & (df.DD == returnD), ['Amount', 'Cost']]
            else:
                df1 = df.loc[(df.CustomerID == CusID) & (df.MM == returnM), ['Amount', 'Cost']]
        else:
            if returnD != 'All':
                df1 = df.loc[(df.CustomerID == CusID) & (df.DD == returnD), ['Amount', 'Cost']]
            else:
                df1 = df.loc[(df.CustomerID == CusID), ['Amount', 'Cost']]
    amount = round(sum(df1['Amount']), 2)
    cost = round(sum(df1['Cost']), 2)
    profit = round((amount - cost), 2)
    newdata = [amount, cost, profit]
    colname = ['Sales Amount', 'Cost', 'Profit']
    df2 = pd.DataFrame({'DataType': colname, 'Amount': newdata})
    fig = px.bar(df2, x="DataType", y="Amount", color='Amount',
                 color_continuous_scale=px.colors.sequential.Tealgrn, text='Amount')
    return fig


if __name__ == '__main__':
    app.run_server(debug = True)

# Question2: Insights gotten from dashboard.
# Answer2: (1) IJ01 is one of our largest customer that contributes over 23M sales amount and 4.7M profit over
#              the 10 years.
#          (2) From the data in first 4 months in 2021, we can infer that the sales amount and profit from IJ01 in 2021
#              will stay steadily like the performance in year 2020.
#          (3) Showing from the data in last 10 years, IJ01 will purchase most amount of product in December, while
#              purchase least in February (in scale of money spent).
#          (4) In a month, 20th is the day that IJ01 tends to purchase most amount of product (in scale of money spent).
