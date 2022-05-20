#!/bin/env python3

import sys
import time

import utils


def print_dist(result):
    """ Print structure of frequent itemsets and their count. Structure
    string is list of number separated by '-'. The left most number is
    count of frequent itemsets of length 1, second number is count of
    frequent pairs and so on.

    Output has format:
    total count | structure string
    """


    fitemsets=""
    if len(result) >  0:
        previous = result[0]
        count = 0
        for itemset in result:
            if len(itemset) != len(previous):
                fitemsets += str(count)+"-"
                count = 1
            else:
                count += 1
            previous = itemset


        fitemsets += str(count)
    print(len(result), "|", fitemsets)

def main():
    """fpm/test.py

Requires:
../data/coursera/categories.txt file:
    File with database - each line is a transaction, items are separated by ";"
    For example:
        itemA; itemB; itemC
        itemB; itemD

../data/coursera/patterns.txt file:
    File containing right results - each line is a frequent itemset
    Lines have following format:
        support : itemX; itemY; itemZ

"""

    # File with database - each line is a transaction, items are separated by ";"
    # For example:
    # itemA; itemB; itemC
    # itemB; itemD
    # ifile = "../data/coursera/categories.txt"
    ifile = "allk.txt"

    # Read data in horizontal format
    t = time.time()
    data = []
    with open(ifile, "r") as f:
        for line in f:
            l = line.rstrip().split(',')
            data.append(l)

    print("Data load:", time.time() - t)
    #set the threshold
    threshold = 0.01 * len(data)

    t = time.time()
    result2 = list(utils.treeprojection(data, threshold,len(data)))
    print("TreeProjection:", time.time() - t)
    result2.sort(key=lambda item: (len(item), item))
    print_dist(result2)

    print(result2)


if "-h" in sys.argv or "--help" in sys.argv:
    print(main.__doc__)
else:
    main()