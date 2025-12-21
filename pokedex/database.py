'''Module for managing the Pokemon database using SQLite.'''

import sqlite3
from validation.sql_statements import *

class Database():
    
    def __init__(self):
        self.database_name = "pokemon_database.db"

    def connectdb(self) -> sqlite3.Connection:
        '''Establish a connection to the SQLite database'''
        try:
            db_connection = sqlite3.connect(self.database_name) # Connect to the SQLite database
        except sqlite3.Error as e:
            print(f"Database connection error: {e}")

        return db_connection

    def execute(self,*args:tuple) -> None:
        '''Execute a SQL statement with optional values'''
        with self.connectdb() as connection: # Context manager to ensure connection is closed
            cursor = connection.cursor()
            cursor.execute(*args)
            connection.commit()

    def fetchone(self, sql_statement, *args):
        '''Fetch a single record from the database'''
        with self.connectdb() as connection:
            cursor = connection.cursor()
            cursor.execute(sql_statement,*args)
            result = cursor.fetchone()
        return result

    def create_table(self):
        '''Create the pokemon table if it doesn't exist'''
        try:
            self.execute(CREATE_POKEMON_TABLE)
        except sqlite3.Error as e:
            raise e

    def create_stats_table(self):
        '''Create the stats table if it doesn't exist'''
        
        try:
            self.execute(CREATE_STATS_TABLE) 
            self.execute(POPULATE_STATS) # Populate stats table after creation
        except sqlite3.Error as e: 
            raise e
       
    def update_stats(self, pkmn):
        '''Update a Pokemon's stats in the database'''
        self.create_stats_table()  # Ensure the stats table exists
        VALUES = pkmn.stats# Prepare the values for the SQL statement
        try:  
            self.execute(UPDATE_STATS, (*VALUES,pkmn.number))
        except sqlite3.Error as e:
            raise sqlite3.Error(f"The stats could not be updated. Error: {e}")

    def add_pokemon(self, pkmn):
        '''Add a new Pokemon to the database'''
        self.create_table()  # Ensure the pokemon table exists
        VALUES = (pkmn.name, pkmn.number, pkmn.type1, pkmn.type2, pkmn.ability1, pkmn.ability2, pkmn.hidden_ability)

        try:
            self.execute(ADD_POKEMON, VALUES) # Execute the insert statement and values
            self.create_stats_table()  # Ensure the stats table exists
        except sqlite3.Error as e:
            raise e


    '''Check if a Pokemon exists in the database by name or number'''
    def exists_in_db(self, identifier):
        '''Check if a Pokemon exists in the database by name or number'''
        try:
            count = self.fetchone(GET_STATUS, (identifier, identifier))[0]
            return count > 0 # Return True if exists, False otherwise
        except sqlite3.Error as e:
            print(f"Database error: {e}")

    def get_stats(self, identifier):
        '''Get a Pokemon's stats from the database'''
        try:
            result = self.fetchone(GET_STATS, (identifier,)) # Fetch the stats by Pokemon number
        except sqlite3.Error as e:
            raise e
        return result
    
    def get_pokemon (self, identifier):
        '''Get a Pokemon's full details including stats from the database'''

        try:
            result = self.fetchone(GET_POKEMON, (identifier, identifier)) # Fetch the full Pokemon details by name or number
        except sqlite3.Error as e:
            raise e
 
        return result



