import pandas as pd
df = pd.read_excel("1.xlsx")
df.to_csv("data.csv", index=False, encoding='utf-8-sig')