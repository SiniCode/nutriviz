import plotly.express as px
from utils import nutricolors, hover_text_item_chart, hover_text_ranking_chart

def construct_item_graph(data, food):
    title_text = f'The proportion of nutrients in {food} relative to the daily intake recommendation'

    fig = px.bar(
        data_frame=data,
        x='Percent of the recommended daily intake (%)',
        y='Nutrient',
        custom_data=['Nutriamount', 'Unit', 'Food', 'Foodamount'],
        title=title_text,
        orientation='h',
        height=860,
        color='Nutrient',
        color_discrete_sequence=nutricolors,
        text_auto='.1f'
    )
    
    fig.update_layout(title={'x': 0.5})
    fig.update_traces(
        hovertemplate=hover_text_item_chart,
        textposition='outside'
    ),
    fig.add_vline(x=100, line_width=3, line_color="grey")

    return fig

def construct_ranking_graph(data, nutrient, unit):
    xlab = f'{nutrient} ({unit})'
    title_text = f'The amount of {nutrient.lower()} in 100 g of the product'

    fig = px.bar(
        data_frame=data.iloc[::-1],
        x=nutrient,
        y='Food',
        custom_data=['Nutrient', 'Unit'],
        title=title_text,
        labels={nutrient: xlab},
        orientation='h',
        height=max(460, data.shape[0]*30),
        text_auto='.1f'
    )
    
    fig.update_layout(title={'x': 0.5})
    fig.update_traces(
        marker_color='darkcyan',
        hovertemplate=hover_text_ranking_chart,
        textposition='outside'
    )
    
    return fig
