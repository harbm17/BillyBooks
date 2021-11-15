import psycopg2
from psycopg2 import Error


# this function is based on the tutorial at: https://pynative.com/python-postgresql-tutorial/
def connect_to_db(username='postgres', password='Password', host='127.0.0.1', port='5432', database='BillyBooks'):
    try:
        # Connect to an existing database
        connection = psycopg2.connect(user=username,
                                      password=password,
                                      host=host,
                                      port=port,
                                      database=database)

        # Create a cursor to perform database operations
        cursor = connection.cursor()
        #print("connected to the database")

        return cursor, connection

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)


def disconnect_from_db(connection, cursor):
    if (connection):
        cursor.close()
        connection.close()
        #print("PostgreSQL connection is closed.TESTING")
    else:
        print("Connection does not work.")

# run_sql(cursor,"select from;")
def run_and_fetch_sql(cursor, sql_string=""):
    try:
        # Executing a SQL query
        # cursor.execute("SELECT version();")
        # cursor.execute("SELECT * from customer;")
        cursor.execute(sql_string)
        # Fetch result
        # record = cursor.fetchone()
        # print("You are connected to - ", record, "\n")
        record = cursor.fetchall()
        # print("Here are the first 5 rows", record[:5])
        return record
    except (Exception, Error) as error:
        print("Errors while executes the code: ", error)
        return -1

def runSQL(cursor, sql_string=""):
    try:
        cursor.execute(sql_string)
        return 1
    except (Exception, Error) as error:
        print("Errors while executes the code: ", error)
        return -1

def genreAssign(num):
    if num == 0:
        return "history, historical fiction, biography"
    elif num == 1:
        return "fiction"
    elif num==2:
        return "fantasy, paranormal"
    elif num==3:
        return "mystery, thriller, crime"
    elif num==4:
        return "poetry"
    elif num==5:
        return "romance"
    elif num==6:
        return "non-fiction"
    elif num==7:
        return "children"
    elif num==8:
        return "young-adult"
    elif num==9:
        return "comics, graphic"

def runnerSQL(cursor, sql_string=""):
    cursor.execute(sql_string)
    return




class DatabaseConnection:
    def __init__(self, username, password, host, port, database):
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        print(self.username)
        self.connection = psycopg2.connect(user=self.username,
                                           password=self.password,
                                           host=self.host,
                                           port=self.port,
                                           database=self.database)
    
    # Create the tables in the database if they don't already exist.
    def setup_database(self):
        print("============================")
        
        with self.getCursor() as cur:
            cur.execute("""
                SELECT table_name FROM information_schema.tables
                WHERE table_schema = 'public'
                """)
            records = cur.fetchall()
            if len(records) == 0:
                # Create the tables that we need.
                # TODO: ADD THE REST OF OUR TABLES.
                cur.execute("""
                    CREATE TABLE users (
                        id serial PRIMARY KEY,
                        username varchar(255) UNIQUE NOT NULL,
                        password varchar(255) NOT NULL
                    )
                """)
                self.connection.commit()
                print("Created new table")
            else:
                # List the tables that exist
                print(f"Table exists already(count): {len(records)}")
                for record in records:
                    print(record)
        print("============================")

    def getCursor(self):
        return self.connection.cursor()

    def runSQL(self, sql_string):
        try:
            with self.getCursor() as cur:
                cur.execute(sql_string)
                return True
        except Exception as e:
            print("Errors while executes the code: ", e)
            return False

    def runAndCommitSQL(self, sql_string):
        try:
            with self.getCursor() as cur:
                cur.execute(sql_string)
                self.connection.commit()
                return True
        except Exception as e:
            print("Errors while executes the code: ", e)
            return False

    def runAndFetchSQL(self, sql_string):
        try:
            with self.getCursor() as cur:
                cur.execute(sql_string)
                record = cur.fetchall()
                return record
        except (Exception, Error) as error:
            print("Errors while executes the code: ", error)
            return None
