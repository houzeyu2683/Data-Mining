
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

def getTerm(head, condition=[]):

    assert condition!=[], 'need condition'
    term = []
    for i,c in zip(head['item'][1:], head['count'][1:]):

        l = [i] + condition
        term += [{",".join([str(k) for k in l]): c}]
        continue

    return(term)

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

class Engine:

    def __init__(self, path, support=200, confidence=200):

        self.path = path
        self.support = support
        self.confidence = confidence
        return
    
    def scan(self):

        data = Data(path=self.path)
        data.readDictionary()
        self.length = data.length ## = =!
        sequence, head = processDictionary(dictionary=data.dictionary, threshold=self.support)
        condition = []
        frequency = []
        plant = Plant(sequence=sequence, head=head, threshold=self.support)
        plant.build()
        for _, (item, _) in enumerate(zip(reversed(head['item']), reversed(head['count']))):

            if(item=='root'):break
            condition = [item]
            pattern = mineTree(sequence, head, self.support, condition=condition, frequency=[])
            frequency += pattern
            continue

        frequency = sum(frequency, [])
        count = {'item':[], 'frequency':[]}
        for i in frequency:

            count['item'] += [set([int(i) for i in list(i.keys())[0].split(',')])]
            count['frequency'] += [list(i.values())[0]]
            continue

        f = count['frequency']
        l = range(len(f))
        s = sorted(l, key=lambda k: f[k])
        c = {'item':[count['item'][i] for i in s], 'frequency':[count['frequency'][i] for i in s]}
        self.count = c
        return

    pass


# frequency = sum(frequency, [])
# frequency



# count = {}
# for f in frequency:

#     count.update(f)
#     continue

# count['14,41']  458
# count['14,41,34']  316
# 14    2148
# 34    1920


# d.length 2997



