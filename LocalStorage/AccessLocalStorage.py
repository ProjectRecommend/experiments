
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from MetaData import ManageMetaData
import ManageLocalStorage

class AccessLocalStorage:


    def __init__(self):
        self.db=QSqlDatabase.database(ManageLocalStorage.getConnectionName(),True)# the second parameter also opens the connection if the connection is not already open
        self.query=QSqlQuery(self.db)

    # so basically querying on the instance of the database mentioned earlier

    """
    The database function simply returns an instance of the connection given the connection name. The second parameter is a boolean
    value that tells us whether the connection is open or not, if the connection is not already open, it is opened now.
    """

    def Read(self,SongID):

        songDet={}

        if self.db.isOpen():
            
            """
            QSqlQuery(const QString &query = QString(), QSqlDatabase db = QSqlDatabase())
            accepts a query string and a database instance (of class QSqlDatabase) and the object can be 
            used for simply navigating the record(if select statement is used).
            """
            record=QSqlQuery("SELECT * FROM songs WHERE SongID="+SongID,self.db)

            #now we can use record object (which is an QSqlQuery object) to navigate the record

        else:
            print ("could not read from the database, connection not found")
        """
        populating the dictionary songDet
        """
        songDet["SPath"]=record.value(1)
        songDet["isUpdated"]=record.value(2)
        songDet["TIT2"]=record.value(3)
        songDet["TALB"]=record.value(4)
        songDet["TPE1"]=record.value(5)
        songDet["TPE2"]=record.value(6)
        songDet["TSOP"]=record.value(7)
        songDet["TDRC"]=record.value(8)
        songDet["TCON"]=record.value(9)

        print "the songDet dictionary is:"+songDet

        return songDet

        
    """
    the following function writes song details, like its metadata and so on into the database, it is
    passed the songPath only, it calls the function ReadMetaData which returns a dictionary containing key value 
    pairs of the songMetadata
    """

    def Write(self, SongPath):

        songDet={}
        songDet= ManageMetaData.ReadMetaData(SongPath) #this will read metadata songPath.

        """
        the songDet format is always the same
        """ 
        valuesList=songDet.values()    
        valuesString="" 
        for i in range(9):
            if not i==8:
                valuesString=valuesString+valuesList[i]+","
            else:
                valuesString=valuesString+valuesList[i]
        queryString="insert into songs (SPath,isUpdated,TIT2,TALB,TPE1,TPE2,TSOP,TDRC,TCON)values("+valuesString+")"
        isQuerySuccessful=query.exec_(queryString); 
        if isQuerySuccessful:
            print ("----------------------------------------------")
            print ("insertion successful")
        else:
            print ("----------------------------------------------")
            print ("insertion not successful")
        return True
    
    def Delete(self, SongID):
    
        isQuerySuccessful=query.exec_("delete from songs WHERE SID="+SongID)
        if isQuerySuccessful:
            print ("----------------------------------------------")
            print ("deletion successful")
        else:
            print ("----------------------------------------------")
            print ("could not delete")

        return True

    def getSongPath(self):
    
        return SongPath

    def setSongPath(self,SongPath):

         self.songPath=songPath
    """
    the following function is only for the purpose of testing purspose, delete this fucntion for release
    """
    def testQueries(self,queryInstance,query):
        
        queryInstance.exec_(query);

print ("Welcome to AccessLocalStorage terminal, this terminal lets you build a database with song table and read and write data to it")
print ("commands: build, dump, disconnect, connect, read, write, delete")
a=AccessLocalStorage("C:/helloworld")


