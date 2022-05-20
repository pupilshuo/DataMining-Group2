from csv import reader
from collections import defaultdict
from itertools import chain, combinations

import operator

import pandas as pd


class Node:
    """
    Define a tree node include the name,count,parent node,children node,next node
    """
    def __init__(self, itemName, frequency, parentNode):
        self.itemName = itemName
        self.count = frequency
        self.parent = parentNode
        self.children = {}
        self.next = None

    def increment(self, frequency):
        self.count += frequency

    def display(self, ind=1):
        print('  ' * ind, self.itemName, ' ', self.count)
        for child in list(self.children.values()):
            child.display(ind + 1)

def getFromFile(fname, T_Num):
    #null itemset list
    itemSetList = []
    #null item frequency
    frequency = []
    with open(fname, 'r',  encoding='UTF-8') as file:
        csv_reader = reader(file)
        count = 0
        # for line in csv_reader:
        #      if count == T_Num:
        #          break
        #      else:
        #          count += 1
        #          line = list(filter(None, line))
        #          itemSetList.append(line)
        #          frequency.append(1)
        for line in csv_reader:
            line = list(filter(None, line))
            itemSetList.append(line)
            frequency.append(1)
    # print(itemSetList)
    return itemSetList, frequency

def constructTree(itemSetList, frequency, minSup):

    headerTable = defaultdict(int)

    # Count frequency and create header table
    for idx, itemSet in enumerate(itemSetList):
        for item in itemSet:



            headerTable[item] += frequency[idx]

    # Deleting items below minSup
    headerTable = dict((item, sup) for item, sup in headerTable.items() if sup >= minSup)

    value_key_pairs = ((value, key) for (key, value) in headerTable.items())
    sorted_value_key_pairs = sorted(value_key_pairs, reverse=True)
    print("Header Table")
    df = pd.DataFrame(sorted_value_key_pairs)
    print(df.head(3))
    df.to_csv("header.csv")

    if (len(headerTable) == 0):
        return None, None

    # HeaderTable column [Item: [frequency, headNode]]
    for item in headerTable:
        headerTable[item] = [headerTable[item], None]

    # print(headerTable)

    # initiate Null headNode
    fpTree = Node('Null', 1, None)

    # Update FP tree for each cleaned and sorted itemSet
    for idx, itemSet in enumerate(itemSetList):
        itemSet = [item for item in itemSet if item in headerTable]
        itemSet.sort(key=lambda item: headerTable[item][0], reverse=True)
        # Traverse from root to leaf, update tree with given item
        currentNode = fpTree
        for item in itemSet:
            currentNode = updateTree(item, currentNode, headerTable, frequency[idx])

    fpTree.display()
    return fpTree, headerTable


def constructTree_2(itemSetList, frequency, minSup):

    headerTable = defaultdict(int)

    # Count frequency and create header table
    for idx, itemSet in enumerate(itemSetList):
        for item in itemSet:



            headerTable[item] += frequency[idx]

    # 项头表

    # Deleting items below minSup
    headerTable = dict((item, sup) for item, sup in headerTable.items() if sup >= minSup)

    if (len(headerTable) == 0):
        return None, None

    # HeaderTable column [Item: [frequency, headNode]]
    for item in headerTable:
        headerTable[item] = [headerTable[item], None]

    # initiate Null headNode
    fpTree = Node('Null', 1, None)

    # Update FP tree for each cleaned and sorted itemSet
    for idx, itemSet in enumerate(itemSetList):
        itemSet = [item for item in itemSet if item in headerTable]
        itemSet.sort(key=lambda item: headerTable[item][0], reverse=True)
        # Traverse from root to leaf, update tree with given item
        currentNode = fpTree
        for item in itemSet:
            currentNode = updateTree(item, currentNode, headerTable, frequency[idx])

    return fpTree, headerTable


def updateTree(item, treeNode, headerTable, frequency):
    if item in treeNode.children:
        # If the item already exists, increment the count
        treeNode.children[item].increment(frequency)
    else:
        # Create a new branch
        newItemNode = Node(item, frequency, treeNode)
        treeNode.children[item] = newItemNode
        # Link the new branch to header table
        updateHeaderTable(item, newItemNode, headerTable)

    return treeNode.children[item]

def updateHeaderTable(item, targetNode, headerTable):
    if (headerTable[item][1] == None):
        headerTable[item][1] = targetNode
    else:
        currentNode = headerTable[item][1]
        # Traverse to the last node then link it to the target
        while currentNode.next != None:
            currentNode = currentNode.next
        currentNode.next = targetNode



def ascendFPtree(node, prefixPath):
    if node.parent != None:
        prefixPath.append(node.itemName)
        ascendFPtree(node.parent, prefixPath)

def findPrefixPath(basePat, headerTable):
    # First node in linked list
    treeNode = headerTable[basePat][1]
    condPats = []
    frequency = []
    while treeNode != None:
        prefixPath = []
        # From leaf node all the way to root
        ascendFPtree(treeNode, prefixPath)
        if len(prefixPath) > 1:
            # Storing the prefix path and it's corresponding count
            condPats.append(prefixPath[1:])
            frequency.append(treeNode.count)

        # Go to next node
        treeNode = treeNode.next
    return condPats, frequency

def mineTree(headerTable, minSup, preFix, freqItemList):
    # Sort the items with frequency and create a list
    sortedItemList = [item[0] for item in sorted(list(headerTable.items()), key=lambda p: p[1][0])]
    # print("sortted item list", sortedItemList)
    # Start with the lowest frequency
    for item in sortedItemList:
        # Pattern growth is achieved by the concatenation of suffix pattern with frequent patterns generated from conditional FP-tree
        newFreqSet = preFix.copy()
        newFreqSet.add(item)


        freqItemList.append(newFreqSet)

        # Find all prefix path, constrcut conditional pattern base
        conditionalPattBase, frequency = findPrefixPath(item, headerTable)
        # Construct conditonal FP Tree with conditional pattern base

        # print("conditional patt base")

        conditionalTree, newHeaderTable = constructTree_2(conditionalPattBase, frequency, minSup)
        if newHeaderTable != None:
            # Mining recursively on the tree
            mineTree(newHeaderTable, minSup,
                     newFreqSet, freqItemList)

def powerset(s):
    """
      Generate all unique permutations of each element in the powerset(s)
    """
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)))

def getSupport(testSet, itemSetList):
    """The support of the candidate k-item set is obtained by finding the intersection set, and therefore the k+1-item set"""
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
            rules.append([set(s), set(itemSet.difference(s)), confidence])
    return rules

def getFrequencyFromList(itemSetList):
    frequency = [1 for i in range(len(itemSetList))]
    return frequency
