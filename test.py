#!/usr/bin/python  
#-*-  coding:GB2312  -*-
from Factory import Factory
from Condition import EqualCondition,LargerCondition,LargerEqualCondition,NotEqualCondition,SmallerCondition,SmallerEqualCondition,ContainCondition
from Query import Query

Operations = ["=",">",">=","<","<=","contains","!="]
OperationsName = ["equal","larger","largerE","smaller","smallerE","contain","notequal"]
property = ["CompanyName","Contact title","Phone"]
if __name__ == "__main__":
    try:
        query = Query("Customer")
        flag = True
        while flag:
            first = True
            while flag:
                for i in property:
                    print(i)
                idx = int(input("please chose the property: input the index of the number(1 or 2 or 3): ")) - 1
                ChoiceFiledName = property[idx]
                for i in Operations:
                    print(i)
                idx = int(input("please chose the operations: input the index of the number(1 - 7): ")) - 1
                ChoiceOperationName = OperationsName[idx]
                InputValue = input("please input the value: ")
                RelationType = "and"
                if first:
                    first = False
                else:
                    idx = int(input("pleae choice the logic: AND(0) OR (1) :"))
                    if idx == 1:
                        RelationType == "or"
                query.addCondition(ChoiceOperationName,RelationType,ChoiceFiledName,InputValue)

                idx =int(input("if you want to add more query condition please input 0 else input 1: "))
                if idx == 1:
                    break
            print(query.generateSQL())
            query.reset()
            idx =int(input("if you want to add more query please input 0 else input 1: "))
            if idx == 1:
                break
    except Exception as e:
        print("Unexpected input, please re-input！")
    finally:
        print("Bye, have a nice day:)")

            
