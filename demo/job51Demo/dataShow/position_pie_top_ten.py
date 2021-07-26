from pyecharts.charts import Pie
import pyecharts.options as opts
from pyecharts.globals import ThemeType
import pandas as pd

df = pd.read_csv('../data/position_num.csv', encoding='utf-8')
# print(df)

v0 = df['岗位名称'].values
print(v0)
v1 = df['招聘数量']
print(v1)
print([list(z) for z in zip(v0, v1)])


pie = (
    Pie(init_opts=opts.InitOpts(theme=ThemeType.SHINE))
    .add(
        "",
        [list(z) for z in zip(v0, v1)],
        radius=["30%", "50%"],
        center=["45%", "50%"],
        # label_opts=opts.LabelOpts(is_show=True),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="招聘数量前十占比", pos_left='50%', ),
        legend_opts=opts.LegendOpts(
            type_="scroll", pos_top="20%", pos_left="80%", orient="vertical"
        ),
    )
    .set_series_opts(
        label_opts=opts.LabelOpts(formatter="{b}:{c}\r\n{d}%", font_size=14)
    )
)

pie.render('folder/position_pie_top_ten.html')
