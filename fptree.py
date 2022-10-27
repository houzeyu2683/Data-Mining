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
    support = {"item":item, "count":count}
    pass

    sequence = {}
    for key, v in dictionary.items():

        v = list(v)
        chain = []
        for i in support['item']: 

            if(i in v): chain += [i]
            continue

        sequence[key] = chain
        continue
    
    return(support, sequence)


dictionary = read(path='./inputs/example')
pprint.pprint(dictionary)
support, sequence = prepare(dictionary=dictionary, threshold=2)
pprint.pprint(support)
pprint.pprint(sequence)

def grow_node(chain=['I2', 'I1', 'I5'], node = {}):

    if(node=={}): node = {chain[-1]:{}}
    else: node = {chain[-1]:node}
    del chain[-1]
    if(chain!=[]): return(grow(chain, node))
    else: return(node)

left = {'I2': {'I1': {'I5': {}}}}
right = {'I2': {'I4': {}}}
by = 'left'
intersection = set.intersection(set(left.keys()), set(right.keys()))
intersection != {}
if(condition): pass
list(intersection)
left

grow_node(chain=['I1', 'I3'])


['A', "C", "E", 'B']
a = [1,1,1,1]

['A', 'C']
b = a[:2]
b[0] = b[0]+1

a

b = a
a[0] = 2
b[0]

