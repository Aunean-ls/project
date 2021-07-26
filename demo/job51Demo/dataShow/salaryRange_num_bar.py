from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.commons.utils import JsCode
import pandas as pd
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType


df = pd.read_csv('../data/salaryRange_num.csv', encoding='utf-8')
# print(df)

v1 = df['数量'].values.tolist()
print(v1)
# v1 = df['招聘数量'].values.astype(int).tolist()
# print(v1)

c = (
    Bar(init_opts=opts.InitOpts(
        animation_opts=opts.AnimationOpts(
            animation_delay=500, animation_easing="cubicOut"
        ),
        theme=ThemeType.MACARONS))
        .add_xaxis(["1-5", "5-10", "10-15", "15-25", "25-50", "50-100", "100-500"])
        .add_yaxis("", v1, category_gap="50%", markpoint_opts=opts.MarkPointOpts(), is_selected=True)
        .set_series_opts(itemstyle_opts={
        "normal": {
            "color": JsCode("""new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                    offset: 0,
                    color: 'rgba(0, 244, 255, 1)'
                }, {
                    offset: 1,
                    color: 'rgba(0, 77, 167, 1)'
                }], false)"""),
            "barBorderRadius": [6, 6, 6, 6],
            "shadowColor": 'rgb(0, 160, 221)',
        }}
    )
        .set_global_opts(title_opts=opts.TitleOpts(title="工资区间各数量一览"),
                         yaxis_opts=opts.AxisOpts(position="right", name="Y轴", is_show=False),
                         )

)
c.render('folder/salaryRange_num_bar.html')
