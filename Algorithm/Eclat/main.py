#library
import numpy as np
import pandas as pd
import csv
import time
df_id = pd.read_csv('id.csv')
df_id = df_id.head(n=3000000)
data_ls = df_id.to_dict()['product_id']
for i in list(data_ls.keys()):
        data_ls[i]=data_ls[i].split(',')


def convert(data):
    """将水平数据格式转换为垂直数据格式"""
    data_vert = {}
    for tid,items in data_ls.items():
        for item in items:
            if frozenset({item}) not in data_vert:
                data_vert[frozenset({item})] = {tid}
            else :
                data_vert[frozenset({item})].add(tid)
    return data_vert


def drop_data(data):
    """根据阈值删除掉不频繁的项"""
    res = data.copy()
    for key in data :
        if len(data[key])<threshold_val:
            del res[key]
    return res





def aprioriGen(Lk_1, k):  # creates Ck
    """ 根据k-1项集产生候选k项集
    Lk_1: k-1项集的列表
    k: k项集的k
    """
    res = {}
    lenLk_1 = len(Lk_1)  # k-1项集的长度
    for i in range(lenLk_1):
        for j in range(i + 1, lenLk_1):
            L1 = sorted(list(Lk_1[i]))  # k等于2时, 1项集取空, k等于3时,2项集取第一个元素, k等于4时,3项集取前两个元素
            L2 = sorted(list(Lk_1[j]))  # k等于2时, 1项集取空, k等于3时,2项集取第一个元素, k等于4时,3项集取前两个元素

            if L1[:k - 2] == L2[:k - 2]:  # 如果前k减2个元素相等 , 就将两几何求并
                res[Lk_1[i]|Lk_1[j]]=[Lk_1[i],Lk_1[j]]  # set union

    return res




def get_support(candidate_k_1,vert):
    """通过求交集获得候选k项集的支持度,并因此获得k项集"""
    res = {}
    for key,items in candidate_k_1.items():
        item1,item2 = items
        ss = vert[item1]&vert[item2]

        res[key] = ss
    return res



threshold_val = 30000
# 将水平数据格式转换为垂直数据格式
data_vert = convert(data_ls)
# 删除不满足最小支持度的项
data_vert = drop_data(data_vert)
# 得到频繁一项集 L1
L1 = [frozenset(key) for key in data_vert.keys()]
print('L1:',L1)

res = []
res.append(L1)
# 获得候选2项集
candidate = aprioriGen(L1, k=2)
i=1
combo={}
def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res
while len(candidate):
    # print(f'data_vert{i}:', data_vert)
    combo=Merge(combo,data_vert)
    i+=1
    # 对候选2项集通过求交集计算支持度
    data_vert = get_support(candidate,data_vert)
    # 删除不满足支持度的项, 得到频繁2项集
    data_vert = drop_data(data_vert)
    if len(data_vert):
        L = [frozenset(key) for key in data_vert.keys()]
        res.append(L)
        # print(f'L{i}:',L)
        candidate = aprioriGen(L, k=2)
    else:
        for i in list(combo.keys()):
            combo[i]=len(list(combo[i]))/len(data_ls)

        df = pd.DataFrame.from_dict(combo, orient='index',columns=['support'])
        df['id']=list(df.index)
        df = df.loc[:, ['id', 'support']]
        df.to_csv('support.csv',index=False)
        break


# # combos_to_counts=sorted(combos_to_counts.items(), key=lambda item:item[1],reverse=True)


