from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker
import pandas as pd
from pyecharts.globals import ThemeType

df = pd.read_csv('../data/companyType_num.csv', encoding='utf-8')
# print(df)

v0 = df['公司类型'].values
print(v0)
v1 = df['数量']
print(v1)


pie = (
    Pie(init_opts=opts.InitOpts(theme=ThemeType.SHINE))
    .add(
        "",
        [list(z) for z in zip(v0, v1)],
        # radius=["30%", "50%"],
        center=["45%", "50%"],
        # label_opts=opts.LabelOpts(is_show=True),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="各类公司类型占比", pos_left='50%', ),
        legend_opts=opts.LegendOpts(
            type_="scroll", pos_top="20%", pos_left="85%", orient="vertical"
        ),
    )
    .set_series_opts(
        label_opts=opts.LabelOpts(formatter="{b}:{c}\r\n{d}%", font_size=14)
    )
)

pie.render("folder/companyType_pie.html")
