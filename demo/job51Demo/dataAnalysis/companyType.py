import pandas as pd

df = pd.read_csv('../data/processedData.csv', encoding='utf-8')


data = {}
group = df.groupby('公司类型')
for x, y in group:
    data[x] = len(y)
print(data)

companyType_num = pd.DataFrame(data.items(), columns=['公司类型', '数量'])
print(companyType_num)

companyType_num.to_csv('../data/companyType_num.csv', encoding='utf-8', index=False)

