
import sys
import timeit
from optparse import OptionParser
from efficient_apriori.apriori import apriori
from efficient_apriori.rules import Rule
from efficient_apriori.itemsets import ItemsetCount


def dataFromFile(fname):
    """Function which reads from the file and yields a generator"""
    with open(fname, 'r') as file_iter:
        for line in file_iter:
            line = line.strip().rstrip(",")  # Remove trailing comma
            record = frozenset(line.split(","))
            yield record

if __name__ == "__main__":
    optparser = OptionParser()
    optparser.add_option(
        "-f", "--inputFile", dest="input", help="filename containing csv", default=None
    )
    optparser.add_option(
        "-s",
        "--minSupport",
        dest="minS",
        help="minimum support value",
        default=0.01,
        type="float",
    )
    optparser.add_option(
        "-c",
        "--minConfidence",
        dest="minC",
        help="minimum confidence value",
        default=0,
        type="float",
    )

    (options, args) = optparser.parse_args()

    inFile = None
    if options.input is None:
        inFile = sys.stdin
    elif options.input is not None:
        inFile = dataFromFile(options.input)
    else:
        print("No dataset filename specified, system with exit\n")
        sys.exit("System will exit")

    minSupport = options.minS
    minConfidence = options.minC

    start = timeit.default_timer()
    items, rules = apriori(inFile, minSupport, minConfidence)
    stop = timeit.default_timer()

    
    
    rules_rhs = filter(lambda rule: len(rule.lhs) == 1 and len(rule.rhs) == 1, rules)
    for rule in sorted(rules_rhs, key=lambda rule: rule.lift):
        print(rule)
    print('Time: ', stop - start)