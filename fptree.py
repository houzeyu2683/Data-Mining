
def updateSoil(link, node, support):

    sequence = []
    for l in link[node]:
    
        l.createTrace()
        # [n.name for n in l.trace]
        r = [n.name for n in l.trace[1:-1]]
        b = [r] * l.count
        sequence += b
        continue
    
    sequence = orderSequence(sequence, support, increasing=False)
    soil = Soil(sequence=sequence, support=support)
    soil.createTree()
    soil.createLink(soil.tree, link={})
    return(soil)

def cutSoil(link, condition, support):

    condition = condition.split(',')
    for c in condition:

        soil = updateSoil(link, c, support)
        if(soil.link==[]): break
        link = soil.link
        continue
    
    return(soil)

class Soil:

    def __init__(self, sequence, support=300):

        self.sequence = sequence
        self.support = support
        return

    def createTree(self):

        sequence = self.sequence
        # tree = Node(count=None, name='root', children={}, father=None, status=0)
        tree = Node(count=None, name='root', children={}, father=None)
        for row in sequence:

            branch = tree
            for name in row:

                if(branch.children.get(name)): branch.children[name].count += 1
                # else: branch.children[name] = Node(count=1, name=name, children={}, father=branch, status=0)
                else: branch.children[name] = Node(count=1, name=name, children={}, father=branch)
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

    def getHead(self):

        head = getHead(self.sequence, self.support, False)
        return(head)

    pass

def getPattern(link=None, condition='', support=None):
    
    loop = sum(link.values(), [])
    pattern = {}
    for node in loop:
        
        # name = ','.join(condition+[node.name])
        if(condition==''): name = ','.join([node.name])
        else: name = ','.join([condition]+[node.name])
        if(pattern.get(name)): pattern[name] += node.count
        else: pattern[name] = node.count
        continue
    
    if(support):

        pattern = {k:v for k, v in pattern.items() if(v>=support)}
        pass

    return(pattern)

class Node:

    # def __init__(self, count=0, name="", children={}, father=None, status=0):
    def __init__(self, count=0, name="", children={}, father=None):

        self.count = count
        self.name = name
        self.children = children
        self.father = father
        # self.status = status
        return

    def createTrace(self):

        # count = sum([n.count for n in self.children.values()])
        if(self.father):  
            
            # self.count -= count    
            trace = [self]
            item = self.father
            while(item):
                
                # if(item.name!='root'): item.count -= count    
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
            
            _, t, i = line.split()
            i = str(i)
            if(dictionary.get(t)): dictionary[t].add(i)
            else: dictionary[t] = {i}
            continue
    
        pass
    
    number = list(dictionary.keys())
    sequence = [list(v) for v in dictionary.values()]
    table = [number, sequence]
    return(table)

def getHead(sequence, support=None, increasing=True):

    chain = sum(sequence, [])
    pass

    item  = list(set(chain))
    size  = len(item)
    count = [chain.count(n) for n in item]
    pass

    order = sorted(range(size), key=lambda k: count[k], reverse = not increasing)
    item = [item[o] for o in order]        
    count = [count[o] for o in order]        
    head = [item, count]

    if(support):
        
        item, count = [], []
        for i, c in zip(head[0], head[1]):

            if(c>=support):

                item += [i]
                count += [c]
                pass

            continue

        head = [item, count]
        pass

    return(head)

def orderSequence(sequence, support=None, increasing=False):

    head = getHead(sequence, support, increasing)
    pass

    q = []
    h, _ = head
    for s in sequence: q += [[i for i in h if(i in s)]]
    pass

    sequence = q
    return(sequence)

def runFptree(data_path, sup_min, conf_min):

    # data_path = './inputs/2022-DM-release-testdata-2.data'
    # data_path = './inputs/test_data_sample.txt'
    number, sequence = readTable(data_path)
    support=int(len(number)*sup_min)

    head = getHead(sequence, support, increasing=False)
    sequence = orderSequence(sequence=sequence, support=support, increasing=False)

    term = {}

    ##  1-term
    soil = Soil(sequence, support)
    soil.createTree()
    soil.createLink(soil.tree, link={})
    term.update(getPattern(soil.link, ''))

    ##  2-term
    queue = list(reversed(head[0]))
    pattern = {}
    for q in queue: 
        
        s = cutSoil(soil.link, q, support)
        p = getPattern(s.link, q, support)
        pattern.update(p)
        term.update(p)
        continue

    ##  other-term
    while(pattern!={}):

        c = {}
        for q in list(pattern.keys()):

            s = cutSoil(soil.link, q, support)
            p = getPattern(s.link, q, support)
            c.update(p)
            term.update(p)
            continue
        
        pattern = c
        pass
    
    item, count = [], []
    for k,v in term.items():

        item += [k]
        count += [round(v/len(number),3)]
        continue
    
    result ={'item':item, "count":count}
    return(result)

def writeSupport(result, path):

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

def getRule(result, confidence):
    
    rule = []
    score = []
    for i, c in zip(result['item'], result['count']):

        l = len(i.split(','))
        if(l==1): continue
        else:
            
            for j, d in zip(result['item'], result['count']):
                
                left = set(sorted(i.split(',')))
                right = set(sorted(j.split(',')))
                union = set.union(left, right)
                if(union==right and left!=right):

                    a = left
                    b = set.difference(right, left)
                    if(round(d/c, 3)>=confidence):

                        rule += ["{} -> {}".format(a, b)]
                        score += [round(d/c, 3)]
                        pass

                    pass

                continue                        

            pass

        continue
    
    print('confidence item: {}'.format(len(rule)))
    output = rule, score
    return(output)

# title=['freqset', 'support']
def writeConfidence(rule, path):

    # zip(rule[0], rule[1])
    # iteration = list(result.values())
    with open(path, 'w') as paper:
            	
        title = ['A -> B', 'confidence']
        line = ','.join(title) + '\n'
        paper.write(line)
        for k, v in zip(rule[0], rule[1]):
                
            line = ','.join([k.replace(',', ""), str(v)]) + '\n'
            paper.write(line)
            continue

        pass

    return