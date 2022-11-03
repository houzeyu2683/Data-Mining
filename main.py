
import argparse
import time
import os

import apriori
import fptree

def write(output, path='output.txt'):

    iteration = list(output.values())
    with open(path, 'w') as paper:
            
        title = ['freqset', 'support']
        line = ','.join(title) + '\n'
        paper.write(line)
        for i in zip(*iteration):

            line = ','.join([str(s) for s in i]) + '\n'
            paper.write(line)
            continue

        pass

    return

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--min_sup", help="min support", default=200, type=float)
    parser.add_argument("--min_conf", help="min confidence", default=200, type=float)
    parser.add_argument("--dataset", help="dataset", default='./inputs/2022-DM-release-testdata-2.data', type=str)
    args = parser.parse_args()
    pass

    min_sup = args.min_sup
    min_conf = args.min_conf
    dataset = args.dataset
    min_sup = 100
    min_conf = 100
    dataset = './inputs/ibm-2022.txt'
    
    print('start apriori method')
    dictionary = apriori.read(path=dataset)
    # LEN = len(dictionary) ## 不該這樣搞
    # threshold_sup = int(LEN*min_sup)
    # threshold_conf = int(LEN*min_conf)
    threshold_sup = min_sup
    threshold_conf = min_conf
    start_time = time.time()
    apriori_engine = apriori.engine(support=threshold_sup, confidence=threshold_conf, limit=10)
    apriori_engine.load(dictionary)
    apriori_engine.scan()
    finish_time = time.time()
    apriori_engine.time = finish_time - start_time
    print('finish apriori method: {}'.format(apriori_engine.time))
    pass

    ##  Store the hw ouput format.
    apriori_output = {'freqset':[], 'support':[]}
    loop = zip(apriori_engine.count['item'], apriori_engine.count['frequency'])
    for i,f in loop:

        apriori_output['freqset'] += ["{" + " ".join([str(i) for i in list(i)]) + "}"]
        apriori_output['support'] += [f / apriori_engine.length]
        continue
    
    write(apriori_output, path=dataset.replace('inputs', 'outputs') + '_appriori.csv')

    print('start fptree method')
    fptree_engine = fptree.Engine(path=dataset, support=threshold_sup, confidence=threshold_conf)
    start_time = time.time()
    fptree_engine.scan()
    finish_time = time.time()
    fptree_engine.time = finish_time - start_time
    print('finish fptree method: {}'.format(fptree_engine.time))
    pass

    ##  Store the hw ouput format.
    fptree_output = {'freqset':[], 'support':[]}
    loop = zip(fptree_engine.count['item'], fptree_engine.count['frequency'])
    for i,f in loop:

        fptree_output['freqset'] += ["{" + " ".join([str(i) for i in list(i)]) + "}"]
        fptree_output['support'] += [f / fptree_engine.length]
        continue
    
    write(fptree_output, path=dataset.replace('inputs', 'outputs') + '_fptree.csv')
    pass

