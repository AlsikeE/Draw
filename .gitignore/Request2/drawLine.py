import pandas as pd

import matplotlib.pyplot as plt
from  pyecharts.charts import  Line,Bar
import pyecharts.options as opts
plt.rcParams['font.sans-serif'] = ['KaiTi', 'SimHei', 'FangSong']  # 汉字字体,优先使用楷体，如果找不到楷体，则使用黑体
plt.rcParams['font.size'] = 12  # 字体大小
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号

import numpy as np
import json,codecs

def readCsv (path):
    df = pd.read_csv(path, delimiter='\t',header=None)[2:-21]
    df_list = df.values.tolist()
    result = []

    for s in df_list:
        # print(s)
        a = s[0].split(',')
        pair = {}
        pair['submitTime'] = int(a[3])
        pair['responseTime'] = float(a[-2])#-2是因为最后还有个,
        result.append(pair)
    result.sort(key=lambda x:x['submitTime'])
    # print(result)
    submitTime = list(map(lambda x: x['submitTime'],result))
    responseTime = list(map(lambda x: x['responseTime'], result))
    # print(submitTime)
    # print(responseTime)
    return submitTime,responseTime

def _draw_one_line(x,y,marker,mec,mfc,l):
    plt.plot(x, y,mec=mec, mfc=mfc, label=l,linewidth=2.0)

def drawLine(x,ys):
    # plt.plot(x, y1, 'o', 'r', 'w', l = u'test')
    _draw_one_line(x,ys[0],'o','r','w',u'1-1')
    _draw_one_line(x, ys[1], 'o', 'r', 'w', u'1-2')
    _draw_one_line(x, ys[2], 'o', 'r', 'w', u'1-3')
    _draw_one_line(x, ys[3], 'o', 'r', 'w', u'1-4')
    _draw_one_line(x, ys[4], 'o', 'r', 'w', u'1-5')
    _draw_one_line(x, ys[5], 'o', 'r', 'w', u'1-6')
    plt.plot()
    plt.legend()
    plt.xlabel('submitTime/seconds')
    plt.ylabel('responseTime/seconds')
    plt.savefig('responseTime')
    plt.show()


# def drawLineEcharts(x,y1,y2):
#     line = Line()
#     line.add_xaxis(x)
#     line.add_yaxis('1-5',y1,label_opts=opts.LabelOpts(is_show=False))
#     line.add_yaxis('1-2',y2,label_opts=opts.LabelOpts(is_show=False))
#     line.set_global_opts(
#         xaxis_opts=opts.AxisOpts(name="submitTime"),
#         yaxis_opts=opts.AxisOpts(name= "responseTime")
#     )
#     line.render()

if __name__ == '__main__':
    paths = [
        'D:\AlsikeE\code\Test2\Scenario1-1\\results\Scenario1-1\workloads\\[29-13_57_40]result_workloads_chain1.csv',
        'D:\AlsikeE\code\Test2\Scenario1-2\\results\Scenario1-2\workloads\\[29-14_26_45]result_workloads_chain1.csv',
        'D:\AlsikeE\code\Test2\Scenario1-3\\results\Scenario1-3\workloads\\[29-14_31_44]result_workloads_chain1.csv',
        'D:\AlsikeE\code\Test2\Scenario1-4\\results\Scenario1-4\workloads\\[29-14_33_12]result_workloads_chain1.csv',
        'D:\AlsikeE\code\Test2\Scenario1-5\\results\Scenario1-5\workloads\\[29-14_34_04]result_workloads_chain1.csv',
        'D:\AlsikeE\code\Test2\Scenario1-6\\results\Scenario1-6\workloads\\[29-14_34_39]result_workloads_chain1.csv'
    ]
    path1,path2,path3,path4,path5,path6 = paths
    x = []
    ys = []
    for p in paths:
        a,y = readCsv(p)
        x = a
        ys.append(y)
    # x,y1 = readCsv(path1)
    # x2,y2 = readCsv(path2)
    drawLine(x,ys)
    # drawLineEcharts(x,y1,y2)