nutricolors = ['gold', 'orange', 'coral', 'indianred', 'lightcoral',
               'palevioletred', 'deeppink', 'mediumvioletred', 'purple', 'indigo',
               'midnightblue', 'steelblue', 'skyblue', 'turquoise', 'springgreen',
               'yellowgreen', 'olivedrab', 'darkolivegreen', 'darkkhaki', 'goldenrod',
               'peru', 'sienna', 'saddlebrown', 'maroon', 'firebrick']

hover_text_item_chart = '<b>%{customdata[2]}</b><br>The amount of %{y} in %{customdata[3]} g of this product is %{customdata[0]} %{customdata[1]}, which is %{x} % of the daily intake recommendation.'

hover_text_ranking_chart = '<b>%{y}</b><br>The amount of %{customdata[0]} in 100 g of this product is %{x} %{customdata[1]}.'

def get_unit(df, nutrient):
    unit = list(df[df['Nutrient'] == nutrient].Unit)[0]

    return unit
