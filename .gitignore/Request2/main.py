# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from fileProcess import  *
from anaDir import *
from drawLine import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dirname = 'D:\AlsikeE\code\Test2\S1' #文件夹的总夹
    output_dir = 'test'#输出文件夹
    sno = 1#第几个scenario
    main_draw_average(dirname, output_dir)#两个平均图
    main_draw_line(dirname, sno, output_dir)#响应时间折线图
    main_draw_pics_calculate_from_topo(dirname, sno, output_dir)#两个消耗图

