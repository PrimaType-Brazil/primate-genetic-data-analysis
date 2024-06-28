import pandas as pd


pd.options.display.max_rows = 9999
pd.options.display.max_columns = 15
df = pd.read_csv('primates_dataset.csv')
#print(df.info())
#print(df.to_string)

#new_csv = df.dropna()
#new_csv.to_csv("novo_csv_analisar", sep = ';', index=False, encoding='utf-8')


dfgenetic = df.loc[df['genetic_variation']!=0,['genetic_variation','species_name']]
q1 = df['genetic_variation'].quantile(0.25)
q2 = df['genetic_variation'].quantile(0.75)
print(q1)
print(q2)
#print(new_csv.info())
#print(new_csv.to_string)
print(dfgenetic.describe)
print(dfgenetic.info())
#print(novo_csv.info())
#64 14 5