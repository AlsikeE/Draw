import json
import os
from drawBar import  *
def readfile(path):
    with open(path,'r') as load_f:
        load_dict = json.load(load_f)

    return load_dict['nodes'],load_dict['links']



def trans_in_node(item):
    node = {}
    node['datacenter'] =  item['datacenter']
    node['name'] = item['name']
    node['cost'] = item['pes'] * item['mips']
    node['queuesize'] =  item['queuesize']
    return node

def ana_nodes(nodes):
    nodeResult = list(map(trans_in_node, nodes))
    # print (nodeResult)
    return nodeResult


def ana_links(nodes,links):
    result = {}
    inter_result = 0
    for item in links:
        # print(item['name'])
        src_node = {}
        dst_node = {}
        try:
            src_node = list(filter(lambda x:x['name'] == item['source'], nodes))[0]
        except:
            print('no such node')

        try:
            dst_node = list(filter(lambda x: x['name'] == item['destination'], nodes))[0]
        except:
            print('no such node')

        if (dst_node['datacenter'] == src_node['datacenter']):
            if(src_node['type'] == 'Ingress' and dst_node['type'] == 'Egress'):
                pass

            else:
                dc = dst_node['datacenter']
                # print(dc)
                try:
                    result[dc] += item['bandwidth']
                except KeyError:
                    result[dc] = item['bandwidth']
        else:
            inter_result += item['bandwidth']


    result['inter'] = inter_result


    # print(result)
    return result


def cal_node_cost(nodes):
    costs = {}
    for item in nodes:
        # print(item)
        dc = item['datacenter']
        try:
            costs[dc] += item['cost']
        except KeyError:
            costs[dc] = item['cost']
    return costs


def main_draw_pics_calculate_from_topo(scenario_dir,no,output_dir):
    i = 1
    paths = []
    while (i < 7):
        paths.append(scenario_dir + '\Scenario'+ str(no) + '-' + str(i) +'\\virtualTopology.json')
        i += 1
    dc1_costs = []
    dc2_costs = []
    net_costs = []
    # print(paths)
    for p in paths:
        nodes, links = readfile(p)
        nodes_ = ana_nodes(nodes)
        cpu_costs = cal_node_cost(nodes_)
        net_cost = ana_links(nodes, links)['inter']
        dc1_costs.append(cpu_costs['DC1'])
        dc2_costs.append(cpu_costs['DC2'])
        net_costs.append(net_cost)

    # print(dc1_costs)
    # print(dc2_costs)
    # print(net_costs)

    x = ["S1-1", "S1-2", "S1-3", "S1-4", "S1-5", "S1-6"]

    if (os.path.isdir(output_dir)):
        pass
    else:
        os.makedirs(output_dir)
    drawInOne(x, dc1_costs, dc2_costs,output_dir + '//CPUResource.pdf') #堆叠图
    drawBar(x, net_costs, 'WAN BandWidth Consumption(KB/s)', output_dir + '//WANBandwidth.pdf') #柱状图

if __name__ == '__main__':
    main_draw_pics_calculate_from_topo('D:\AlsikeE\code\Test2\S1', 1, 'test')
    # paths = ['D:\AlsikeE\code\Test2\Scenario1-1\\virtualTopology.json',
    #          'D:\AlsikeE\code\Test2\Scenario1-2\\virtualTopology.json',
    #          'D:\AlsikeE\code\Test2\Scenario1-3\\virtualTopology.json',
    #          'D:\AlsikeE\code\Test2\Scenario1-4\\virtualTopology.json',
    #          'D:\AlsikeE\code\Test2\Scenario1-5\\virtualTopology.json',
    #          'D:\AlsikeE\code\Test2\Scenario1-6\\virtualTopology.json']
    # dc1_costs = []
    # dc2_costs = []
    # net_costs = []
    # for p in paths:
    #     nodes, links = readfile(p)
    #     nodes_ = ana_nodes(nodes)
    #     cpu_costs = cal_node_cost(nodes_)
    #     net_cost = ana_links(nodes,links)['inter']
    #     dc1_costs.append(cpu_costs['DC1'])
    #     dc2_costs.append(cpu_costs['DC2'])
    #     net_costs.append(net_cost)
    #
    # print(dc1_costs)
    # print(dc2_costs)
    # print(net_costs)
    #
    # x = ["S1-1", "S1-2", "S1-3", "S1-4", "S1-5", "S1-6"]
    # drawInOne(x,dc1_costs,dc2_costs,'cpucost.pdf')
    # drawBar(x,net_costs,'BW cost','bwcost.pdf')
    # # nodes, links = readfile(path)
    # # result1 = ana_nodes(nodes)  #nodes里得到的结果
    # # result2 = ana_links(nodes,links)#links里得到的结果
    #
    # # print(result1)
    # # print(result2)
