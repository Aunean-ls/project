import pyecharts.options as opts
from pyecharts.charts import WordCloud
import pandas as pd
from pyecharts.globals import SymbolType

df = pd.read_csv('../data/welfare_num.csv', encoding='utf-8')
# print(df)

v0 = df['福利待遇'].values
print(v0)
v1 = df['数量']
print(v1)

data = list(zip(v0, v1))
print(data)


# c = (
#     WordCloud()
#     .add(series_name="热点分析", data_pair=data, word_size_range=[6, 66])
#     .set_global_opts(
#         title_opts=opts.TitleOpts(
#             title="", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
#         ),
#         tooltip_opts=opts.TooltipOpts(is_show=True),
#     )
# )
c = (
    WordCloud()
    .add("", data, word_size_range=[10, 100], shape=SymbolType.DIAMOND)
    # .set_global_opts(title_opts=opts.TitleOpts(title=""))
)
c.render("folder/welfare_wordCloud.html")

