
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
        
        self.length = len(dictionary.keys())
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
        
        head['item'].reverse()
        head['count'].reverse()
        pass

        self.threshold = threshold
        self.head = head
        self.sequence = sequence
        return

    pass

class node:

    def __init__(self, count=0, name="", children={}, father=None, status=0):

        self.count = count
        self.name = name
        self.children = children
        self.father = father
        self.status = status
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

    def __init__(self, sequence):

        self.sequence = sequence
        return

    def build(self):

        sequence = self.sequence
        tree = node(count=None, name='root', children={}, father=None, status=0)
        for row in sequence:
            
            branch = tree
            for name in sequence[row]:
                
                if(branch.children.get(name)): branch.children.get(name).count += 1
                else: branch.children[name] = node(count=1, name=name, children={}, father=branch, status=0)
                branch = branch.children[name]
                continue
            
            continue
        
        self.tree = tree
        return

    ##  Tree node link.
    def connect(self, node, first=True):

        if(first): self.connection = {}
        if(node.children!={}):
            
            for (_, item) in node.children.items():

                exist = self.connection.get(item.name)
                if(not exist): self.connection[item.name] = []
                self.connection[item.name] += [item]
                pass
                
                self.connect(node=item, first=False)
                continue

            pass

        return

    ##  get head table with sort.
    def update(self, what='head'):

        if(what=='head'):

            assert self.connection, 'connection not found'
            length = len(self.connection.keys())
            item, count = [], []
            for k in self.connection.keys():
                
                item += [k]
                count += [sum([n.count for n in self.connection[k]])]
                continue
            
            order = sorted(range(length), key=lambda k: count[k])
            item = [item[o:o+1][0] for o in order]
            count = [count[o:o+1][0] for o in order]
            head = {'item': item, "count":count}
            self.head = head
            pass

        return

    def capture(self, node=37):

        connection = self.connection
        for n in connection[node]: 

            c = n.count
            n.children = {}
            while(n.name != 'root'): 

                if(n.status==0): 
                    
                    n.count = c
                    n.status = 1
                    pass

                else: 
                    
                    n.count += c
                    pass

                n = n.father
                continue
        
        ##  Remove the node without status=0(not visit)
        for k in connection: 

            for n in connection[k]:

                name = None
                while(n.status==0):

                    name = n.name 
                    n = n.father
                    if(not n): continue
                    break

                if(not n or not name): break

                if(n.children.get(name)): n.children.pop(name)
                continue

            continue

        self.branch = self.tree
        return

    def reset(self):

        self.build()
        self.connect(node=self.tree, first=True)
        self.sort()
        self.branch = None
        return
    
    pass

threshold=300
d = data(path='./inputs/2022-DM-release-testdata-2.data')
d.read()
d.prepare()
d.length

p = plant(sequence=d.sequence)
p.build()
p.connect(p.tree)
p.sort()
p.head
p.tree.children[14].children

p.capture(node=18)
p.branch.children
p.connect(node=p.branch)
p.connection
p.sort()
p.head

p.branch.children[18].children
p.branch.children[14].children
p.reset()
p.tree.children
p.tree
