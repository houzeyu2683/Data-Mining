
class Soil:

    def __init__(self, sequence, head, support=300):

        self.sequence = sequence
        self.head = head
        self.support = support
        return

    # def build(self):

    #     # print('create tree')
    #     self.createTree()
    #     # print('create link')
    #     self.createLink(node=self.tree, root=True)
    #     return

    def createTree(self):

        sequence = self.sequence
        tree = Node(count=None, name='root', children={}, father=None, status=0)
        for row in sequence:
            
            branch = tree
            for name in row:
                
                if(branch.children.get(name)): branch.children.get(name).count += 1
                else: branch.children[name] = Node(count=1, name=name, children={}, father=branch, status=0)
                branch = branch.children[name]
                continue
            
            continue
        
        self.tree = tree
        return

    ##  Tree node link.
    def createLink(self, root=None, link={}):

        # if(root): self.link = {}
        # self.link = link
        if(root.children!={}):
            
            for (_, node) in root.children.items():

                exist = link.get(node.name)
                if(not exist): link[node.name] = []
                link[node.name] += [node]
                pass
                
                self.createLink(root=node, link=link)
                continue

            pass
        
        self.link = link
        return

    # def cutNode(self, node):

    #     link = self.link
    #     threshold = self.threshold
    #     chain = []
    #     for n in link[node]: 

    #         n.trackPath()
    #         del n.trace[0]
    #         del n.trace[-1]
    #         chain += [{i.name for i in n.trace} for _ in range(n.count)]
    #         continue

    #     dictionary = {k:v for k,v in enumerate(chain)}
    #     sequence, head = processDictionary(dictionary=dictionary, threshold=threshold)
    #     stop = True if(len(head['item'])==1) else False
    #     return(sequence, head, stop)

    pass

class Node:

    def __init__(self, count=0, name="", children={}, father=None, status=0):

        self.count = count
        self.name = name
        self.children = children
        self.father = father
        self.status = status
        return

    def createTrace(self):

        if(self.father):  
            
            trace = [self]
            item = self.father
            while(item):
                
                trace += [item]
                item = item.father
                pass
            
            trace.reverse()
            self.trace = trace
            return

        self.trace = None
        return

    pass

def readTable(path):

    dictionary = {}
    with open(path, 'r') as paper:
    
        for line in paper.readlines():
            # print(line)
            _, t, i = line.split()
            # try: i = int(i) 
            # except: i = str(i)
            i = str(i)
            if(dictionary.get(t)): dictionary[t].add(i)
            else: dictionary[t] = {i}
            continue
    
        pass
    
    table = {
        "number":list(dictionary.keys()), 
        "item":[list(v) for v in dictionary.values()]
    }
    return(table)

def getHead(table):

    chain = sum(table['item'], [])
    name = list(set(chain))
    value = [chain.count(n) for n in name]
    pass

    index = range(len(name))
    order = sorted(index, key=lambda k: value[k], reverse = True)
    unit = [name[o] for o in order]        
    value = [value[o] for o in order]        
    head = {'unit':unit, 'value':value}
    return(head)

def updateHead(head, support):

    loop = zip(head['unit'], head['value'])
    unit = []
    value = []
    for u, v in loop:

        if(v>=support): 

            unit += [u]
            value += [v]
            pass

        continue

    head = {'unit':unit, 'value':value}
    return(head)

def sortSequence(table, head):

    sequence = []
    h = head['unit']
    t = table['item']
    for s in t: sequence += [[i for i in h if(i in s)]]
    return(sequence)

def getBucket(link, support):

    sequence = []
    for l in link:

        l.createTrace()
        # [n.name for n in l.trace]
        r = [n.name for n in l.trace[1:-1]]
        b = [r] * l.count
        sequence += b
        continue
    
    table = {'item':sequence}
    head = updateHead(getHead(table), support)
    sequence = sortSequence(table, head)
    bucket = Soil(sequence=sequence, head=head, support=support)
    bucket.createTree()
    bucket.createLink(root=bucket.tree, link={})
    return(bucket)

def getCount(head):

    loop = zip(head['unit'], head['value'])
    count = {u:v for u, v in loop}
    return(count)

def mineBucket(bucket, support, condition=[], term={}):

    head = bucket.head.copy()
    link = bucket.link.copy()
    loop = zip(reversed(head['unit']), reversed(head['value']))
    for unit, _ in loop:
        
        if(unit==[]): return(term)
        bucket = getBucket(link=link[unit], support=support)
        if(bucket.link=={}): continue 
        else: 
            
            condition = condition + [unit]
            c = ','.join(condition)
            term = {','.join([c,k]):v for k, v in getCount(bucket.head).items()}
            mineBucket(bucket, support, condition, term)
            pass

        continue

    return(term)

def getSupport(summary, length):

    item = []
    count = []
    for i, c in summary.items():

        item += [i]
        count += [round(c/length, 3)]
        continue

    frequency = {'item':item, 'count':count}
    return(frequency)    


def runFptree(data_path, sup_min, conf_min):

    table = readTable(path=data_path)
    head = getHead(table)
    pass

    ##  common setting
    length = len(table['number'])
    support = int(sup_min * length)
    confidence = int(conf_min * length)  ## not use...'..'
    summary = {}
    pass

    head = updateHead(head, support=support)
    summary.update(getCount(head))
    sequence = sortSequence(table, head)
    soil = Soil(sequence=sequence, head=head, support=support)
    soil.createTree()
    soil.createLink(root=soil.tree, link={})

    term = {}
    head = head.copy()
    link = soil.link.copy()
    loop = zip(reversed(head['unit']), reversed(head['value']))
    for unit, _ in loop:

        link = soil.link[unit]
        bucket = getBucket(link=link, support=support)
        if(bucket.link=={}): continue 
        else: 

            condition = [] + [unit]
            c = ','.join(condition)
            term.update({','.join([c,k]):v for k, v in getCount(bucket.head).items()})
            term.update(mineBucket(bucket, support, condition, term))
            pass

        continue
    
    summary.update(term)
    output = getSupport(summary, length)
    return(output)

def writeResult(result, path):

    iteration = list(result.values())
    with open(path, 'w') as paper:
            	
        title = ['freqset', 'support']
        line = ','.join(title) + '\n'
        paper.write(line)
        for i in zip(*iteration):
                
            k = "{" + i[0].replace(",", " ") + "}"
            line = ','.join([k, str(i[1])]) + "\n"
            paper.write(line)
            continue

        pass

    return

'''
import time
DATA_PATH = './inputs/2022-DM-release-testdata-2.data'
SUP_MIN = 0.3
CONF_MIN = 0.3

OUT_PATH = './outputs/2022-DM-release-testdata-2.data_fptree.csv'
start_time = time.time()
result = runFptree(data_path=DATA_PATH, sup_min=SUP_MIN, conf_min=CONF_MIN)
print(len(result['item']))
finish_time = time.time()
print("{} sec".format(round(finish_time - start_time, 2)))
writeResult(result=result, path=OUT_PATH)
'''