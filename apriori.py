
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

def getCount(head):

    loop = zip(head['unit'], head['value'])
    count = {u:v for u, v in loop}
    return(count)

def upgradeHead(table, head, support):

    chain = sum([u.split(",") for u in head['unit']], [])
    key = list(set(chain))
    match = []
    for u in head['unit']:

        for k in key:

            l = ','.join(list(sorted(set([u,k]))))
            m = ','.join(list(sorted(set(l.split(',')))))
            condition = ((m not in match) and (m not in head['unit']))
            if(condition): match += [m]
            continue
        
        continue
    
    count = []
    for m in match:
        
        s = m.split(',')
        c = 0
        for i in table['item']:

            exist = not (False in [p in i for p in s])
            if(exist): c += 1
            continue

        count += [c]
        continue
    
    name = match
    value = count
    pass

    index = range(len(name))
    order = sorted(index, key=lambda k: value[k], reverse = True)
    unit = [name[o] for o in order]        
    value = [value[o] for o in order]        
    head = updateHead({'unit':unit, 'value':value}, support)
    return(head)

def getFrequency(summary):

    item = []
    count = []
    for i, c in summary.items():

        item += [i]
        count += [c]
        continue

    frequency = {'item':item, 'count':count}
    return(frequency)

def getSupport(summary, length):

    item = []
    count = []
    for i, c in summary.items():

        item += [i]
        count += [round(c/length, 3)]
        continue

    frequency = {'item':item, 'count':count}
    return(frequency)

def runApriori(data_path, sup_min, conf_min):

    ##  load data
    table = readTable(data_path)
    head = getHead(table)
    pass

    ##  common setting
    length = len(table['number'])
    support = int(sup_min * length)
    confidence = int(conf_min * length)  ## not use...'..'
    summary = {}
    pass

    ##  inital step
    head = updateHead(head, support=support)
    count = getCount(head)
    summary.update(count)
    pass

    while(head['unit']!=[]):

        head = upgradeHead(table, head, support)
        count = getCount(head)
        summary.update(count)
        pass
    
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

'''
import time
DATA_PATH = './inputs/2022-DM-release-testdata-2.data'
SUP_MIN = 0.3
CONF_MIN = 0.3
OUT_PATH = './outputs/2022-DM-release-testdata-2.data_apriori.csv'
start_time = time.time()
result = runApriori(data_path=DATA_PATH, sup_min=SUP_MIN, conf_min=CONF_MIN)
print(len(result['item']))
finish_time = time.time()
print("{} sec".format(round(finish_time - start_time, 2)))
writeResult(result=result, path=OUT_PATH)
'''
