
import pprint

def read(path):

    dictionary = {}
    with open(path, 'r') as paper:
    
        for line in paper.readlines():
            # print(line)
            _, t, i = line.split()
            try: i = int(i) 
            except: i = str(i)
            if(dictionary.get(t)): dictionary[t].add(i)
            else: dictionary[t] = {i}
            continue
    
        pass
    
    return(dictionary)

def prepare(dictionary, threshold=2):

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
    
    return(head, sequence)

class node:

    def __init__(self, count=0, name="", children={}, father=None):

        self.count = count
        self.name = name
        self.children = children
        self.father = father
        # self.visit = 0#用于链表的时候观察是否已经被访问过了        
        # self.next = None#用于链表，链接到另一个孩子处
        return

    pass

class root:

    def __init__(self, table, connection = {}):

        self.table = table
        self.connection = connection        
        return

    def build(self):

        table = self.table
        tree = node(count=None, name='root', children={}, father=None)
        for row in table:
            
            branch = tree
            for name in table[row]:
                
                if(branch.children.get(name)): branch.children.get(name).count += 1
                else: branch.children[name] = node(count=1, name=name, children={}, father=branch)
                branch = branch.children[name]
                continue
            
            continue
        
        self.tree = tree
        return

    def connect(self, tree):
        
        if(tree.children!={}):
            
            for (_, children) in tree.children.items():

                exist = self.connection.get(children.name)
                if(not exist): self.connection[children.name] = []
                self.connection[children.name] += [children]
                self.connect(tree=children)
                continue

            pass

        return

    pass
 
trans = read('./inputs/bit')
head, trans_order = prepare(trans)
tr = root(table=trans_order)
tr.build()
tr.connection
tr.connect(tr.tree)
tr.connection


head["item"][-1]
head["count"][-1]
tree = tr.tree
tree

h = head["item"][-1]
n = tr.connection[h][0]
n.father.father.father.name

def prune(node, tree):

    
    return(tree)


# node = tr.tree.children['I2']
# node.name

# tr.tree.children['I2'].children['I1'].children['I4'].children
# tr.table

# tree = tr.tree
# tr.connection
# head = head

# connection = {}


# h = head['item'][0]
# connection[h] = []
# c = tree.children
# for t in c:

#     if(c.get[t]): +=[{c:c.get[t]}]
#     continue



# item, count = head["item"][-1], head["count"][-1]



# dictionary = read(path='./inputs/example')
# pprint.pprint(dictionary)
# support, sequence = prepare(dictionary=dictionary, threshold=2)
# pprint.pprint(support)
# pprint.pprint(sequence)

# def grow_node(chain=['I2', 'I1', 'I5'], node = {}):

#     if(node=={}): node = {chain[-1]:{}}
#     else: node = {chain[-1]:node}
#     del chain[-1]
#     if(chain!=[]): return(grow(chain, node))
#     else: return(node)

# left = {'I2': {'I1': {'I5': {}}}}
# right = {'I2': {'I4': {}}}
# by = 'left'
# intersection = set.intersection(set(left.keys()), set(right.keys()))
# intersection != {}
# if(condition): pass
# list(intersection)
# left

# grow_node(chain=['I1', 'I3'])


# ['A', "C", "E", 'B']
# a = [1,1,1,1]

# ['A', 'C']
# b = a[:2]
# b[0] = b[0]+1

# a

# b = a
# a[0] = 2
# b[0]

