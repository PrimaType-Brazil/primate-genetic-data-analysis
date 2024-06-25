import pandas as pd


pd.options.display.max_rows = 9999
pd.options.display.max_columns = 15
df = pd.read_csv('primates_dataset.csv')
print(df.info())

df.dropna(inplace = True)

print(df.info())
print(df.to_string)
#print(novo_csv.info())
