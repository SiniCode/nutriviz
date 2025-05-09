import dash_bootstrap_components as dbc
from dash import html

def title_component():
    component = dbc.Row([
        html.Div(
            'Nutriviz',
            className='text-primary text-center fs-1'
        )
    ], style={'margin-top': '20px', 'margin-bottom': '80px'})

    return component

def item_graph_heading_row():
    row = dbc.Row([
        dbc.Col([
            html.Div(
                'Total nutrients',
                className='text-primary text-left fs-2'
            )
        ], width=8),
        dbc.Col([
            html.Label(
                'Daily intake recommendations',
                htmlFor='recommendation-table',
                className='text-primary fs-2'
            )
        ], width=4, style={'padding-left': '40px'})
    ], style={'margin-bottom': '20px'})

    return row

def ranking_graph_heading_row():
    row = dbc.Row([
        html.Div(
            'Rank food items',
            className='text-primary text-left fs-2'
        )
    ], style={'margin-top': '60px', 'margin-bottom': '20px'})

    return row

def data_source_row():
    row = dbc.Row([
        html.Div(
            'Original data source: Finnish Institute of Health and Welfare, Fineli. License: CC-BY 4.0.',
            className='text-left'
        )
    ])

    return row
