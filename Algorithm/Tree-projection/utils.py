import csv
def frequentItems(database, threshold):
    """ Return dict where key is frequent item. And its value is
    support of the item. """

    supports = {}
    for itemset in database:
        for item in itemset:
            try:
                supports[item] += 1
            except KeyError:
                supports[item] = 1
    #print("supports:",supports)
    return dict(filter(lambda x: x[1] >= threshold, supports.items()))

def processNode(database, threshold, prefix,length):
    """ Process node of lexicographical tree determined by 'prefix'
    parameter. Run processing of subtrees by recursive calls. """
    sup_list = frequentItems(database, threshold)
    F1 = list(sup_list.keys())
    #print(threshold)
    #print("sup_list:",sup_list)
    #print("F1:",F1)
    for item in F1:
        new_prefix = prefix + (item,)
        #print("new_frefix:",new_prefix)
        #print("support = ",sup_list[item])
        with open(str(length)+".txt", 'a', encoding='utf-8') as f:
            st = ""
            st += str(sup_list[item])
            st += ":"
            for i in new_prefix:
                st += str(i)
                st += ";"
            st = st[:-1]
            f.write(st)
            f.write('\n')

        yield new_prefix

        new_database = []
        #print("database:", database)
        for transaction in database:
            if item in transaction:
                #print("transaction:",transaction)
                new_database.append([i for i in transaction if i > item and i in F1])
                #print(new_database)
        #print("new_database:",new_database)
        for itemset in processNode(new_database, threshold, new_prefix,length):
            #print("itemset:",itemset)
            yield itemset


def treeprojection(data, threshold,length):
    """ TreeProjection algorithm to find frequent itemsets


    Input:
    data - list of transactions, transaction contains items
    threshold - number of transactions to consider itemset as frequent

    Output:
    yields frequent itemsets (tuples)

    """
    return processNode(data, threshold, (),length)




