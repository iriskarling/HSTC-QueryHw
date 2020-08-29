#!/usr/bin/python  
#-*-  coding:GB2312  -*-
from Condition import EqualCondition,LargerCondition,LargerEqualCondition,NotEqualCondition,SmallerCondition,SmallerEqualCondition,ContainCondition
class Factory:
    def setCondition(conditionType, relationType, fieldName, value):
        if conditionType == "equal":
            condition = EqualCondition(conditionType, relationType, fieldName, value)
        elif conditionType == "larger":
            condition = LargerCondition(conditionType, relationType, fieldName, value)
        elif conditionType == "largerE":
            condition = LargerEqualCondition(conditionType, relationType, fieldName, value)
        elif conditionType == "smaller":
            condition = SmallerCondition(conditionType, relationType, fieldName, value)
        elif conditionType == "smallerE":
            condition = SmallerEqualCondition(conditionType, relationType, fieldName, value)
        elif conditionType == "contain":
            condition = ContainCondition(conditionType, relationType, fieldName, value)
        elif conditionType == "notequal":
            condition = NotEqualCondition(conditionType, relationType, fieldName, value)
        return condition
