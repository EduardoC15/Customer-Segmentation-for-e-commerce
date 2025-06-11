import pandas as pd

# Define the data types for each column
dtype_dict = {
    'Invoice': 'string',
    'StockCode': 'string',
    'Description': 'string',
    'Quantity': 'int16',
    'Price': 'float32',
    'Country': 'category'
}

# Read the Excel file with specified data types
df = pd.read_excel(
    'online_retail_II.xlsx',
    sheet_name='Year 2010-2011',
    dtype=dtype_dict,
    parse_dates=['InvoiceDate']
)

df['StockCode'] = df['StockCode'].astype('category')
df['Description'] = df['Description'].astype('category')

# Convert to Parquet format
df.to_parquet('online_retail_II.parquet', index=False)

print(df.info())