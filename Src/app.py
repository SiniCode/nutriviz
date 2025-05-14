# Import packages
import os

from dash import Dash, html, dash_table, dcc, callback, Output, Input

import pandas as pd
import dash_bootstrap_components as dbc

from layout_components import title_component, item_graph_heading_row, ranking_graph_heading_row, data_source_row
from utils import get_unit
from data_filters import filter_data_for_item_graph, filter_data_for_ranking_graph
from graph_constructors import construct_item_graph, construct_ranking_graph

# Incorporate data
data_file_path = os.path.join('Data', 'Fineli_food_data_processed.csv')
help_file_path = os.path.join('Data', 'Fineli_nutrients.csv')
df = pd.read_csv(data_file_path, sep=';')
df_help = pd.read_csv(help_file_path, sep=';')

# Initialize the app - incorporate a Dash Bootstrap theme
external_stylesheets = [dbc.themes.LUMEN]
app = Dash(__name__, external_stylesheets=external_stylesheets)

# App layout
app.layout = dbc.Container([
    title_component(),
    item_graph_heading_row(),

    dbc.Row([
        dbc.Col([
            html.Label('Select food item', htmlFor='food-item-selection'),
            dcc.Dropdown(
                list(df.Food.unique()),
                'SUGAR',
                id='food-item-selection',
                clearable=False
            )
        ], width=4),
        dbc.Col([
            html.Label('Amount (g)', htmlFor='amount-selection'),
            dcc.Input(id='amount-selection', type='number', min=1, max=1000, step=1, value=100)
        ], width=1),
        dbc.Col([
            dcc.Checklist(
                options=['Highlight 100 %'],
                value=[],
                id='highlight-100',
                inputStyle={'margin-right': '10px'}
            )
        ], width=3)
    ]),

    dbc.Row([
       dbc.Col([
            html.Label('Show nutrients', htmlFor='nutrients-to-show-selection'),
            dcc.Dropdown(
                list(df_help.Nutrient.unique()),
                list(df_help.Nutrient.unique()),
                id='nutrients-to-show-selection',
                multi=True
            )
        ], width=8),
        dbc.Col([
            html.Div(
                'Note: This is a reference guide only. The recommended values depend on many personal factors like age and gender.'
            )
        ], width=4, style={'padding-left': '40px'})
    ], style={'padding-top': '20px'}),

    dbc.Row([
        dbc.Col([
            dcc.Graph(figure={}, id='item-bar-chart')
        ], width=8),
        dbc.Col([
            dash_table.DataTable(
                id='recommendation-table',
                data=df_help.to_dict('records'),
                columns=[{'name': i, 'id': i} for i in ['Nutrient', 'Recommended daily intake', 'Unit']],
                style_table={'overflowX': 'auto'}
            )
        ], width=4, style={'padding-left': '40px'})
    ]),

    ranking_graph_heading_row(),

    dbc.Row([
        dbc.Col([
            html.Label('Select nutrient', htmlFor='nutri-selection'),
            dcc.Dropdown(
                list(df.columns)[3:28],
                'Carbohydrates',
                id='nutri-selection',
                clearable=False
            )
        ], width=3),
        dbc.Col([
            html.Label('Select food category', htmlFor='category-selection'),
            dcc.Dropdown(
                ['All'] + sorted(list(df.Category.unique())),
                'All',
                id='category-selection',
                clearable=False
            )
        ], width=3),
        dbc.Col([
            dbc.Row(html.Label('Search with keyword', htmlFor='keyword-input')),
            dbc.Row(dcc.Input(id='keyword-input', type='text', value=''))
        ], width=1),
        dbc.Col([
            dbc.Row(html.Label('Show', htmlFor='show-selection')),
            dbc.Row(dcc.Input(id='show-selection', type='number', min=1, max=50, step=1, value=10))
        ], width=1),
        dbc.Col([
            dbc.RadioItems(options=[{"label": x, "value": x} for x in ['Maximize intake', 'Minimize intake']],
                       value='Maximize intake',
                       inline=False,
                       id='minmax-radio')
        ], width=3)
    ]),

    dbc.Row([
        dcc.Graph(figure={}, id='ranking-bar-chart')
    ]),

    data_source_row()

], fluid=True, style={'padding': '60px'})

# Add controls to build the interaction

@callback(
    Output(component_id='item-bar-chart', component_property='figure'),
    Input(component_id='food-item-selection', component_property='value'),
    Input(component_id='amount-selection', component_property='value'),
    Input(component_id='nutrients-to-show-selection', component_property='value'),
    Input(component_id='highlight-100', component_property='value')
)
def update_item_graph(food, amount, nutrients, highlight):
    
    data = filter_data_for_item_graph(df, df_help, food, amount, nutrients)
    fig = construct_item_graph(data, food, highlight)
    
    return fig

@callback(
    Output(component_id='ranking-bar-chart', component_property='figure'),
    Input(component_id='nutri-selection', component_property='value'),
    Input(component_id='category-selection', component_property='value'),
    Input(component_id='keyword-input', component_property='value'),
    Input(component_id='show-selection', component_property='value'),
    Input(component_id='minmax-radio', component_property='value')
)
def update_ranking_graph(nutrient, category, keyword, show, minmax):

    unit = get_unit(df=df_help, nutrient=nutrient)
    data = filter_data_for_ranking_graph(df, nutrient, category, keyword, show, minmax, unit)
    fig = construct_ranking_graph(data, nutrient, unit)

    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
