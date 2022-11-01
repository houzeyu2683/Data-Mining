
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
        # self.connection = {}
        return

    def connect(self, children, first=True):

        if(first): self.connection = {}
        if(children!={}):
            
            for (_, item) in children.items():

                exist = self.connection.get(item.name)
                if(not exist): self.connection[item.name] = []
                self.connection[item.name] += [item]
                pass
                
                self.connect(children=item.children, first=False)
                continue

            pass

        return

    pass

class pattern:

    def __init__(self, connection, threshold):

        self.connection = connection
        self.threshold = threshold
        pass
    
    def grow(self, item=38, limit=None):

        base = []
        # print(item)
        for l in connection[item]:

            l.track()
            if(len(l.trace)<3): continue
            b = [n.name for n in l.trace[1:-1]] * l.trace[-1].count
            base += b
            continue
        
        unit = {}
        threshold = self.threshold
        for i in set(base):

            if(base.count(i)>threshold): unit.update({i:base.count(i)})
            
            continue

        base = [set([i]) for i in unit.keys()]
        group = []
        frequency = {}
        limit = limit if(limit) else len(base)
        for i in range(limit):

            if(i==0): 
                
                group += base.copy()
                frequency.update({",".join([str(k)]+[str(item)]):v for k,v in unit.items()})
                pass

            else:

                # group = [set.union(l,r) for l in base for r in group]
                pool = group.copy()
                # print(pool)
                for b in base:

                    # pool = [p for p in pool if(p.intersection(b)==set())]
                    for g in pool:
                        
                        u = set.union(b, g)
                        if(u not in group): 
                            
                            group += [u]
                            f = {",".join([str(i) for i in u]+[str(item)]): min([unit.get(v) for v in u])}
                            frequency.update(f)
                            pass

                        continue

                    continue

                pass

            continue
        

        return(frequency)

    pass

threshold=300
d = data(path='./inputs/2022-DM-release-testdata-2.data')
d.read()
d.length
d.prepare(threshold=threshold)
d.head
p = plant(sequence=d.sequence)
p.build()
p.connect(children=p.tree.children, first=True)
connection = p.connection
pa = pattern(connection=connection, threshold=threshold)


# pa.grow(item=38, limit=3)

frequency = {}
for i in d.head['item']:

    print(i)
    frequency.update(pa.grow(i, limit=3))
    continue


len(frequency.keys())
len(set(frequency.keys()))
frequency['14,18']

2184
1580 / 
# def grow(unit, limit=3):

#     base = [set([i]) for i in unit.keys()]
#     group = []
#     frequency = {}
#     limit = limit if(limit) else len(base)
#     for i in range(limit):

#         if(i==0): 
            
#             group += base
#             frequency.update({str(k):v for k,v in unit.items()})
#             pass

#         else:

#             for b in base:

#                 for g in group:

#                     u = set.union(b, g)
#                     # print(u)
#                     if(u not in group): 
                        
#                         group += [u]
#                         f = {",".join([str(i) for i in u]): min([unit.get(v) for v in u])}
#                         frequency.update(f)
#                         pass

#                     continue

#                 continue

#             pass

#         continue

#     return

# def subs(l):
#     if l == []:
#         return [[]]

#     x = subs(l[1:])

#     return x + [[l[0]] + y for y in x]    

# subs([1,2,4,5,6])
# # class generation:

# #     def __ini__(self, unit):

# #         self.unit = unit
# #         return
    
# #     def grow(self, first=True):

# #         if(first): 
            
# #             pattern = self.unit
# #             pool = [set([i]) for i in self.unit]
# #             pass

# #         else: 

# #             for l in pattern:
# #                 break
# #                 for r in pattern:

# #                     p = set([l,r])
# #                     if(p not in pool):

# #                         pool += [p]
# #                         set()
# #                         pass

# #                     continue

# #                 continue

# #             pass

# #         return

# #     pass

# # unit

# e = engine(p.tree, d.head, p.connection)
# e.search(threshold=200)
# e.frequency

# unit = {}
# # class branch:

# #     def __init__(self, trace, size=3):

# #         self.trace = trace
# #         self.size = size
# #         return

# #     def match(self):

# #         left = self.trace[1:-1]
# #         right = self.trace[-1]
# #         pass

# #         count = right.count
# #         name = right.name
# #         pattern = self.expand(term=[n.name for n in left])
# #         item = [p+","+str(name) for p in pattern]
# #         return(item, count)

# #     def expand(self, term):

# #         for i in range(self.size):

# #             if(i==0): 

# #                 group = [set([n]) for n in term]
# #                 continue

# #             else:
                
# #                 pool = []
# #                 for n in term:

# #                     for g in group:

# #                         c = g.union(set([n]))
# #                         if(c not in pool): pool += [c]

# #                     continue
                
# #                 group = pool
# #                 pass    
            
# #             continue
        
# #         extension = [','.join([str(i) for i in list(i)]) for i in group]
# #         return(extension)

# #     pass

# class engine:

#     def __init__(self, tree, head, connection):

#         self.tree = tree
#         self.head = head
#         self.connection = connection
#         return

#     def search(self, threshold=2):

#         frequency = {}
#         loop = zip(self.head['item'], self.head['count'])
#         for key, _ in loop:

#             index = set()
#             pattern = []
#             for chain in self.connection[key]:

#                 chain.track()
#                 trace = chain.trace
#                 if(len(trace)>2):

#                     item, count = branch(trace=trace).match()
#                     index = set.union(index, set(item))
#                     pattern += item * count
#                     pass

#                 continue
            
#             for i in index:

#                 if(pattern.count(i)<threshold):

#                     continue

#                 elif(frequency.get(i)):

#                     frequency[i] += pattern.count(i)
#                     pass
                
#                 else:

#                     frequency[i] = pattern.count(i)
#                     pass

#                 continue

#             continue
        
#         loop = zip(self.head['item'], self.head['count'])
#         frequency.update({k:v for k, v in loop})
#         self.frequency = frequency
#         return

#     pass




