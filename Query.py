#!/usr/bin/python  
#-*-  coding:GB2312  -*-
from Factory import Factory

class Query(object):
    def __init__(self,queryObject,queryCondition = []):
        self.queryObject =queryObject
        self.queryCondition = queryCondition
  

    def addCondition(self,type,relationType,fieldName,value):
        condition = Factory.setCondition(type, relationType, fieldName, value)
        condition.setRelationType(relationType)
        condition.setFieldName(fieldName)
        condition.setValue(value)
        self.queryCondition.append(condition)
        

    def generateSQL(self):
        if self.queryCondition == None or self.queryCondition == None:
            return ""
        base_sql = "select * from " + self.queryObject + " where "
        init = True
        for i in self.queryCondition:
            if init:
                base_sql += i.getSQL()
                init = False
            else:
                base_sql += i.getSQLandRCondition()
        base_sql += ";"
        return base_sql


    def reset(self):
        self.queryCondition = []

