from pyecharts import options as opts
from pyecharts.charts import Bar, Grid
from pyecharts.faker import Faker
import pandas as pd

df = pd.read_csv('../data/position_num_top5.csv', encoding='utf-8')
# print(df)

v0 = df['岗位名称'].values.tolist()
print(v0)
v1 = df['招聘数量'].values.astype(int).tolist()
print(v1)

c = (
    Bar()
        .add_xaxis(v0)
        .add_yaxis("", v1, gap='60%', color='blue')
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right"), )
        .set_global_opts(title_opts=opts.TitleOpts(title="招聘数量前五岗位"))

)
grid = Grid()
grid.add(c, grid_opts=opts.GridOpts(pos_left='40%'), )
grid.render('folder/position_bar.html')


# def grid_base() -> Grid:
#     c = (
#         Bar()
#             .add_xaxis(v0)
#             .add_yaxis("", v1)
#             .reversal_axis()
#             .set_series_opts(label_opts=opts.LabelOpts(position="right"), )
#             .set_global_opts(title_opts=opts.TitleOpts(title="招聘数量前五岗位"))
#     )
#
#     grid = Grid()
#     # 仅使用pos_top修改相对顶部的位置
#     grid.add(c, grid_opts=opts.GridOpts(pos_left="50%"))
#
#     return grid
#
#
# if __name__ == '__main__':
#     grid_base().render('folder/position_bar.html')
