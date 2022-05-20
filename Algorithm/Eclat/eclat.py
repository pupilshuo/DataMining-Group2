# -----------eclat-------------#
from utils import *
from csv import reader, writer

minSup = 0.001
itemSetList = []
data_ls = dict()
freqItemSet = []

if __name__ == '__main__':
    with open('product_name_set.csv', encoding='UTF-8-sig') as file:
    # with open('test.csv', encoding='UTF-8-sig') as file:
        csv_reader = reader(file)
        for line in csv_reader:
            line = list(filter(None, line))
            line = ','.join(line)
            itemSetList.append(line)

    threshold_val = minSup * len(itemSetList)
    print(len(itemSetList))

    for i, j in enumerate(itemSetList):
        num = i + 1
        num = str(num)
        data_ls[num] = j.split(',')

    # Converting horizontal data formats to vertical data formats
    data_vert = convert(data_ls)
    # Delete items that do not meet the minimum support
    data_vert = drop_data(data_vert, threshold_val)
    # Get the set of frequent items L1
    # data_vert.pop(frozenset({''}))
    combo = data_vert
    itemSet1 = [frozenset(key) for key in data_vert.keys()]
    # Received candidate k+1 sets
    k = 2
    candidate = aprioriGen(itemSet1, k)


    i = 1
    while len(candidate):
        print(i)
        i += 1
        # Support is calculated by finding the intersection of the candidate 2-item set
        data_vert = get_support(candidate, data_vert)
        # delete the items  which don't reach the threshold of the support
        data_vert = drop_data(data_vert, threshold_val)

        if len(data_vert):
            combo = merge(combo, data_vert)
            L = [frozenset(key) for key in data_vert.keys()]
            candidate = aprioriGen(L, k + 1)
        else:
            break

    print("loop ending")

    for i in combo.keys():
        itemset = set(i)
        freqItemSet.append(itemset)

    print("get sets")

    with open("fileItemset.csv", "w", newline='', encoding='UTF-8-sig') as csvfile:
        for i in freqItemSet:
            csvfile.write(str(i))
            csvfile.write('\n')

    # rules = associationRule(freqItemSet, itemSetList)

    # with open("rules.csv", "w", newline='') as csvfile:
    #     writer = writer(csvfile)
    #     writer.writerows(rules)
