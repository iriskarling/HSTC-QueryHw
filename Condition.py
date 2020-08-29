#!/usr/bin/python  
#-*-  coding:GB2312  -*-
class Condition(object):
    def __init__(self,type,relationType,fieldName,value):
        self.type = type
        self.relationType = relationType
        self.fieldName = fieldName
        self.value = value
    def getRelationType(self):
        return self.relationType
    def setRelationType(self,relationType):
        self.relationType = relationType
    def getFieldName(self):
        return self.fieldName
    def setFieldName(self,fieldName):
        self.fieldName = fieldName
    def getValue(self):
        return self.value
    def setValue(self,value):
        self.value = value
    def getSQL(self):
        pass
    def getSQLandRCondition(self):
        return " " + self.relationType + " " + self.getSQL()


class ContainCondition(Condition):
    def __init__(self, type, relationType, fieldName, value):
        super().__init__(type, relationType, fieldName, value)
        self.type = type
        self.relationType = relationType
        self.fieldName = fieldName
        self.value = value
    def getSQL(self):
        return self.fieldName + "like" + "\%" + self.value +"%\'"

class EqualCondition(Condition):
    def __init__(self, type, relationType, fieldName, value):
        super().__init__(type, relationType, fieldName, value)
        self.type = type
        self.relationType = relationType
        self.fieldName = fieldName
        self.value = value
    def getSQL(self):
        return self.fieldName + ' = ' + self.value

class LargerCondition(Condition):
    def __init__(self, type, relationType, fieldName, value):
        super().__init__(type, relationType, fieldName, value)
        self.type = type
        self.relationType = relationType
        self.fieldName = fieldName
        self.value = value
    def getSQL(self):
        return self.fieldName + ' > ' + self.value

class SmallerCondition(Condition):
    def __init__(self, type, relationType, fieldName, value):
        super().__init__(type, relationType, fieldName, value)
        self.type = type
        self.relationType = relationType
        self.fieldName = fieldName
        self.value = value
    def getSQL(self):
        return self.fieldName + ' < ' + self.value

class LargerEqualCondition(Condition):
    def __init__(self, type, relationType, fieldName, value):
        super().__init__(type, relationType, fieldName, value)
        self.type = type
        self.relationType = relationType
        self.fieldName = fieldName
        self.value = value
    def getSQL(self):
        return self.fieldName + ' >= ' + self.value

class SmallerEqualCondition(Condition):
    def __init__(self, type, relationType, fieldName, value):
        super().__init__(type, relationType, fieldName, value)
        self.type = type
        self.relationType = relationType
        self.fieldName = fieldName
        self.value = value
    def getSQL(self):
        return self.fieldName + ' <= ' + self.value

class NotEqualCondition(Condition):
    def __init__(self, type, relationType, fieldName, value):
        super().__init__(type, relationType, fieldName, value)
        self.type = type
        self.relationType = relationType
        self.fieldName = fieldName
        self.value = value
    def getSQL(self):
        return self.fieldName + ' != ' + self.value

