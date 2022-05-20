"""
utilization of Eclat,including converting data,drop data,get support of the itemset and set the union of associate rule
"""

from itertools import chain, combinations

def convert(data_ls):
    """Converting horizontal data items to vertical data items"""
    data_vert = {}
    for tid, items in data_ls.items():
        for item in items:
            if frozenset({item}) not in data_vert:
                data_vert[frozenset({item})] = {tid}
            else:
                data_vert[frozenset({item})].add(tid)
    return data_vert

def drop_data(data, threshold_val):
    """Remove infrequent items based on thresholds"""
    res = data.copy()
    for key in data:
        if len(data[key]) < threshold_val:
            del res[key]
    return res

def aprioriGen(Lk_1, k):  # creates Ck
    """
    Generate candidate k-item sets based on k-1 item sets
    Input.
    Lk_1: list of k-1 itemsets
    k: k of the k-item set
    """
    res = {}
    lenLk_1 = len(Lk_1)  #the length of  k-1 itemset
    for i in range(lenLk_1):
        for j in range(i + 1, lenLk_1):
            L1 = sorted(list(Lk_1[i]))
            # When k is equal to 2, the 1-item set is taken as empty, when k is equal to 3, the 2-item set is taken as the first element, and when k is equal to 4, the 3-item set is taken as the first two elements
            L2 = sorted(list(Lk_1[j]))
            # When k is equal to 2, the 1-item set is taken as empty, when k is equal to 3, the 2-item set is taken as the first element, and when k is equal to 4, the 3-item set is taken as the first two elements
            if L1[:k - 2] == L2[:k - 2]:
                # If the first k minus 2 elements are equal, then merge the two geometries
                res[Lk_1[i] | Lk_1[j]] = [Lk_1[i], Lk_1[j]]  # set union
    return res

def get_support(candidate_k_1, vert):
    """The support of the candidate k-item set is obtained by finding the intersection set, and therefore the k+1-item set"""
    res = {}
    for key, items in candidate_k_1.items():
        item1, item2 = items
        ss = vert[item1] & vert[item2]
        res[key] = ss
    return res

# def trans(combo):
#     for i in list(combo.keys()):
#         new_k = tuple(sorted(list(i)))
#         if len(new_k) == 1:
#             combo[(new_k[0])] = combo.pop(i)
#         else:
#             key = new_k[0] + "," + new_k[1]
#             combo[key] = combo.pop(i)
#     return combo

def merge(dict1, dict2):
    """
    Merge the two dicts into one dict
    """
    res = {**dict1, **dict2}
    return res

def powerset(s):
    """
    Generate all unique permutations of each element in the powerset(s)
    """
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)))

def getSupport(testSet, itemSetList):
    """
    get the support of Itemset
    output:
    count:the value of support
    """
    count = 0
    for itemSet in itemSetList:
        if (set(testSet).issubset(itemSet)):
            count += 1
    return count

def associationRule(freqItemSet, itemSetList):
    """
    generate the association rule including the the difference,lift and confidence of k itemset
    output:
    rules(list):[set(s), set(itemSet.difference(s)), confidence, lift]
    """
    rules = []
    for itemSet in freqItemSet:
        subsets = powerset(itemSet)
        itemSetSup = getSupport(itemSet, itemSetList)
        for s in subsets:
            confidence = float(itemSetSup / getSupport(s, itemSetList))
            lift = float(confidence / float(getSupport(itemSet.difference(s), itemSetList)/len(itemSetList)))
            rules.append([set(s), set(itemSet.difference(s)), confidence, lift])
    return rules
