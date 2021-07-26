from pyecharts.charts import Page, Bar, Line, Grid, Pie, Map, WordCloud
import pyecharts.options as opts
from pyecharts.globals import ThemeType, SymbolType
from pyecharts.faker import Faker
from pyecharts.commons.utils import JsCode
import pandas as pd
import numpy as np
import random
from bs4 import BeautifulSoup


# https://mp.weixin.qq.com/s?__biz=MzI3ODM3MTU1Mw==&mid=2247483793&idx=1&sn=fd8d5c326741014e45c6ac932329bfcf&chksm=eb594c1fdc2ec5093c78ee6511a3bc0d33a55005b5998c4457390bbfd9094876c3ac26e80386&scene=21#wechat_redirect
def get_grid_1():
    # c = (Pie(init_opts=opts.InitOpts(chart_id=1, bg_color='#00589F'))
    #     .set_global_opts(
    #     title_opts=opts.TitleOpts(title="超市数据管理驾驶舱",
    #                               title_textstyle_opts=opts.TextStyleOpts(font_size=36, color='#FFFFFF'),
    #                               pos_left='center', pos_top='middle')))
    df = pd.read_csv('../data/salaryRange_num.csv', encoding='utf-8')
    v1 = df['数量'].values.tolist()
    # v1 = df['招聘数量'].values.astype(int).tolist()
    # print(v1)

    c = (
        Bar(init_opts=opts.InitOpts(
            animation_opts=opts.AnimationOpts(
                animation_delay=500, animation_easing="cubicOut"
            ),
            theme=ThemeType.MACARONS))
            .add_xaxis(["1-5", "5-10", "10-15", "15-25", "25-50", "50-100", "100-500"],)
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
                             xaxis_opts=opts.AxisOpts(name='千/月', axislabel_opts=opts.LabelOpts(rotate=-60)),
                             yaxis_opts=opts.AxisOpts(position="right", name="Y轴", is_show=False),
                             )
    )
    grid = Grid()
    grid.add(c, grid_opts=opts.GridOpts(pos_left='5%', width='80%'))
    return grid
    # return c


def get_grid_2():
    df = pd.read_csv('../data/workAddress_num_top5.csv', encoding='utf-8')

    v0 = df['工作地点'].values.tolist()
    v1 = df['招聘数量'].values.astype(int).tolist()

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
            title_opts=opts.TitleOpts(title="招聘数量前五的城市", title_textstyle_opts=opts.TextStyleOpts(
                font_size=20, color='blue'), pos_left='center'),
            # datazoom_opts=opts.DataZoomOpts(type_="inside"),
            yaxis_opts=opts.AxisOpts(name="数量/个", is_show=False),
            # xaxis_opts=opts.AxisOpts(name="城市", is_show=False, ),
        )

    )
    return c


def get_grid_3():
    df = pd.read_csv('../data/province_num.csv', encoding='utf-8')
    # print(df)
    v0 = df['省份'].values.tolist()
    v1 = df['数量'].values.astype(int).tolist()

    c = (
        Map()
            .add("", [list(z) for z in zip(v0, v1)], "china", is_map_symbol_show=False)
            .set_global_opts(
            title_opts=opts.TitleOpts(title="各省岗位分布", title_textstyle_opts=opts.TextStyleOpts(
                font_size=20, color='blue'), pos_left='center'),
            visualmap_opts=opts.VisualMapOpts(max_=2500),
        ).set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    )
    return c


def get_grid_4():
    df = pd.read_csv('../data/position_num_top5.csv', encoding='utf-8')

    v0 = df['岗位名称'].values
    v1 = df['招聘数量']

    pie = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.SHINE))
            .add(
            "",
            [list(z) for z in zip(v0, v1)],
            radius=["40%", "60%"],
            center=["45%", "53%"],
            # label_opts=opts.LabelOpts(is_show=False),
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="招聘数量前五占比", title_textstyle_opts=opts.TextStyleOpts(
                font_size=20, color='blue'), pos_left='center'),
            legend_opts=opts.LegendOpts(
                type_="scroll", pos_top="20%", pos_left="80%", orient="vertical", is_show=False
            ),
        )
            .set_series_opts(
            label_opts=opts.LabelOpts(formatter="{b}\r\n{d}%", font_size=9),
        )
    )
    return pie


