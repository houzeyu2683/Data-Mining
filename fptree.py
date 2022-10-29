
class data:

    def __init__(self, path):

        self.path = path
        return

    def read(self):

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
        
        self.dictionary = dictionary
        return

    def prepare(self, threshold=2):

        dictionary = self.dictionary
        pass

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
        item = [list(item[o])[0] for o in order]
        count = [count[o] for o in order]
        header = {"item":item, "count":count}
        pass

        sequence = {}
        for key, v in dictionary.items():

            v = list(v)
            chain = []
            for i in header['item']: 

                if(i in v): chain += [i]
                continue

            sequence[key] = chain
            continue
            
        self.threshold = threshold
        self.header = header
        self.sequence = sequence
        return

    pass

class node:

    def __init__(self, count=0, name="", children={}, father=None):

        self.count = count
        self.name = name
        self.children = children
        self.father = father
        return

    def track(self):

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

class plant:

    # def __init__(self, table, connection = {}):
    def __init__(self, sequence):

        self.sequence = sequence
        # self.connection = connection        
        return

    def build(self):

        sequence = self.sequence
        tree = node(count=None, name='root', children={}, father=None)
        for row in sequence:
            
            branch = tree
            for name in sequence[row]:
                
                if(branch.children.get(name)): branch.children.get(name).count += 1
                else: branch.children[name] = node(count=1, name=name, children={}, father=branch)
                branch = branch.children[name]
                continue
            
            continue
        
        self.tree = tree
        self.connection = {}
        return

    def connect(self, tree):
        
        if(tree.children!={}):
            
            for (_, children) in tree.children.items():

                exist = self.connection.get(children.name)
                if(not exist): self.connection[children.name] = []
                # children.track()
                # right, left = children.trace[-1], children.trace[1:-1]
                # mate(right=right, left=left)
                self.connection[children.name] += [children]
                pass
                
                self.connect(tree=children)
                continue

            pass

        return

    def search(self, item):

        branch = []
        for b in self.connection.get(item):

            b.track()
            branch += [b.trace]
            continue
        
        return(branch)

    pass

# def mate(right, left, threshold):

#     group = {}
#     length = len(left)
#     pass

#     for e in range(length):
        
#         k = ",".join([n.name for n in left[:e+1]]) + ":" + right.name
#         v = right.count
#         if(group.get(k)): group[k] += v
#         else: group[k] = v
#         continue

#     for s in range(length-1):

#         k = ",".join([n.name for n in left[s+1:]]) + ":" + right.name
#         v = right.count
#         if(group.get(k)): group[k] += v
#         else: group[k] = v        
#         continue
    
#     # group = {k: v for k, v in group.items() if v >= threshold}
#     return(group)

d = data(path='./inputs/bit')
d.read()
d.prepare()
d.header
p = plant(sequence=d.sequence)
p.build()
p.connect(tree=p.tree)
p.connection
p.search(item='I3')

right = '1'
left = ['a', 'b', 'c', 'd', 'e']
class chain:

    def __init__(self, left='node8', right=['node1', 'node2', 'node3', 'node4', 'node5']):
        
        self.left = left
        self.right = right
        return

    def get(self, width=1):

        length = len(self.right)
        for index in range(length):

            ",".join([n.name for n in self.right[index:index+width]]) + ":" + self.left.name
            pass

        return

    pass



p.branch['I3'][0]
right = p.branch['I3'][0][-1]
left = p.branch['I3'][0][1:-1]



mate(right=right, left=left, threshold=1)

d.header
d.header['item'][-1]
nolist = p.connection['I4']
nolist[0].track()
= [n.name for n in nolist[0].trace]


# trans = data.read('./inputs/bit')
# head, trans_order = prepare(trans)
# tr = root(table=trans_order)
# tr.build()
# tr.connection
# tr.connect(tr.tree)

# def undefine(branchList, node):

#     #根據子樹根以及給定的node去計算彼此的頻率
#     return


[i.name for i in tr.connection['I5'][2].track()]

treeClass = tr.tree

nodeItem = nodeList[0]
itemChain = []
while(nodeItem.father):
    
    itemChain += [nodeItem.father]
    nodeItem = nodeItem.father
    pass

itemChain.reverse()
itemChain[0]

def trim(nodeList, treeClass):

    branch = []
    n = nodeList[0]
    n.father
    branch
    return


# head["item"][-1]
# head["count"][-1]
# tree = tr.tree
# tree

# h = head["item"][-1]
# n = tr.connection[h][0]
# n.father.father.father.name

# def prune(node, tree):

    
#     return(tree)


# # node = tr.tree.children['I2']
# # node.name

# # tr.tree.children['I2'].children['I1'].children['I4'].children
# # tr.table

# # tree = tr.tree
# # tr.connection
# # head = head

# # connection = {}


# # h = head['item'][0]
# # connection[h] = []
# # c = tree.children
# # for t in c:

# #     if(c.get[t]): +=[{c:c.get[t]}]
# #     continue



# # item, count = head["item"][-1], head["count"][-1]



# # dictionary = read(path='./inputs/example')
# # pprint.pprint(dictionary)
# # support, sequence = prepare(dictionary=dictionary, threshold=2)
# # pprint.pprint(support)
# # pprint.pprint(sequence)

# # def grow_node(chain=['I2', 'I1', 'I5'], node = {}):

# #     if(node=={}): node = {chain[-1]:{}}
# #     else: node = {chain[-1]:node}
# #     del chain[-1]
# #     if(chain!=[]): return(grow(chain, node))
# #     else: return(node)

# # left = {'I2': {'I1': {'I5': {}}}}
# # right = {'I2': {'I4': {}}}
# # by = 'left'
# # intersection = set.intersection(set(left.keys()), set(right.keys()))
# # intersection != {}
# # if(condition): pass
# # list(intersection)
# # left

# # grow_node(chain=['I1', 'I3'])


# # ['A', "C", "E", 'B']
# # a = [1,1,1,1]

# # ['A', 'C']
# # b = a[:2]
# # b[0] = b[0]+1

# # a

# # b = a
# # a[0] = 2
# # b[0]

