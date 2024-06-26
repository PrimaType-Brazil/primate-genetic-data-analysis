import pandas as pd


pd.options.display.max_rows = 9999
pd.options.display.max_columns = 15
df = pd.read_csv('primates_dataset.csv')
print(df.info())
print(df.to_string)

new_csv = df.dropna()
new_csv.to_csv("novo_csv_analisar", sep = ';', index=False, encoding='utf-8')

print(new_csv.info())
print(new_csv.to_string)
#print(novo_csv.info())
