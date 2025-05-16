import pandas as pd


def filter_data_for_item_graph(df, df_help, food, amount, nutrients):
    if amount == None:
        amount = 0

    if nutrients == None:
        nutrients = []
    
    item = df[df.Food == food]
    percentages = item.iloc[:, 3:28] / list(df_help['Recommended daily intake']) * 100 * (amount/100)
    amounts = item.iloc[:, 3:28] * (amount/100)

    data = pd.DataFrame({
        'Nutrient': list(df_help['Nutrient']),
        'Percent of the recommended daily intake (%)': percentages.iloc[0,:],
        'Nutriamount': amounts.iloc[0, :],
        'Unit': list(df_help['Unit']),
        'Food': [f'{food}']*25,
        'Foodamount': [amount]*25
    })

    data = data.loc[data['Nutrient'].isin(nutrients)]

    return data

def filter_data_for_ranking_graph(df, nutrient, category, diet, keyword, show, minmax, unit):
    if show == None:
        show = 0
    
    ascending = minmax == 'Minimize intake'

    if category != 'All':
        selected_items = df[df.Category == category]
    else:
        selected_items = df

    if diet != 'None':
        selected_items = selected_items[selected_items[diet] == 1]

    if len(keyword) > 0:
        selected_items = selected_items[selected_items['Food'].str.contains(keyword.upper())]
    
    data_length = min(show, selected_items.shape[0])

    data = selected_items.sort_values(by=nutrient, ascending=ascending).head(data_length)
    data['Nutrient'] = [f'{nutrient.lower()}']*data_length
    data['Unit'] = [unit]*data_length

    return data

def filter_data_for_stacked_graph(df, df_help, selected_foods, stored_amounts):
    data = pd.DataFrame()

    for food in selected_foods:
        item = df[df.Food == food]
        item = item.iloc[:, [1] + list(range(3, 28))]
        item.iloc[:, 1:] = item.iloc[:, 1:] / list(df_help['Recommended daily intake']) * 100 * (stored_amounts.get(food, 0)/100)
        data = pd.concat([data, item])

    data_long = data.melt(id_vars=['Food'], var_name='Nutrient', value_name='Percent of the RDI (%)')

    return data_long
