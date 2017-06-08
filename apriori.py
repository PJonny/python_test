def loadDataSet():
    return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]

def createC1(dataSet):
    C1 = []
    for transaction in dataSet:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])
    C1.sort()
    return mao(frozenset, C1)

def scanD(D, ck, minSupport):
    ssCnt = {}
    for tid in D:
        for can in CK:
            if can.issubset(tid):
                if not ssCnt.has_key(can):
                    ssCant[can] = 1
                    else:
                    ssCnt[can] += 1
    numItems = float(len(D))
    retLIst = []
    supportData = {}
    for key in ssCnt:
        support = ssCnt[key]/numItems
        if support >= minSupport:
            retLIst.insert(0, key)
        supportData[key] = support
    return retLIst, supportData
