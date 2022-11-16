
import apriori
import fptree
import argparse
import time
   
if(__name__=='__main__'):

    parser = argparse.ArgumentParser()
    parser.add_argument("--method", help="method", default='apriori', type=str)
    parser.add_argument("--dataset", help="dataset path", default='./inputs/example', type=str)
    parser.add_argument("--min_sup", help="min support", default=0.1, type=float)
    parser.add_argument("--min_conf", help="min confidence", default=0.1, type=float)
    args = parser.parse_args()
    METHOD = args.method
    DATA_PATH = args.dataset
    SUP_MIN = args.min_sup
    CONF_MIN = args.min_conf
    # METHOD = 'apriori'
    # DATA_PATH = './inputs/2022-DM-release-testdata-2.data'
    # SUP_MIN = 0.3
    # CONF_MIN = 0.3
    # OUT_PATH = DATA_PATH.replace('inputs', 'outputs') + "_" + METHOD + ".csv"
    # OUT_PATH = './outputs/2022-DM-release-testdata-2.data_apriori.csv'

    if(METHOD=='apriori'):

        print("method: {}".format(METHOD))
        start_time = time.time()
        result = apriori.runApriori(data_path=DATA_PATH, sup_min=SUP_MIN, conf_min=CONF_MIN)
        finish_time = time.time()
        print("{} sec".format(round(finish_time - start_time, 2)))
        print("find {} item set".format(len(result['item'])))
        rule = apriori.getRule(result=result, confidence=CONF_MIN)
        apriori.writeSupport(result=result, path=DATA_PATH.replace('inputs', 'outputs') + "_" + METHOD + '_support' + ".csv")
        apriori.writeConfidence(rule=rule, path=DATA_PATH.replace('inputs', 'outputs') + "_" + METHOD + '_confidence' + ".csv")
        pass
    
    if(METHOD=='fptree'):
        
        print("method: {}".format(METHOD))
        start_time = time.time()
        result = fptree.runFptree(data_path=DATA_PATH, sup_min=SUP_MIN, conf_min=CONF_MIN)
        finish_time = time.time()
        print("{} sec".format(round(finish_time - start_time, 2)))
        print("find {} item set".format(len(result['item'])))
        rule = fptree.getRule(result=result, confidence=CONF_MIN)
        fptree.writeSupport(result=result, path=DATA_PATH.replace('inputs', 'outputs') + "_" + METHOD + '_support' + ".csv")
        fptree.writeConfidence(rule=rule, path=DATA_PATH.replace('inputs', 'outputs') + "_" + METHOD + '_confidence' + ".csv")
        pass

    pass
