import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['KaiTi', 'SimHei', 'FangSong']  # 汉字字体,优先使用楷体，如果找不到楷体，则使用黑体
plt.rcParams['font.size'] = 12  # 字体大小
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号


def readAverageFile(path):
    f = open(path,'r')
    lines = f.readlines()
    compute = float(lines[-4].split(':')[1])
    network = float(lines[-3].split(':')[1])

    return compute,network



def drawBar(x,y,yname,filename):
    plt.bar(x,y)
    plt.xlabel('Method')
    plt.ylabel(yname)
    plt.savefig(filename,format='pdf')
    plt.show()

def drawInOne(x,dc1,dc2,filename):
    plt.bar(x=x,height=dc1,label='DC1',color='steelblue')
    plt.bar(x=x, height=dc2, label='DC2', color='indianred')
    plt.legend()
    plt.xlabel('Method')
    plt.ylabel('CPU Resource Consumption (MIPS)')
    plt.savefig(filename,format='pdf')
    plt.show()


# if __name__ == '__main__':
#     paths = ['D:\AlsikeE\code\Test2\Scenario1-2\\results\_abs_Scenario1-2\workloads\\[29-14_26_45]result_workloads_chain1.csv',
#              'D:\AlsikeE\code\Test2\Scenario1-1\\results\_abs_Scenario1-1\workloads\\[29-13_57_40]result_workloads_chain1.csv']
#     # path2 = 'D:\AlsikeE\code\Test2\Scenario1-2\\results\Scenario1-2\workloads\\[29-14_26_45]result_workloads_chain1.csv'
#     x = ["S1-1","1-2","1-3","1-4","1-5","1-6"]
#     cpus= []
#     nets = []
#     for p in paths:
#         c,n = readAverageFile(p)
#         cpus += (c)
#         nets += (n)
#     drawBar(x,cpus + [0] * (6-len(cpus)),'CPU cost')
#     drawBar(x,nets + [0] * (6-len(nets)),'Network cost')
#     drawInOne(x,cpus + [0] * (6-len(cpus)),nets + [0] * (6-len(nets)))


