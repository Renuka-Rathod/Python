import pandas as pd
df=pd.read_csv("D:/IACSD/Python and R Programming/Python/Day15/market.csv")
print(df.columns)
print(df['market'].unique())
print(df['market'].nunique(),(df['market'].unique()))
#1.find the market 
df['market'].mode()
#2. Find state with maximum number of markets in it
# find unique pairs of state and market
df_1 = df.loc[:,['state','market']].drop_duplicates()
df_1.groupby('state')['market'].count()
#3.choose  the market
#find the maximum pricemax for that market for every year
df[df['market'] == 'ABOHAR(PB)'].groupby('year')['priceMax'].max()

