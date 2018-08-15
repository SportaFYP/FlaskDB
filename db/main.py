import sqlite3
from sqlite3 import Error 
 
 
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
      

def main():
    database = "C:\Users\L31104\Desktop\MQTT\db\pythonsqlite.db"
 
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        u integer PRIMARY KEY,
                                        tagId text NOT NULL,
                                        data text,
                                        quaternion text
                                        linearAcceleration integer NOT NULL,
                                        pressure text NOT NULL,
                                        coordinates text NOT NULL,
                                        acceleration text NOT NULL,
                                        metrics text NOT NULL
                                    ); """
 
    
    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)
        # create tasks table
        # create_table(conn, sql_create_tasks_table)
    else:
        print("Error! cannot create the database connection.")

        

if __name__ == '__main__':
    main()


