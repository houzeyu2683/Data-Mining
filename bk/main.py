
class ibmqd:

    def __init__(self, path=None):

        self.path = path
        return

    def load(self):

        dictionary = {}
        # item = []
        with open(self.path, 'r') as paper:

            for line in paper.readlines():
                
                _, t, i = line.split()
                # item += [i]
                i = int(i)
                if(dictionary.get(t)): dictionary[t].add(i)
                else: dictionary[t] = {i}
                continue

            pass

        self.dictionary = dictionary
        # self.item = [{i} for i in set(item)]
        return   

    pass

def scan(dictionary={'01':{'a', 'b', 'c'}, '02':{'b', 'c', 'a'}}, threshold=0.5, item=[{'b', 'a'}]):

    proposal = {'item':[], 'score':[]}
    refusion = {'item':[], 'score':[]}
    for i in item:

        count = 0
        for k in dictionary:

            exist = set.intersection(i, dictionary[k]) == i
            if(exist): count += 1 
            continue
            
        s = (count / len(dictionary))
        store = s > threshold
        if(store): 
            
            proposal['item'] += [i]
            proposal['score'] += [s]
            pass
            
        else: 

            refusion['item'] += [i]
            refusion['score'] += [s]
            pass

        continue

    output = proposal['item'], proposal['score'], refusion['item'], refusion['score']
    return(output)

def expand(item=[{'a'}, {'b'}, {'c'}, {"d"}], ignore=[], length=2):

    candidate = []
    for left in item:

        for right in item:

            l, r = set(left), set(right)
            g = set.union(set(l), r)
            store = (g not in candidate) and (len(g)==length) and (sum([i.issubset(g) for i in ignore])==0)
            if(store): candidate += [g]
            continue

        continue

    return(candidate)

class apriori:

    def __init__(self, dictionary, support, limit=20):

        self.dictionary = dictionary
        self.support = support
        # self.confidence = confidence
        self.limit = limit
        return

    def prepare(self):

        item = []
        for k in self.dictionary: item += list(self.dictionary[k])
        item = [{i} for i in set(item)]
        return(item)

    def filter(self):

        summary = {
            'item':[],
            'score':[]
        }
        for i in range(self.limit):

            if(i==0): item = self.prepare()
            else: 
                
                item = expand(item=p['i'], ignore=r['i'], length=i+1)
                if(item==[] or i==(self.limit-1)): break
                pass

            p, r = {}, {}
            p['i'], p['s'], r['i'], _ = scan(dictionary=self.dictionary, threshold=self.support, item=item)
            for k, v in zip(p['i'], p['s']): 

                summary['item'] += [k]
                summary['score'] += [round(v,3)]
                continue

            continue

        self.summary = summary
        return

    def associate(self, antecedent='14', consequent='18'):

        left = set([int(i) for i in antecedent.split()])
        right = set([int(i) for i in consequent.split()])
        union = set.union(left, right)
        score = {
            'left':self.summary['score'][self.summary['item'].index(left)],
            'right':self.summary['score'][self.summary['item'].index(right)],
            'union':self.summary['score'][self.summary['item'].index(union)]
        }
        support = self.support
        confidence = score['union'] / score['left']

        confidence = self.score.get(union) / self.score.get(left)
        lift = confidence / right
        return(support, confidence, lift)

    pass

path = 'inputs/2022-DM-release-testdata-2.data'
data = ibmqd(path)
data.load()
model = apriori(dictionary=data.dictionary, support=0.5)
model.filter()
model.summary
model.associate(antecedent='14', consequent='18')



# item = model.prepare()

# dictionary = data.dictionary

# model.prepare()
# p, f = model.filter(model.item)

# item = expand(item=p['item'], ignore=f['item'], length=2)

# p, f = model.filter(item)

# item = expand(item=p['item'], ignore=f['item'], length=3)
# if(item==[])
# p, f = model.filter(item)


# p['item']

# f


# item  = [{'a'}, {'b'}, {'c'}]
# # score = [0.5, 0.2, 0.3]

# def support(dictionary, item={'30', '2'}):

#     count = 0
#     for k in dictionary:

#         exist = set.intersection(item, dictionary[k]) == item
#         if(exist): count += 1 
#         continue
    
#     length = len(dictionary)
#     score = count / length
#     return(score)




    # def prepare(self):

    #     length = len(self.transaction)
    #     item = set()
    #     chain = []
    #     for k in self.transaction: 
            
    #         item = item.union(self.transaction[k])
    #         chain = chain + list(self.transaction[k])
    #         continue
        
    #     count = []
    #     support = []
    #     for i in item: 
            
    #         count += [chain.count(i)]
    #         support += [chain.count(i)/length]
    #         continue

    #     pass

    #     self.length = length 
    #     self.item = item
    #     self.chain = chain 
    #     self.count = count
    #     self.support = support
    #     return

    # pass

# support(d.dictionary, {'12', '15'})

# d.prepare()
# d.item
# d.count
# tr = d.transaction
# d.chain
# len(tr)
# tr.items()


    


#     pass

# antecedent = {'12', '18'}
# consequent = '6'
# support = 0.5
# confidence = 0.6
# #lift



# def load_data(path):

#     item_list = []
#     with open(path, 'r') as f:

#         lines = f.readlines()
#         for line in lines:
            
#             _, _, iid = line.split()
#             item_list += [iid]
#             continue

#         pass

#     out = item_list
#     return(out)

# trans = load_data(path='inputs/2022-DM-release-testdata-2.data')
# trans_unique = set(trans)
# for i in trans_unique: 
    
#     c = trans.count(i)



# trans[0:20]




# item_list = trans
# unique_item_set = set(trans)
# unique_item_set_len = len(unique_item_set)

# for i in unique_item_set: 
    
#     {i : item_list.count(i)/ unique_item_set_len}
    
    



# def init_level_table(trans):

#     seq = []
#     for k in trans: seq += trans[k]



# # transaction_table = {'transID':[], "itemID":[]}
# # transaction_table = pd.DataFrame(transaction_table)


# def level_count(trans_dict)



# given_minsup = 0.5
# given_minconf = 0.6
# given_left_itemset = ['9', '4']
# given_right_itemset = ['6']

# given_union_set = given_left_itemset + given_right_itemset
# level_max = len(given_union_set)

# for i in range(level_max):

#     if(i==0):

#         class leveltab:

#             level = 0
#             trans = transaction_dict.copy()
#             length = len(transaction_dict)
#             pass
        
#         sum([given_union_set[i] in leveltab.trans[k] for k in leveltab.trans]) / leveltab.length

# t_level = 1
# item_unique_set = set(T['itemID'])



# T['itemID'].count("3")




