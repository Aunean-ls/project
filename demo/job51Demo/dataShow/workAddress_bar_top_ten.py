from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.commons.utils import JsCode
import pandas as pd
from pyecharts.globals import ThemeType

df = pd.read_csv('../data/workAddress_num.csv', encoding='utf-8')
# print(df)

v0 = df['工作地点'].values.tolist()
print(v0)
v1 = df['招聘数量'].values.astype(int).tolist()
print(v1)


c = (
    Bar({"theme": ThemeType.MACARONS})
    .add_xaxis(v0)
    .add_yaxis("", v1, category_gap="50%")  # category_gap 柱宽（之间的相隔距离
    .set_series_opts(
        itemstyle_opts={
            "normal": {
                "color": JsCode(
                    """new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                offset: 0,
                color: 'rgba(0, 244, 255, 1)'
            }, {
                offset: 1,
                color: 'rgba(0, 77, 167, 1)'
            }], false)"""
                ),
                "barBorderRadius": [30, 30, 30, 30],
                "shadowColor": "rgb(0, 160, 221)",
            }
        }
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="招聘数量前十五的城市"),
        datazoom_opts=opts.DataZoomOpts(type_="inside"),
        yaxis_opts=opts.AxisOpts(name="数量/个"),
        xaxis_opts=opts.AxisOpts(name="城市"),
    )

)

c.render('folder/workAddress_bar_top_ten.html')

