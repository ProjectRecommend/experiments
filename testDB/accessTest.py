from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
#from MetaData import ManageMetaData
from ManageLocalStorageModule import ManageLocalStorage
class accessTestDB:
    def __init__(self,connectionName):
        self.db=QSqlDatabase.database(connectionName,True)# the second parameter also opens the connection if the connection is not already open
        print("current connectionName:")
        print(self.db.connectionName())  
        self.query=QSqlQuery(self.db)
        self.songDet={}

    def read(self,songID):

        if self.db.isOpen():
            
            queryString="SELECT SID, SPath, isUpdated FROM songs WHERE SPath='hello'"
            record=self.query.exec_(queryString)
            
            if record:
                print ("read successfull, it seems")
                a=0
                while self.query.next():
                    print ("executing times: ")
                    print (a)
                    a=a+1
                    self.songDet["SID"]=self.query.value(0)
                    self.songDet["SPath"]=self.query.value(1)
                    self.songDet["isUpdated"]=self.query.value(2)
            else:
                print ("read not successfull")
                print ("error")
                print (self.query.lastError().text())
                return False
        else:
            print ("-----------------------------could not read from database, connection is not open------------------------")
            return False
        return self.songDet

    def write(self,songPath):
        
        #fucntion returns true if the writing is successfull
        if self.db.isOpen():
            queryString="insert into songs(SPath, isUpdated) values ('"+ songPath+"',0)"
            record=self.query.exec_(queryString)
            if record:
                print ("writing successfull")
                print ("no of rows affected: "+str(self.query.numRowsAffected()))
            else:
                print ("writing not successfull")
                print ("error")
                print (self.query.lastError().text())
                return False
        else:
            print ("-------------------------check the connection of the database----------------------------")
            return False
        
        return True
    def delete(self,songID):
        
        #function returns true if the record is successfully deleted

        if self.db.isOpen():
            queryString="delete from songs where SID="+str(songID)
            record=self.query.exec_(queryString)

            if record:
                print ("deletion successfull")
            else:
                print ("deletion not successfull")
                print ("error")
                print (self.query.lastError().text())
                return False
        else:
            print ("--------------------------check the connection of the database------------------------------------------")
            return False


        return True

"""
the following piece of code is only for debugging, remove or comment this out durinf release
"""
# objMan = ManageLocalStorage()
#objMan.setConnectionName('sqLiteConProjectRecommendConnection')
objMan=ManageLocalStorage(False,'sqLiteConProjectRecommendConnection')

print ("welcome accessTestDB terminal, commands: build, dump, connect, disconnect, read, write, delete,-1 for exiting ")
while True:
    x=str(input('input:'))
    if x=="build":
        test=objMan.build()
        if test:
            print ("build successfull")
        else:
            print ("build not successfull")
    elif x=="dump":
        test=objMan.dump()
        if test:
            print ("dump successfull")
        else:
            print ("dump not successfull")
    elif x=="connect":
        
        test=objMan.connect()
        print ("connected to database")
    elif x=="disconnect":
        test=objMan.disconnect()
        print ("database disconnected")
    elif x=="read":
        obj=accessTestDB(objMan.getConnectionName())
        print("enter a songID")
        songID=int(input("songID"))
        songDet=obj.read(songID)
        if type(songDet) is dict:
            print ("dictionary returned is:")
            print (songDet)
        else:
            print ("error: could not read from the database")
    elif x=="write":
        obj=accessTestDB(objMan.getConnectionName())
        print ("enter a songpath: ")
        songPath=str(input("songPath: "))
        test=obj.write(songPath)
        if test:
            print ("writing successfull")
        else:
            print ("writing not successfull")
    elif x=="delete":
        print ("enter a songID to delete: ")
        songID=int(input("songID: "))
        test=obj.delete(songID)
        if test:
            print ("deletion successfull")
        else:
            print ("deletion not successfull")
    elif x=="-1":
        break
    else:
        print ("invalid input")

