from pyecharts import options as opts
from pyecharts.charts import Map, Geo
import pandas as pd
from pyecharts.globals import ChartType

df = pd.read_csv('../data/province_num.csv', encoding='utf-8')
# print(df)

v0 = df['省份'].values.tolist()
print(v0)
v1 = df['数量'].values.astype(int).tolist()
print(v1)


c = (
    Map()
    .add("", [list(z) for z in zip(v0, v1)], "china", is_map_symbol_show=False)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="各省岗位分布"),
        visualmap_opts=opts.VisualMapOpts(max_=2600),
    ).set_series_opts(label_opts=opts.LabelOpts(is_show=False))
)

# c = (
#     Geo()
#     .add_schema(maptype="china")
#     .add("geo", [list(z) for z in zip(v0, v1)])
#     .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
#     .set_global_opts(
#         visualmap_opts=opts.VisualMapOpts(max_=2600), title_opts=opts.TitleOpts(title="Geo-基本示例")
#     )
# )

# c = (
#     Geo()
#         .add_schema(maptype="china",
#
#                     )
#
#         .add("geo", [list(z) for z in zip(v0, v1)], type_=ChartType.HEATMAP,
#
#              )
#
#         # .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
#
#         .set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=500),
#                          title_opts=opts.TitleOpts(title="Geo-基本示例"), )
# )

c.render('folder/wordAddress_map.html')
