import json
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
    print (nodeResult)
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
                print(dc)
                try:
                    result[dc] += item['bandwidth']
                except KeyError:
                    result[dc] = item['bandwidth']
        else:
            inter_result += item['bandwidth']


    result['inter'] = inter_result


    print(result)
    return result


def cal_node_cost(nodes):
    costs = {}
    for item in nodes:
        print(item)
        dc = item['datacenter']
        try:
            costs[dc] += item['cost']
        except KeyError:
            costs[dc] = item['cost']
    return costs

if __name__ == '__main__':
    paths = ['D:\AlsikeE\code\Test2\Scenario1-1\\virtualTopology.json',
             'D:\AlsikeE\code\Test2\Scenario1-2\\virtualTopology.json',
             'D:\AlsikeE\code\Test2\Scenario1-3\\virtualTopology.json',
             'D:\AlsikeE\code\Test2\Scenario1-4\\virtualTopology.json',
             'D:\AlsikeE\code\Test2\Scenario1-5\\virtualTopology.json',
             'D:\AlsikeE\code\Test2\Scenario1-6\\virtualTopology.json']
    dc1_costs = []
    dc2_costs = []
    net_costs = []
    for p in paths:
        nodes, links = readfile(p)
        nodes_ = ana_nodes(nodes)
        cpu_costs = cal_node_cost(nodes_)
        net_cost = ana_links(nodes,links)['inter']
        dc1_costs.append(cpu_costs['DC1'])
        dc2_costs.append(cpu_costs['DC2'])
        net_costs.append(net_cost)

    print(dc1_costs)
    print(dc2_costs)
    print(net_costs)

    x = ["1-1", "1-2", "1-3", "1-4", "1-5", "1-6"]
    drawInOne(x,dc1_costs,dc2_costs)
    drawBar(x,net_costs,'BW cost')
    # nodes, links = readfile(path)
    # result1 = ana_nodes(nodes)  #nodes里得到的结果
    # result2 = ana_links(nodes,links)#links里得到的结果

    # print(result1)
    # print(result2)