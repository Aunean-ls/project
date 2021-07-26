import pandas as pd

df = pd.read_csv('../data/processedData.csv', encoding='utf-8', usecols=[0])
print(df)
data = {}
group = df.groupby('岗位名称')  # 按岗位名称进行分组
for x, y in group:
    data[x] = len(y)

sortData = sorted(data.items(), key=lambda asd: asd[1], reverse=True)  # 进行降序排序

row10 = sortData[:10]  # 招聘数量最多的10个岗位
print(row10)

position_num = pd.DataFrame(row10, columns=['岗位名称', '招聘数量'])
print(position_num)

position_num.to_csv('../data/position_num.csv', encoding='utf-8', index=False)

