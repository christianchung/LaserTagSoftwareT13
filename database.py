import psycopg2
from psycopg2 import Error

class Database:

    def __init__(self):
        try:
            # Initialize variables used to get info from the database
            self.connection = None
            self.cursor = None
            self.record = None
            
            #Connects to database on Heroku
            self.connection = psycopg2.connect(user="aigprmbvspqgeb", 
                                        password="9fc89e2a58804e0d9132b626a88d1788e34c733bf9fed01188ad9c5726974632", 
                                        host="ec2-44-193-188-118.compute-1.amazonaws.com", 
                                        port="5432", 
                                        database="d2d6m26rbfjgmi")
            self.cursor = self.connection.cursor()
            
            # Initialize arrays used to store information
            self.id = []
            self.firstName = []
            self.lastName = []
            self.codeName = []
        except(Exception, Error) as error:
            print("Error while connecting to PostgreSQL.", error)

    def RetrieveInfo(self):
        try:
            # Execute SQL query and store all data from the player table into record
            query = "SELECT * from player"
            self.cursor.execute(query)
            self.record = self.cursor.fetchall()

            # Retrieves data from record and passes it into the info arrays
            for row in self.record:
                self.id.append(row[0])
                self.firstName.append(row[1])
                self.lastName.append(row[2])
                self.codeName.append(row[3])

        except(Exception, Error) as error:
            print("Error while executing query.", error)

    def insertFunction(self, Id, fn, ln, cn):
            try:
                insertQuery = "INSERT INTO PLAYER \nVALUES ( '" + str(Id) + "', '" + fn + "', '" + ln + "', '" + cn + "');"
                print(insertQuery)
                self.cursor.execute(insertQuery)
                self.connection.commit()
            except(Exception, Error) as error:
                print("Error with insert function. \n" , error)
            print("Insert successful")
            self.connection.commit()


    def deleteFunction(self, ID):
        try:
            deleteQuery = "DELETE FROM PLAYER WHERE ID='" + ID + "'"
            self.cursor.execute(deleteQuery)
            self.connection.commit()
        except(Exception, Error) as error:
            print("Error while passing in data to main program.", error)


    def LoadName(self, ID, largeTextBox):
        try:
            print(ID)
            query = "SELECT * FROM player WHERE ID = " + ID
            print(query)
            self.cursor.execute(query)
            record = self.cursor.fetchall()
            print(largeTextBox)
            print("record")
            print(record)
            largeTextBox[0] = record[0][3]
        except(Exception, Error) as error:
            largeTextBox[0] = ""
            print("Error while passing in data to main program.", error)

    def PassInformation(self, passID, passFirst, passLast, passCode):
        try:
            for x in self.id:
                passID.append(x)
            for x in self.firstName:
                passFirst.append(x)
            for x in self.lastName:
                passLast.append(x)
            for x in self.codeName:
                passCode.append(x)
        except(Exception, Error) as error:
            print("Error while passing in data to main program.", error)
        
        print("Data successfully passed to main program.")

    def CloseConnection(self):
        #Closes database connection
        if(self.connection):
            self.cursor.close()
            self.connection.close()
            print("PostgreSQL connection is closed")
