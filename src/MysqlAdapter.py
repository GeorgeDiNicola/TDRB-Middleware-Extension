import mysql.connector
from mysql.connector import Error


class MysqlAdapter():

    def __init__(self, host, db, user):
        self.connection = None
        self.host = host
        self.database = db
        self.user = user
        #self.password = password

    # ref: https://realpython.com/python-mysql/
    def connect(self):
        
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user#,
                #password=self.password
            )
            if self.connection.is_connected():
                db_Info = self.connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = self.connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                print("You're connected to database: ", record)
                cursor.close()
        except Error as e:
            print("Error while connecting to MySQL", e)

    def send_query(self, q):
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(q)
                result = cursor.fetchall()
                return result
            except Error as e:
                print("Error while querying MySQL", e)

        
    def disconnect(self):
        if self.connection.is_connected():
            self.connection.close()
            print("MySQL connection is closed")