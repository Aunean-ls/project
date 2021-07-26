import pandas as pd


df = pd.read_csv('../data/processedData.csv', encoding='utf-8')

df['区域'] = df['工作地点'].str.split('-').str[1]
df['工作地点'] = df['工作地点'].str.split('-').str[0]
# print(df)

data = {}
group = df.groupby('工作地点')  # 按工作地点进行分组
for x, y in group:
    data[x] = len(y)

print(data)

sortData = sorted(data.items(), key=lambda asd: asd[1], reverse=True)  # 进行降序排序

row15 = sortData[:15]  # 招聘数量前十五的城市
print(row15)

workAddress_num = pd.DataFrame(row15, columns=['工作地点', '招聘数量'])
print(workAddress_num)

# workAddress_num.to_csv('../data/workAddress_num.csv', encoding='utf-8', index=False)

