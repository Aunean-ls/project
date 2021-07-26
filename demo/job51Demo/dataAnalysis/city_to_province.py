import pandas as pd


df = pd.read_csv('../data/processedData.csv', encoding='utf-8', usecols=[1])
df2 = pd.read_csv('../data/China-City-List-latest2.csv', encoding='utf-8')
# df['区域'] = df['工作地点'].str.split('-').str[1]
df['工作地点'] = df['工作地点'].str.split('-').str[0]
v0 = df2['一级行政区划(Adm1)'].values
v1 = df2['二级行政区划(Adm2)'].values

dic1 = dict(zip(v1, v0))

data = []
# print(len(df['工作地点']))  # 8285
for i in df['工作地点']:
    if i in dic1.keys():
        tuple1 = tuple([i, dic1.get(i)])
        data.append(tuple1)
    if '省' in i:
        # print(i)
        tuple2 = tuple([i.replace('省', ''), i.replace('省', '')])
        data.append(tuple2)
# print(len(data))  # 8204

city_province = pd.DataFrame(data, columns=['城市', '省份'])

data = {}
group = city_province.groupby('省份')  # 按省份进行分组
for x, y in group:
    data[x] = len(y)
print(data)

province_num = pd.DataFrame(data.items(), columns=['省份', '数量'])
print(province_num)

province_num.to_csv('../data/province_num.csv', encoding='utf-8', index=False)