def get_grid_5():
    df = pd.read_csv('../data/companyType_num.csv', encoding='utf-8')

    v0 = df['公司类型'].values
    v1 = df['数量']

    pie = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.SHINE))
            .add(
            "",
            [list(z) for z in zip(v0, v1)],
            radius=["40%", "55%"],
            center=["45%", "60%"],
            # label_opts=opts.LabelOpts(is_show=False),
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="各类公司类型占比",
                                      title_textstyle_opts=opts.TextStyleOpts(
                                          font_size=20, color='blue'), pos_left='center'
                                      ),
            legend_opts=opts.LegendOpts(
                type_="scroll", pos_top="20%", pos_left="85%", orient="vertical", is_show=False
            ),
        )
            .set_series_opts(
            label_opts=opts.LabelOpts(formatter="{b}:{d}%", font_size=10)
        )
    )
    return pie


def get_grid_6():
    df = pd.read_csv('../data/position_num_top5.csv', encoding='utf-8')

    v0 = df['岗位名称'].values.tolist()
    v1 = df['招聘数量'].values.astype(int).tolist()

    c = (
        Bar()
            .add_xaxis(v0)
            .add_yaxis("", v1, category_gap='50%', color='')
            .reversal_axis()
            .set_series_opts(itemstyle_opts={
            "normal": {
                "color": JsCode("""new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                offset: 0,
                                color: 'rgba(0, 244, 255, 1)'
                            }, {
                                offset: 1,
                                color: 'rgba(0, 77, 167, 1)'
                            }], false)"""),
                "barBorderRadius": [3, 3, 3, 3],
                # "shadowColor": 'rgb(0, 160, 221)',
            }}
        )
            .set_series_opts(label_opts=opts.LabelOpts(position="right"),)
            .set_global_opts(title_opts=opts.TitleOpts(title="招聘数量前五岗位",
                                                       title_textstyle_opts=opts.TextStyleOpts(
                                                           font_size=20, color='blue'), pos_left='center'
                                                       ),
                             yaxis_opts=opts.AxisOpts(name=''),
                             xaxis_opts=opts.AxisOpts(name="数量", max_=600, is_show=False),
                             )
    )
    grid = Grid()
    grid.add(c, grid_opts=opts.GridOpts(pos_left='35%', pos_bottom='20%'))
    return grid


def get_grid_7():
    df = pd.read_csv('../data/welfare_num.csv', encoding='utf-8')

    v0 = df['福利待遇'].values
    v1 = df['数量']

    data = list(zip(v0, v1))

    c = (
        WordCloud()
            .add(series_name="", data_pair=data, width='100%', height='100%', word_size_range=[10, 40])
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
    )
    return c


def get_page():
    grid1 = get_grid_1()
    grid2 = get_grid_2()
    grid3 = get_grid_3()
    grid4 = get_grid_4()
    grid5 = get_grid_5()
    grid6 = get_grid_6()
    grid7 = get_grid_7()
    page = (
        Page().add(grid1).add(grid2).add(grid3).add(grid4).add(grid5).add(grid6).add(grid7)
    )
    return page


with open("folder/my_first_pycharts.html", "r+", encoding='utf-8') as html:
    page = get_page()
    page.render('folder/my_first_pycharts.html')
    html_bf = BeautifulSoup(html, 'lxml')
    divs = html_bf.select('.chart-container')
    divs[0][
        'style'] = "width:26%;height:29%;position:absolute;top:10%;left:72.5%;border-style:solid;border-color:red;border-width:2px;"
    divs[1][
        'style'] = "width:26%;height:29%;position:absolute;top:10%;left:1%;border-style:solid;border-color:red;border-width:2px;"
    divs[2][
        'style'] = "width:44%;height:89%;position:absolute;top:10%;left:27.7%;border-style:solid;border-color:red;border-width:2px;"
    divs[3][
        'style'] = "width:26%;height:29%;position:absolute;top:40%;left:1%;border-style:solid;border-color:red;border-width:2px;"
    divs[4][
        'style'] = "width:26%;height:29%;position:absolute;top:40%;left:72.5%;border-style:solid;border-color:red;border-width:2px;"
    divs[5][
        'style'] = "width:26%;height:29%;position:absolute;top:70%;left:1%;border-style:solid;border-color:red;border-width:2px;"
    divs[6][
        'style'] = "width:26%;height:29%;position:absolute;top:70%;left:72.5%;border-style:solid;border-color:red;border-width:2px;"

    body = html_bf.find("body")
    body["style"] = "background-color:white;border:2px solid red;height:680px"  # 设置网页背景颜色
    div_title = "<div align='center' style='width:-1000px;'>\n<span style='font-size:34px;color:#000000'><b>招聘数据分析展示</b></div>"  # 修改页面背景色、追加标题
    body.insert(0, BeautifulSoup(div_title, "lxml").div)
    html_new = str(html_bf)
    html.seek(0, 0)
    html.truncate()
    html.write(html_new)
    html.close()
