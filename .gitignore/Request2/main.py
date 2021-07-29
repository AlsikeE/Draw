# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from fileProcess import  *


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    path = 'D:\AlsikeE\code\Test2\Scenario1-5\\virtualTopology.json'
    nodes, links = readfile(path)
    result1 = ana_nodes(nodes)  #nodes里得到的结果
    result2 = ana_links(nodes,links)#links里得到的结果

    print(result1)
    print(result2)
    # print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
