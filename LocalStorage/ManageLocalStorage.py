
import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

class ManageLocalStorage:

    def __init__(self,isConnected,connectionName):
        
        self.isConnected=isConnected
        self.connectionName=connectionName


    """
        QSqlDatabase is a class that has a static public member function called addDatabase that simply adds a database given the 
        driver type and the connection name. If there already exists a connection by the connection name provided in the function, that 
        connection is removed.

        the object db now has a few functions of its own that we can work on.
        setDatabaseName(), setUserName(), setPassword(), setHostName(), setPort(), setConnectOptions() and finally open(). 
        working of the functions is self-explanatory

        if no connection name is specified the new connection becomes the default connection

        if we add a connection with the same name as the existing connection the new connection replaces the old one.
    """
            
    def getIsConnected(self):
        
        return self.isConnected

    def setIsConnected(self, isConnected):
        
        self.isConnected = isConnected


    def Build(self):
        db = QSqlDatabase.addDatabase('QSQLITE',self.connectionName)
        
        db.setDatabaseName('ProjectRecommendDatabase')
        db.setUserName('ProjectRecommend')
        db.setPassword('elite1337')
        db.setPort(1337)

        """
        Error testing : whether the creation of database and opening of connection is successful or not
        """

        if not db.open():
            # db.open() returns true if the connection is open obviously
            print ("----------------------------------------------")
            print ("could not open the database")
            return False
        else:
            print ("----------------------------------------------")
            print ("opened the database successfully")
            self.isConnected=True

            #db=QSqlDatabase.database(self.connectionName)

            query = QSqlQuery(db)
           
            isQuerySuccessful=query.exec_("create table songs(SID int auto_increment primary key , SPath varchar(255), isUpdated int, TIT2 varchar(255), TALB varchar(255), TPE1 varchar(255), TPE2 varchar(255), TSOP varchar(255), TDRC date, TCON varchar(255))")
            
            """
            isDeleteSuccessful=query.exec_("drop table if exists test")
            if isDeleteSuccessful:
                print ("table test dropped")
            else:
                print ("table could not be dropped:")
                print (query.lastError().text())
            isQuerySuccessful=query.exec_("create table test(SID int auto_increment primary key ,SPath varchar(255))")
            """

            # the fieldnames used here in the query are described in dbFields.md file in the same directory
            #know that this is how error information is grabbed in pyqt: QSqlDatabase
            
            """
            Error testing: whether the creation of the table is successful or not
            """

            if isQuerySuccessful:
                print("----------------------------------------------")
                print ("creation of table successful")

                #now that we have acatually created a table let us try inserting entries into that table
            else:
                print ("----------------------------------------------")
                print ("creation of table unsuccessful")
                error=query.lastError().text()
                print (error)   
            
            return True

    """
    build is working fine
    """

    """
    dumps the database
    returns true if the database exists and the database is successfully dumped
    returns false if the database does not exists 
    """

    def Dump(self):
        db=QSqlDatabase.database(self.connectionName)
        #QSqlDatabase.database(<connection name >) gives us an instance of the QSqlDatabase for the connection given as a parameter
        if self.getIsConnected():
            print("database was connected")

            self.Disconnect()#disconnecting the database first and then attempting remove

            if db.isOpen():
                print ("connection is still open bro")
            
            isDatabaseRemoved=db.removeDatabase(self.connectionName)
            
            """
            Error testing
            """

            if isDatabaseRemoved:
                print ("----------------------------------------------")
                print ("database removed")
            else:
                print ("----------------------------------------------")
                print ("database could not be removed: ")
                print (db.lastError().text())
                return False
        else:
            print("database was not connected")
            #simply opening the connection

            isDatabaseRemoved=db.removeDatabase(self.connectionName)

            if isDatabaseRemoved:
                print ("----------------------------------------------")
                print ("database removed")
            else:
                print ("----------------------------------------------")
                print ("database could not be removed: ")
                print (db.lastError().text())
                return False
        return True
    
    def Connect(self):
        db=QSqlDatabase.database(self.connectionName)
        # creating instance of the QSqlDatabase class, does not refer to any particular database
        if not self.getIsConnected():
            db.open()
            #opens the connection
        else:
            return False
        return True

    def Disconnect(self):
        db=QSqlDatabase.database(self.connectionName)
        # creating instance of the database

        if self.getIsConnected():
            print ("closing the connection")
            db.close()
            print ("closed")
            #closes the connection
            self.setIsConnected(False)
        else:
            return False
        return True

"""
error correction code follows, do not use during final implementation
"""

print ("Welcome to ManageLocalStorage, here are the following sets of commands: build, dump, connect, disconnect,-1 exiting")
obj=ManageLocalStorage(False,'sqLiteConProjectRecommend') 
while True:
    
    x=str(input('input:')) # this is some python 3 stuff.
    
    if x=="build":
        if obj.Build():
            print ("---------------------------------Success------------------------------")
        else:
            print ("---------------------------------Fail----------------------------------")
    elif x=="dump":
        if obj.Dump():
            print ("---------------------------------Success------------------------------")
        else:
            print ("---------------------------------Fail------------------------------")
    elif x=="connect":
        if obj.Connect():
            print ("---------------------------------Success------------------------------")
        else:
            print ("---------------------------------Fail------------------------------")
    elif x=="disconnect":
        if obj.Disconnect():
            print ("---------------------------------Success------------------------------")
        else:
            print ("---------------------------------Fail------------------------------")
    elif x=="-1":
        break
    else:
        print ("incorrect command")
        

        
        
