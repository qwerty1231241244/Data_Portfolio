import pandas as pd

data = [
    {"product": "Phone", "price": 10000},
    {"product": "Laptop", "price": 20000},
    {"product": "Headphones", "price": 1500},
    {"product": "Mouse", "price": 500},
    {"product": "Keyboard", "price": 500},
]

df = pd.DataFrame(data)
df["discounted_price"] = df["price"] * 0.9
df["label"] = df["product"] + " - $" + df["price"].astype(str)
df["expensive"] = df["price"].apply(lambda x: "Yes" if x>15000 else "No")
df = df.sort_values(by="price", ascending=False)
df.to_excel("products.xlsx", index=False)
print(df)