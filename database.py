import psycopg2
from psycopg2 import Error

class Database:

    def __init__(self):
        try:
            # Initialize variables used to get info from the database
            self.connection = None
            self.cursor = None
            self.record = None
            
            #This identifies the database conneciton on Heroku
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
            # for row in self.record:
                # self.id.append(row[0])
                # self.firstName.append(row[1])
                # self.lastName.append(row[2])
                # self.codeName.append(row[3])
                # #when player team tag is added
                # #self.playerTeam.append(row[4]) #will also need to updated in the print statement below
            
            #Retrieves data from record and organizes each entry in order via id 
            for row in self.record:
                #no comparison for the first row needed. just append it.
                if row == 0:
                    self.id.insert(entry, row[0])
                    self.firstName.insert(entry, row[1])
                    self.lastName.insert(entry, row[2])
                    self.codeName.insert(entry, row[3])
                    #when player team tag is added
                    #self.playerTeam.insert(entry, row[4])
                    
                #subsequent rows are compared to previous entries
                else:
                    for entry in self.id:
                            #if id is smaller than first, new entry is the new first
                            if entry == 0:
                                if row[0] < self.id[entry]:
                                    self.id.insert(entry, row[0])
                                    self.firstName.insert(entry, row[1])
                                    self.lastName.insert(entry, row[2])
                                    self.codeName.insert(entry, row[3])
                                    #when player team tag is added
                                    #self.playerTeam.insert(entry, row[4])

                            #compare id to remainaing entries and fit it where it goes
                            elif entry > 0 and entry < self.id.length() - 1:
                                if row[0] < self.id[entry] and row[0] > self.id[entry - 1]:
                                    # if self.id[entry] > self.idToAdd and self.overflowIDs[indexTracker - 1] < self.idToAdd:
                                    #adds player info into slot based on ID (
                                    self.id.insert(entry, row[0])
                                    self.firstName.insert(entry, row[1])
                                    self.lastName.insert(entry, row[2])
                                    self.codeName.insert(entry, row[3])
                                    #when player team tag is added
                                    #self.playerTeam.insert(entry, row[4])
                                    
                            #if it's id is larger than all current entries, append() it to the end
                            else:
                                self.id.append(row[0])
                                self.firstName.append(row[1])
                                self.lastName.append(row[2])
                                self.codeName.append(row[3])
                                #when player team tag is added
                                #self.playerTeam.append(row[4]) #will also need to updated in the print statement below

                
            # Prints array contents/attributes to console)
            for x in range(len(self.id)):
                print(f" id: {self.id[x]} \n First Name: {self.firstName[x]} \n Last Name: {self.lastName[x]} \n Code Name: {self.codeName[x]} \n\n")
        except(Exception, Error) as error:
            print("Error while executing query.", error)

    def PassInformation(self, passID, passFirst, passLast, passCode):
        # Blank arrays are passed in from the main program and are filled in by
        # elements of the arrays storing info from the database
        try:
            for x in self.id:
                passID.append(x)
            for x in self.firstName:
                passFirst.append(x)
            for x in self.lastName:
                passLast.append(x)
            for x in self.codeName:
                passCode.append(x)
            #when player team tag is added
            #for x in self.playerTeam:
                #passTag.append(x)
        except(Exception, Error) as error:
            print("Error while passing in data to main program.", error)
        
        print("Data successfully passed to main program.")

    def CloseConnection(self):
        #Closes database connection
        if(self.connection):
            self.cursor.close()
            self.connection.close()
            print("PostgreSQL connection is closed")




# try:
    # #This identifies the database conneciton on Heroku
    # connection = psycopg2.connect(user="aigprmbvspqgeb", 
                                  # password="9fc89e2a58804e0d9132b626a88d1788e34c733bf9fed01188ad9c5726974632", 
                                  # host="ec2-44-193-188-118.compute-1.amazonaws.com", 
                                  # port="5432", 
                                  # database="d2d6m26rbfjgmi")

    # cursor = connection.cursor()

    # #print postgresql details
    # # print("PostgreSQL server information")
    # # print(connection.get_dsn_parameters(), "\n")

# #######################################################################################
    # #initialize arrays
    # # ARRAYS THAT STORE THE INFORMATION
    # id = []
    # firstName = []
    # lastName = []
    # codeName = []
# ##########################################################################################

    # #execute insert query
    # # insertQuery = "INSERT INTO player (id, first_name, last_name, codename) VALUES (2, 'Christian', 'Chung', 'danger');"
    # # cursor.execute(insertQuery)

    # #executing a SQL query
    # query = "SELECT * from player"
    # cursor.execute(query)
    # #stores all from player table in record
    # record = cursor.fetchall()
    
    # #retrieves from record and adds to the arrays
    # for row in record:
        # id.append(row[0])
        # firstName.append(row[1])
        # lastName.append(row[2])
        # codeName.append(row[3])

    # #prints to console the contents of all the arrays(the attributes)
    # for x in range(len(id)):
        # print(f" id: {id[x]} \n First Name: {firstName[x]} \n Last Name: {lastName[x]} \n Code Name: {codeName[x]} \n\n")

# #if fail to connect
# except(Exception, Error) as error:
    # print("Error while connecting to PostgreSQL", error)

# finally:
    # #closing database connection
    # if(connection):
        # cursor.close()
        # connection.close()
        # print("PostgreSQL connection is closed")