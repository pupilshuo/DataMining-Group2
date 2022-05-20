from utils import *
import datetime

def fpgrowth(fileName, minSupRatio, T_Num):
    """
    Input:file name,support ratio
    Output:freqItems, rules, T1, T2, T3
    """
    itemSetList, frequency = getFromFile(fileName, T_Num)
    print("length", len(itemSetList))
    minSup = len(itemSetList) * minSupRatio
    T1 = datetime.datetime.now()
    fpTree, headerTable = constructTree(itemSetList, frequency, minSup)
    print(headerTable)
    if(fpTree == None):
        print('No frequent item set')
    else:
        freqItems = []
        T2 = datetime.datetime.now()
        mineTree(headerTable, minSup, set(), freqItems)
        T3 = datetime.datetime.now()
        #runtime = str((T2-T1)/math.pow(10, 6))
        rules = associationRule(freqItems, itemSetList)

        return freqItems, rules, T1, T2, T3
