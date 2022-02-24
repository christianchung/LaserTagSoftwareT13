import psycopg2
from psycopg2 import Error

try:
    #This identifies the database conneciton on Heroku
    connection = psycopg2.connect(user="aigprmbvspqgeb", 
                                  password="9fc89e2a58804e0d9132b626a88d1788e34c733bf9fed01188ad9c5726974632", 
                                  host="ec2-44-193-188-118.compute-1.amazonaws.com", 
                                  port="5432", 
                                  database="d2d6m26rbfjgmi")

    cursor = connection.cursor()

    #print postgresql details
    # print("PostgreSQL server information")
    # print(connection.get_dsn_parameters(), "\n")

#######################################################################################
    #initialize arrays
    # ARRAYS THAT STORE THE INFORMATION
    id = []
    firstName = []
    lastName = []
    codeName = []
##########################################################################################

    #execute insert query
    # insertQuery = "INSERT INTO player (id, first_name, last_name, codename) VALUES (2, 'Christian', 'Chung', 'danger');"
    # cursor.execute(insertQuery)

    #executing a SQL query
    query = "SELECT * from player"
    cursor.execute(query)
    #stores all from player table in record
    record = cursor.fetchall()
    
    #retrieves from record and adds to the arrays
    for row in record:
        id.append(row[0])
        firstName.append(row[1])
        lastName.append(row[2])
        codeName.append(row[3])

    #prints to console the contents of all the arrays(the attributes)
    for x in range(len(id)):
        print(f" id: {id[x]} \n First Name: {firstName[x]} \n Last Name: {lastName[x]} \n Code Name: {codeName[x]} \n\n")

#if fail to connect
except(Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    #closing database connection
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

