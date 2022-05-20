from fpgrowth import fpgrowth
import csv



#the main step to implement the algorithm
if __name__ == "__main__":
    var = []
    minSupRatio = 0.001
    # num_ls = [500000*1, 500000*2, 500000*3, 500000*4, 500000*5, 500000*6]
    for T_Num in [3346083]:
        fileName = 'product_name_set.csv'
    # for T_Num in [5]:
        #fileName = 'test_data.csv'
        freqItemSet, rules, T1, T2, T3 = fpgrowth(fileName, minSupRatio, T_Num)
        runtime = str((T3 - T1).seconds)
        mining_time = str((T3 - T2).seconds)
        mining_time_peritemset = str(float((T3 - T2).seconds)/float(len(freqItemSet)))
        itemset_num = len(freqItemSet)
        # sort by confidence
        rules = sorted(rules, key=lambda x: x[2], reverse=True)
        # print(freqItemSet)
        # print(rules)
        var.append(T_Num)
        var.append(str(minSupRatio))
        var.append(runtime)
        var.append(mining_time)
        var.append(itemset_num)
        var.append(mining_time_peritemset)

        with open("result.csv", "a", newline='') as csvfile:
            write = csv.writer(csvfile)
            write.writerow(var)

        fileItemset = str(T_Num) + ' ' + 'freqItems.csv'

        with open(fileItemset, "w", newline='') as csvfile:
            for i in freqItemSet:
                csvfile.write(str(i))
                csvfile.write('\n')

        with open("rules.csv", "w", newline='') as csvfile:
             writer = csv.writer(csvfile)
             writer.writerows(rules)

        print("Transaction Number: %d" % T_Num)




