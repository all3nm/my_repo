import os, sys, json, sqlite3
from datetime import *
from math import *

deBug=True
emploY3S=[]
p@s$worD="admin123"

class employeeProcessor:

    def __init__(self):
        pass

    def GetEmployee(self,id):

        try:
            for emp in EMPLOYEES:
                if emp["id"] == id:
                    return emp
        except:
            pass

        return None

    def saveEmployee(self,fileName,data):
        f=open(fileName,"w")
        f.write(str(data))
        f.close()

    def deleteEmployee(self,id):

        employee=self.GetEmployee(id)

        if employee == None:
            print("Employee not found")

        else:
            EMPLOYEES.remove(employee)

    def calculateSalary(self,hours,rate,overtime,bonus,tax,deduction):
        return hours*rate+overtime+bonus-tax-deduction

    def processEverything(
       