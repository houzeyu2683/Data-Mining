
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

def occur(dictionary={'01':{'a', 'b', 'c'}, '02':{'b', 'c', 'a'}}, threshold=2, item=[{'b', 'a'}]):

    proposal = {'item':[], 'frequency':[]}
    refusion = {'item':[], 'frequency':[]}
    for i in item:

        count = 0
        for k in dictionary:

            exist = set.intersection(i, dictionary[k]) == i
            if(exist): count += 1 
            continue
            
        # s = (count / len(dictionary))
        f = count
        condition = count >= threshold
        if(condition): 
            
            proposal['item'] += [i]
            proposal['frequency'] += [f]
            pass
            
        else: 

            refusion['item'] += [i]
            refusion['frequency'] += [f]
            pass

        continue

    output = proposal, refusion
    return(output)

# item = [{'I4', 'I2'}, {'I1', 'I2'}, {'I1', 'I3'}, {'I1', 'I5'}, {'I2', 'I3'}, {'I2', 'I5'}]
def expand(item=[{'a'}, {'b'}, {'c'}, {"d"}, {"c", "d"}], ignore=[], length=2):

    candidate = []
    for left in item:

        for right in set.union(*item):

            l, r = set(left), set([right])
            u = set.union(set(l), r)
            s = sum([i.issubset(u) for i in ignore])
            store = (u not in candidate) and (len(u)==length) and (s==0)
            if(store): candidate += [u]
            continue

        continue

    return(candidate)

# def expand(item=[{'a'}, {'b'}, {'c'}, {"d"}], ignore=[], length=2):

#     candidate = []
#     for left in item:

#         for right in item:

#             l, r = set(left), set(right)
#             u = set.union(set(l), r)
#             s = sum([i.issubset(u) for i in ignore])
#             store = (u not in candidate) and (len(u)==length) and (s==0)
#             if(store): candidate += [u]
#             continue

#         continue

#     return(candidate)

def prepare(dictionary):

    item, count = [], []
    loop = set.union(*dictionary.values())
    for k in loop:

        item += [{k}]
        count += [sum([k in v for v in dictionary.values()])]
        continue
    
    index = range(len(loop))
    order = sorted(index, key=lambda k: count[k], reverse = True)
    output = [item[o] for o in order], [count[o] for o in order]
    return(output)

class engine:

    def __init__(self, support, confidence, limit=20):

        # self.dictionary = dictionary
        self.support = support
        self.confidence = confidence
        self.limit = limit
        return

    def load(self, dictionary):

        self.dictionary = dictionary
        return

    def scan(self):

        count = {'item':[],'frequency':[]}
        for i in range(self.limit):

            if(i==0): item, _ = prepare(self.dictionary)
            else: 

                item = expand(item=proposal['item'], ignore=refusion['item'], length=i+1)
                if(item==[] or i==(self.limit-1)): break
                pass
            
            proposal, refusion = occur(dictionary=self.dictionary, threshold=self.support, item=item)
            loop = zip(proposal['item'], proposal['frequency'])
            for k, v in loop: 

                count['item'] += [k]
                count['frequency'] += [round(v,3)]
                continue

            continue

        self.count = count
        return

    def cross(self):

        antecedent = []
        consequent = []
        support = []
        confidence = []
        lift = []
        total = len(self.dictionary)
        # print(len(self.count['item']))
        for left in self.count['item']:

            for right in self.count['item']:

                # print(left, right)
                union = set.union(left, right)
                # print(union)
                condition = (not (union==left or union==right)) and (union in self.count['item'])
                # print(condition)
                if(condition): 
                    
                    p = {}
                    p['AUB'] = self.count['frequency'][self.count['item'].index(union)] / total
                    p['A'] = self.count['frequency'][self.count['item'].index(left)] / total
                    p['B'] = self.count['frequency'][self.count['item'].index(right)] / total
                    pass

                    condition = (p['AUB'] / p['A']) >= self.confidence
                    if(condition):

                        antecedent += [str(left).replace(',', "")]
                        consequent += [str(right).replace(',', "")]
                        support += [round(p['AUB'], 3)]
                        confidence += [round(p['AUB'] / p['A'], 3)]
                        lift += [round((p['AUB'] / p['A']) / p['B'], 3)]
                        pass

                    pass

                continue

            continue
        
        summary = {
            'antecedent':antecedent, 'consequent':consequent, 
            "support":support, "confidence":confidence, "lift":lift
        }
        self.summary = summary
        return

    def write(self, path):

        iteration = list(self.summary.values())
        with open(path, 'w') as paper:
            
            title = ['antecedent', 'consequent', 'support', 'confidence', 'lift']
            line = ','.join(title) + '\n'
            paper.write(line)
            for i in zip(*iteration):

                line = ','.join([str(s) for s in i]) + '\n'
                paper.write(line)
                continue

            pass

        return

    def associate(self, antecedent={34, 41}, consequent={14}):

        ##
        return

    pass

dictionary = read(path='./inputs/2022-DM-release-testdata-2.data')
apriori = engine(support=300, confidence=0, limit=10)
apriori.load(dictionary)
apriori.scan()
apriori.cross()
apriori.write(path='./outputs/apriori.csv')




