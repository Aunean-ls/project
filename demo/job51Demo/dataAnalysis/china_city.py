import pandas as pd

df = pd.read_csv('../data/China-City-List-latest.csv', encoding='gbk', usecols=[7, 9])

df.drop_duplicates(inplace=True)
df['一级行政区划(Adm1)'] = df['一级行政区划(Adm1)'].str.replace('市', '')
df['一级行政区划(Adm1)'] = df['一级行政区划(Adm1)'].str.replace('省', '')
df['一级行政区划(Adm1)'] = df['一级行政区划(Adm1)'].str.replace('自治区', '')
df['一级行政区划(Adm1)'] = df['一级行政区划(Adm1)'].str.replace('特别行政区', '')
df['一级行政区划(Adm1)'] = df['一级行政区划(Adm1)'].str.replace('壮族', '')
df['一级行政区划(Adm1)'] = df['一级行政区划(Adm1)'].str.replace('回族', '')
df['一级行政区划(Adm1)'] = df['一级行政区划(Adm1)'].str.replace('维吾尔', '')
print(df)
df.to_csv('../data/China-City-List-latest2.csv', encoding='utf-8', index=False)
