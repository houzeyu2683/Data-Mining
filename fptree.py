
import enum


class Data:

    def __init__(self, path):

        self.path = path
        return

    def readDictionary(self):

        dictionary = {}
        with open(self.path, 'r') as paper:
        
            for line in paper.readlines():

                _, t, i = line.split()
                try: i = int(i) 
                except: i = str(i)
                pass

                if(dictionary.get(t)): dictionary[t].add(i)
                else: dictionary[t] = {i}
                continue
        
            pass
        
        self.length = len(dictionary.keys())
        self.dictionary = dictionary
        return
    
    pass

def processDictionary(dictionary=None, threshold=2):

    item, count = [], []
    loop = set.union(*dictionary.values())
    length = 0
    for k in loop:

        c = sum([k in v for v in dictionary.values()])
        if(c>=threshold):

            count += [c]
            item += [{k}]
            length += 1
            pass
                
        continue
        
    index = range(length)
    order = sorted(index, key=lambda k: count[k], reverse = True)
    item = ['root'] + [list(item[o])[0] for o in order]
    count = [None] + [count[o] for o in order]
    head = {"item":item, "count":count}
    pass

    sequence = {}
    for key, v in dictionary.items():

        v = list(v)
        chain = []
        for i in head['item']: 

            if(i in v): chain += [i]
            continue

        sequence[key] = chain
        continue
    
    head["item"]
    # head["item"].reverse()
    # head['count'].reverse()
    return(sequence, head)

class Node:

    def __init__(self, count=0, name="", children={}, father=None, status=0):

        self.count = count
        self.name = name
        self.children = children
        self.father = father
        self.status = status
        return

    def trackPath(self):

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

class Plant:

    def __init__(self, sequence, head, threshold=300):

        self.sequence = sequence
        self.head = head
        self.threshold = threshold
        return

    def build(self):

        # print('create tree')
        self.createTree()
        # print('create link')
        self.createLink(node=self.tree, root=True)
        return

    def createTree(self):

        sequence = self.sequence
        tree = Node(count=None, name='root', children={}, father=None, status=0)
        for row in sequence:
            
            branch = tree
            for name in sequence[row]:
                
                if(branch.children.get(name)): branch.children.get(name).count += 1
                else: branch.children[name] = Node(count=1, name=name, children={}, father=branch, status=0)
                branch = branch.children[name]
                continue
            
            continue
        
        self.tree = tree
        return

    ##  Tree node link.
    def createLink(self, node, root=True):

        if(root): self.link = {}
        if(node.children!={}):
            
            for (_, item) in node.children.items():

                exist = self.link.get(item.name)
                if(not exist): self.link[item.name] = []
                self.link[item.name] += [item]
                pass
                
                self.createLink(node=item, root=False)
                continue

            pass

        return

    def cutNode(self, node):

        link = self.link
        threshold = self.threshold
        chain = []
        for n in link[node]: 

            n.trackPath()
            del n.trace[0]
            del n.trace[-1]
            chain += [{i.name for i in n.trace} for _ in range(n.count)]
            continue

        dictionary = {k:v for k,v in enumerate(chain)}
        sequence, head = processDictionary(dictionary=dictionary, threshold=threshold)
        stop = True if(len(head['item'])==1) else False
        return(sequence, head, stop)

    pass

condition = ['14']
head = {'item': ['root', 18, 34, 30, 19, 6, 1, 16, 48, 32, 26, 4, 49, 44, 46, 12, 28, 42, 39, 21, 15, 0, 11, 29, 2, 20, 38, 3, 37, 5, 35, 24, 43, 41, 47, 33, 31, 13, 10, 23, 8], 'count': [None, 2113, 1920, 1688, 1617, 1581, 1558, 1538, 1435, 1237, 1236, 1189, 1165, 1118, 1116, 1095, 1026, 951, 947, 919, 915, 852, 845, 840, 817, 811, 806, 714, 698, 680, 664, 637, 623, 620, 618, 506, 496, 445, 422, 382, 344]}

def getTerm(head, condition=[]):

    assert condition!=[], 'need condition'
    term = []
    for i,c in zip(head['item'][1:], head['count'][1:]):

        l = [i] + condition
        term += [{",".join([str(k) for k in l]): c}]
        continue

    return(term)


d = Data(path='./inputs/2022-DM-release-testdata-2.data')
d.readDictionary()
threshold=200
sequence, head = processDictionary(dictionary=d.dictionary, threshold=threshold)
condition=[]
frequency=[]
plant = Plant(sequence=sequence, head=head, threshold=threshold)
plant.build()

def matchPattern(head, condition):

    pattern = []
    given = ",".join([str(i) for i in condition])
    for _, (item, count) in enumerate(zip(reversed(head['item']), reversed(head['count']))):

        if(item=='root'): break
        else: pattern += [{",".join([str(item), given]): count}]
        
    return(pattern)

def mineTree(sequence, head, threshold, condition=[], frequency=[]):

    plant = Plant(sequence=sequence, head=head, threshold=threshold)
    plant.build()
    sequence, head, stop = plant.cutNode(node=condition[-1])
    if(stop): return(frequency)
    # print(stop)
    pattern = matchPattern(head, condition)
    # if(pattern!=[]): print(pattern)
    frequency += [pattern]
    # print(head)
    for _, (item, _) in enumerate(zip(reversed(head['item']), reversed(head['count']))):
        
        if(item=='root'): return(frequency)
        conditionNext = condition.copy() + [item].copy()
        mineTree(sequence, head, threshold, condition=conditionNext, frequency=frequency)
        continue

    pass

frequency = []
# item = 14
for _, (item, _) in enumerate(zip(reversed(head['item']), reversed(head['count']))):

    if(item=='root'):break
    condition = [item]
    pattern = mineTree(sequence, head, threshold, condition=condition, frequency=[])
    frequency += pattern

    continue

[i for i in frequency[1:10]]
# condition=[] 代表第一個大樹沒有

frequency = sum(frequency, [])
count = {}
for f in frequency:

    count.update(f)
    continue

count['14,41']  458
count['14,41,34']  316
14    2148
34    1920


d.length 2997



