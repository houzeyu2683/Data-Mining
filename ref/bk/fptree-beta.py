
class Data:

    def __init__(self, path):

        self.path = path
        return

    def readTable(self):

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

    def process(self, threshold=2):

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

    def __init__(self, sequence, threshold=300):

        self.sequence = sequence
        self.threshold = threshold
        return

    def buildTree(self):

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
    def getLink(self, node, root=True):

        if(root): self.link = {}
        if(node.children!={}):
            
            for (_, item) in node.children.items():

                exist = self.link.get(item.name)
                if(not exist): self.link[item.name] = []
                self.link[item.name] += [item]
                pass
                
                self.getLink(node=item, root=False)
                continue

            pass

        return

    ##  get head table.
    def getHead(self):

        assert self.link, 'link not found'
        length = len(self.link.keys())
        item, count = [], []
        for k in self.link.keys():
                
            item += [k]
            count += [sum([n.count for n in self.link[k]])]
            continue
            
        order = sorted(range(length), key=lambda k: count[k])
        item = [item[o:o+1][0] for o in order]
        count = [count[o:o+1][0] for o in order]
        head = {'item': item, "count":count}
        self.head = head
        return

    def captureBranch(self, node=17):

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
        pass

        self.buildTree()
        self.branch = self.tree
        return

    def reset(self):

        self.buildTree()
        self.getLink(node=self.tree, first=True)
        self.getHead()
        self.branch = None
        return
    
    def mineFrequency(self, p):

        head = p.head
        print('對', head['item'], "開發")
        tree = p.tree
        link = p.link
        for k, v in zip(head['item'], head['count']):
            break
            p.captureBranch(node=k)
            p.tree
            p.tree.children
            print('---')
            p.getLink(node=p.tree, root=True)
            print('--')
            p.getHead()
            print('-')
            print('對', p.head['item'], "開發")
            continue

        return

    pass

threshold=30
d = Data(path='./inputs/2022-DM-release-testdata-2.data')
d.readTable()
d.process(threshold=threshold)
d.length
d.head

p = Plant(sequence=d.sequence)
p.buildTree()
p.tree
p.tree.children
p.getLink(node=p.tree, root=True)
p.getHead()
p.head

p.captureBranch(node=23)
p.branch.children



