import pandas as pd

df = pd.read_excel("supermarket_sales.xlsx")
df.head()

#select columns
df = df[['Gender', 'Product line','Total']]

#Make pivot table
pivot_table = df.pivot_table(index='Gender', columns='Product line',values='Total',
                             aggfunc='sum').round(0)

#Export pivot table to Excel file
pivot_table.to_excel('pivot_table.xlsx','Report', startrow=4)

