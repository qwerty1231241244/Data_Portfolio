import pandas as pd

data = {
    "product": ["Phone","Laptop","Headphones","Phone","","Mouse"],
    "price": [10000,20000,1500,10000,None,500]
}
df = pd.DataFrame(data)

# Remove empty rows
df = df.dropna()

# Remove duplicates
df = df.drop_duplicates()

# Add a new column
df["discounted_price"] = df["price"] * 0.9

# Export to Excel
df.to_excel("excel_cleaning.xlsx", index=False)
print(df)