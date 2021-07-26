import pandas as pd

df = pd.read_csv('../data/processedData.csv', encoding='utf-8', usecols=[2])

data = []

for i in df.values:
    for j in i:
        if '万/月' in j:
            for x in (j.replace('万/月', '').split('-')):
                data.append(int(float(x) * 10))
        elif '万/年' in j:
            for x in (j.replace('万/年', '').split('-')):
                data.append(round((float(x) * 10 / 12), 1))
        elif '千/月' in j:
            for x in j.replace('千/月', '').split('-'):
                data.append(float(x))
        elif '元/天' in j:
            data.append(int(j.replace('元/天', '')) * 30)
        else:
            pass

df = pd.DataFrame(data, columns=['K'])
print(df)

# 异常值检测
mean_num = df['K'].mean()
std_num = df['K'].std()
max_num = mean_num + 2 * std_num
min_num = mean_num - 2 * std_num
print("正常值的范围：", max_num, min_num)
print("是否存在超出正常范围的值：", any(df['K'] > max_num))
print("是否存在小于正常范围的值：", any(df['K'] < min_num))

data = []
for i in df.values:
    for j in i:
        if max_num > j > min_num:
            data.append(j)
# data.sort()
# print(data)
# df = pd.DataFrame(data, columns=['K'])
# print(df)

cats1 = pd.cut(data, bins=[1, 5, 10, 15, 25, 50, 100, 500])
# print(cats1)

cats1_counts = cats1.value_counts()

salaryRange_num = pd.DataFrame(cats1_counts, columns=['数量'])
print(salaryRange_num)

salaryRange_num.to_csv('../data/salaryRange_num.csv', encoding='utf-8')
