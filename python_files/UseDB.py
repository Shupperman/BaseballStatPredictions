import sqlite3
import pandas as pd
from python_files.Queries import Queries


class UseDB:
    """
    Class that holds functionality to use SQL queries with a SQLite Database
    """
    def __init__(self, connection):
        """
        Constructor of the UseDB class.
        :param connection: SQLite `connection` object.
        """
        self.connection = connection

    def create_new_table(self, query):
        """
        Creates a new table in the database.
        :param query: Query to be performed.
        :return: None
        """
        # Cursor object that will be used to run the SQL insert queries
        cursor = self.connection.cursor()

        # Run the query
        cursor.execute(query)

        # Commit the query to the database
        self.connection.commit()
        print("The new table has been created.")

        # Close the cursor object
        cursor.close()

    def insert_into_table(self, query, info_dict):
        """
        Inserts a single record into a table.
        :param query: Query to be performed.
        :param info_dict: Dictionary of values that will be inserted into table.
        :return: None.
        ToDo: Some kind of error checking to ensure there are not duplicate records
        ToDo: Make each table get its own functions for inserting and reading, We will
              need this because of the different checks that will need to be completed
              before inserting into the different tables.
        """

        # Cursor object that will be used to run the SQL insert queries
        cursor = self.connection.cursor()

        # Turn the dictionary into a tuple
        player_tuple = tuple(info_dict.values())

        try:
            # Execute the query
            cursor.execute(query, player_tuple)

            # Commit the query to the database
            self.connection.commit()
            print(f"Data added to database.")
        except sqlite3.IntegrityError:
            print("Data already exists with this primary key. Cannot be added.")
        except sqlite3.ProgrammingError:
            print("This game was probably postponed, no data to enter.")
        except IndexError:
            print("There is some other error. Carry on.")

        # Close the cursor object
        cursor.close()

    def retrieve_from_table(self, query):
        """
        Runs a select query to retrieve data from the db.
        :param query: Query to be performed.
        :return: Pandas DataFrame of the query results.
        """
        # ToDo: Perhaps change to pd.read_sql(query, con=cnx) for getting data

        # Cursor object that will be used to run the SQL insert queries
        cursor = self.connection.cursor()

        # Execute the retrieve query
        cursor.execute(query)

        # fetch the results and store them in a Pandas dataframe
        results = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
        print("The query results have been retrieved.")

        # Close the cursor object
        cursor.close()

        return results
