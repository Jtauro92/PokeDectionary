'''Module for managing the Pokemon database using SQLite.'''

import sqlite3

class Database():
    
    def __init__(self):
        self.database = "pokemon_database.db"


    '''Connect to the database'''
    def connectdb(self):
        try:
            db_connection = sqlite3.connect(self.database) # Connect to the SQLite database
        except sqlite3.Error as e:
            print(f"Database connection error: {e}")

        return db_connection

    '''Execute a SQL statement with optional values'''
    def execute(self,sql_statement,value):
        with self.connectdb() as connection: # Context manager to ensure connection is closed
            cursor = connection.cursor()
            cursor.execute(sql_statement,value)
            connection.commit()

    '''Fetch one record from the database'''
    def fetchone(self,sql_statement,value):
        with self.connectdb() as connection:
            cursor = connection.cursor()
            cursor.execute(sql_statement,value)
            result = cursor.fetchone()
        return result

    '''Create the Pokemon table if it doesn't exist'''
    def create_table(self): 
        try:
            self.execute('''CREATE TABLE IF NOT EXISTS pokemon (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT NOT NULL,
                                    number INTEGER NOT NULL,
                                    type1 TEXT NOT NULL,
                                    type2 TEXT,
                                    ability1 TEXT NOT NULL,
                                    ability2 TEXT,
                                    hidden_ability TEXT
                                )''')
        except sqlite3.Error as e:
            raise e
    

    def create_stats_table(self):
        '''Create the stats table if it doesn't exist'''
        populate_sql = '''INSERT INTO stats (number, hp, atk, def, spatk, spdef, speed)'''
        try:
            self.execute('''CREATE TABLE IF NOT EXISTS stats 
                                    number INTERGER PRIMARY KEY,
                                    hp INTEGER NOT NULL,
                                    atk INTEGER NOT NULL,
                                    def INTEGER NOT NULL,
                                    spatk INTEGER NOT NULL,
                                    spdef INTEGER NOT NULL,
                                    speed INTEGER NOT NULL''' )
        except sqlite3.Error as e: 
            raise e
        try:
            self.populate_stats() # Populate stats table after creation
        except sqlite3.Error as e:
            raise e("The stats table could not be populated after creation.")



    '''Populate stats stats number column from pokemon table'''
    def populate_stats(self):
        '''Populate the stats table with Pokemon numbers from the pokemon table'''
        sql_statement = '''INSERT OR IGNORE INTO stats (number)
                           SELECT number FROM pokemon'''

        self.execute(sql_statement, ()) # Execute the insert statement


    '''Update Pokemon stats in the database'''
    def update_stats(self, identifer, hp, atk, defn, spatk, spdef, speed):
        '''Update a Pokemon's stats in the database'''
        self.create_stats_table()  # Ensure the stats table exists
        VALUES = (hp, atk, defn, spatk, spdef, speed, identifer, identifer)
        sql_statement = '''UPDATE stats 
                           SET hp = ?, atk = ?, def = ?, spatk = ?, spdef = ?, speed = ? 
                           WHERE name = ? or number = ?'''
        try:
            self.execute(sql_statement, VALUES) # Execute the update statement and values
        except sqlite3.Error as e:
            raise f"The stats could not be updated. Error: {e}"


    def add_pokemon(self, name, number, t1, t2, a1, a2, ha):
        '''Add a new Pokemon to the database'''
        self.create_table()  # Ensure the pokemon table exists
        VALUES = (name, number, t1, t2, a1, a2, ha)
        sql_statement = '''INSERT INTO pokemon (name, number, type1, type2, ability1, ability2, hidden_ability)
                           VALUES (?, ?, ?, ?, ?, ?, ?)'''

        try:
            self.execute(sql_statement, VALUES) # Execute the insert statement and values
        except sqlite3.Error as e:
            raise f"The pokemon could not be added. Error: {e}"


    '''Check if a Pokemon exists in the database by name or number'''
    def exists_in_db(self, identifier):
        sql_search = '''SELECT COUNT(*) FROM pokemon WHERE name = ? OR number = ?'''
        try:
            count = self.fetchone(sql_search, (identifier, identifier))[0]
            return count > 0 # Return True if exists, False otherwise
        except sqlite3.Error as e:
            print(f"Database error: {e}")


    def get_pokemon(self, identifier):
        '''Get a Pokemon's details from the database'''
        sql_search = '''SELECT name, number, type1, type2, ability1, ability2, hidden_ability 
                        FROM pokemon 
                        WHERE name = ? OR number = ?'''

        try:
            result = self.fetchone(sql_search, (identifier, identifier)) # Fetch the Pokemon details by name or number
        except sqlite3.Error as e:
            raise e
 
        return result

    def get_full_pokemon (self, identifier):
        '''Get a Pokemon's full details including stats from the database'''
        sql_search = '''SELECT p.name, p.number, p.type1, p.type2, p.ability1, p.ability2, p.hidden_ability,
                               s.hp, s.atk, s.def, s.spatk, s.spdef, s.speed
                        FROM pokemon p
                        JOIN stats s ON p.number = s.number
                        WHERE p.name = ? OR p.number = ?'''
        try:
            result = self.fetchone(sql_search, (identifier, identifier)) # Fetch the full Pokemon details by name or number
        except sqlite3.Error as e:
            raise e
 
        return result
    

if __name__ == "__main__":
    print(Database().get_pokemon('pikachu'))

