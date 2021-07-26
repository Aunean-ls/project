import pandas as pd


df = pd.read_csv('../data/processedData.csv', encoding='utf-8')
data = df['工作福利'].str.split(' ')

data_list = []

for i in data:
    for j in i:
        data_list.append(j)

print(len(data_list))

df2 = pd.DataFrame(data_list, columns=['福利待遇'])

data = {}
group = df2.groupby('福利待遇')

for x, y in group:
    data[x] = len(y)
print(sum(data.values()))
welfare_num = pd.DataFrame(data.items(), columns=['福利待遇', '数量'])
print(welfare_num)

# welfare_num.to_csv('../data/welfare_num.csv', encoding='utf-8', index=False)
