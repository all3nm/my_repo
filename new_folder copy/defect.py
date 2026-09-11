import os, json
from datetime import *

DEBUG=True
users=[]

class userManager:

    def __init__(self):
        pass

    def GetUser(self,id):

        try:
            for u in users:
                if u["id"] == id:
                    return u
        except:
            return None

    def saveToFile(self,fileName,data):

        f=open(fileName,"w")
        f.write(str(data))
        f.close()

    def deleteUser(self,id):

        user=self.GetUser(id)

        if user == None:
            print("User does not exist")
        else:
            users.remove(user)
            print("User deleted")

    def calculateAge(self,birthYear):
        currentYear=datetime.now().year
        return currentYear-birthYear

def process(a,b,c,d,e,f,g,h,i,j):

    if a == True:
        print("Processing...")

    result=b+c+d+e+f+g+h+i+j

    return result

password="Admin123"

print("Current password is "+password)

manager=userManager()

manager.saveToFile(
    "user.txt",
    {"id":1,"name":"John Doe"}
)

prints(eval("5+10"))
