#-*- coding:utf-8 -*-
"""
author:zx
"""
import os
from common import dbase
# 挖掘哪个表就将sql 切换为哪一个，如sql = project_sql 即挖掘的project信息表
from conf.sql import project_sql
from conf.sql import projectMoney_and_project_sql
from conf.sql import paper_sql
from conf.sql import patent_sql
from apriori import *

class wordAnalysis():
    def __init__(self):
        self.DBASE = dbase.dbase()

    def readData(self):
        """
        读取数据库中的数据
        """
        sql = project_sql
        Data = self.DBASE.readSqlServerDb(sql)
        return Data

def processApriori(data,minSupport = 0.5,minConf=0.5):
    '''
    data: 数据集，list格式
    minSupport: 词语组合的最小频率
    minConf: 规则最小置信度，默认为0.5
    '''
    L, suppData = apriori(data, minSupport)
    rules = generateRules(L, suppData, minConf)
    return L,suppData,rules


if __name__ =="__main__":
    initProcess = wordAnalysis()
    Data = initProcess.readData()
    sentence_list = []
    word_list = []
    for sentence in Data:
        tempList = []
        for i in sentence:
            if i:
                temp = i.split(',')
                for j in temp:
                    if j:
                        tempList.append(j)
        word_list.append(tempList)
    # print(len(word_list))
    # 输入参数三个，数据集，最小频繁度，最小置信度
    L, suppData, rules = processApriori(word_list, 0.4,0.5)
    L_temp = []
    for i in L:
        temp = []
        for j in i:
            temp.append(set(j))
            # print(set(j))
        L_temp.append(temp)

    value_list = list(suppData.values())
    keys_list = list(suppData.keys())
    suppData_temp = {}
    for i ,j in zip(keys_list,value_list):
        name = str(set(i))
        suppData_temp[name] = round(j,2)


    print('\n'+"-------------------频繁项集------------------")
    print( L_temp)
    print('\n'+"----------所有候选项集的支持度信息-------------")
    print(suppData_temp)
    print('\n'+"---------'所有满足置信度要求的规则'------------")
    print(rules)



