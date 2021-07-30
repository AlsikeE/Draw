import os
from drawBar import *
def get_files_name(dirname):
    return  (os.listdir(dirname))


def get_csv_files(csv_dir):
    for root, dirs, files in os.walk(csv_dir):
        pass
    return files


def main_draw_average(dirname,output_dir):
    methods = get_files_name(dirname)
    avgCPU = []
    avgNet = []
    for m in methods:
        # 'D:\AlsikeE\code\Test2\S1\Scenario1-1\results\Scenario1-1\workloads'
        csv_dir = dirname + '\\' + m + '\\results\\' + m + '\\workloads'
        csv_files = get_csv_files(csv_dir)
        cpu = 0
        net = 0
        for f in csv_files:
            p = csv_dir + '\\' + f
            c, n = readAverageFile(p)
            cpu += c
            net += n
        ca, na = cpu / 20, net / 20
        avgCPU.append(ca)
        avgNet.append(na)

    x = ["S1-1", "S1-2", "S1-3", "S1-4", "S1-5", "S1-6"]

    if (os.path.isdir(output_dir)):
        pass
    else:
        os.makedirs(output_dir)

    drawBar(x, avgCPU, yname='Average Computation Time (s)', filename=output_dir + '//AverageComputation.pdf')  # 平均柱状图，相当于堆叠图
    drawBar(x, avgNet, yname='Average Transmission Time (s)', filename=output_dir + '//AverageTransmission.pdf')  # 平均柱状图


if __name__ == '__main__':
    dirname = 'D:\AlsikeE\code\Test2\S1'
    main_draw_average(dirname,'test')

    # methods = get_files_name(dirname)
    # avgCPU = []
    # avgNet = []
    # for m in methods:
    #     # 'D:\AlsikeE\code\Test2\S1\Scenario1-1\results\Scenario1-1\workloads'
    #     csv_dir = dirname + '\\' + m  + '\\results\\' + m + '\\workloads'
    #     csv_files = get_csv_files(csv_dir)
    #     cpu = 0
    #     net = 0
    #     for f in csv_files:
    #         p = csv_dir + '\\' + f
    #         c,n = readAverageFile(p)
    #         cpu += c
    #         net += n
    #     ca,na = cpu/20, net/20
    #     avgCPU.append(ca)
    #     avgNet.append(na)
    #
    # x = ["S1-1", "S1-2", "S1-3", "S1-4", "S1-5", "S1-6"]
    # drawBar(x,avgCPU,yname='average service time / seconds',filename='averageservicetime.pdf')#平均柱状图，相当于堆叠图
    # drawBar(x,avgNet,yname='average network time / seconds',filename='averagenetworktime.pdf')#平均柱状图

