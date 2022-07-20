import pandas as pd

# CREATING DATAFRAMES

df_customer = pd.DataFrame({'Customer_id': [1, 2, 3, 4, 5], 'Age': [18, 19, 20, 19, 21]})
df_Sales = pd.DataFrame({'Sales_id': [101, 202, 303, 404, 505], 'Customer_id': [1, 2, 3, 4, 5]})
df_Orders = pd.DataFrame(
    {'Order_id': [10, 20, 30, 40, 50], 'Sales_id': [101, 202, 303, 404, 505], 'Item_id': [1011, 2022, 3033, 4044, 5055],
     'Quantity': [21, 43, 2, 76, 4]})
df_Items = pd.DataFrame(
    {'Item_id': [1011, 2022, 3033, 4044, 5055], 'Item_name': str(['Apple', 'Samsung', 'OnePlus', 'Motorola', 'Nokia'])})

# MERGING DATAFRAMES

merge_Customer_Sales = pd.merge(df_customer, df_Sales, on='Customer_id')
merge_Customer_Sales_Orders = pd.merge(merge_Customer_Sales, df_Orders, on='Sales_id')
merge_Customer_Sales_Orders_Items = pd.merge(merge_Customer_Sales_Orders, df_Items, on='Item_id')

# CREATING POSSIBLE COMBINATION OF CUSTOMERS AND ITEMS

output_concat_final = pd.DataFrame({'Customer_id': [], 'Item_id': []})
for customer in merge_Customer_Sales_Orders_Items['Customer_id']:
    for item in merge_Customer_Sales_Orders_Items['Item_id']:
        output_df = pd.DataFrame({'CUSTOMER': [customer], 'Item_id': [item]})
        output_concat_final = pd.concat([output_concat_final, output_df])

# MERGING THE COMBINATION DATAFRAME TO THE REQUIRED DATAFRAME

new_final = merge_Customer_Sales_Orders_Items[['Customer_id', 'Item_id', 'Age', 'Quantity']]
final_df = pd.merge(new_final, output_concat_final, on='Item_id')

# DROPPING UNNECESSARY COLUMNS

final_df = final_df.drop(columns=['Customer_id_x', 'Customer_id_y'])

# REORGANIZING COLUMNS AS PER REQUIREMENT

new_column = ['CUSTOMER', 'Age', 'Item_id', 'Quantity']
final_df = final_df[new_column]
print(final_df)

# SAVING THE DATAFRAME TO .CSV FORMAT

final_df.to_csv('ETLPANDAS.csv', index = False)
