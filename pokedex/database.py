'''Module for managing the Pokemon database using SQLite.'''

import sqlite3

class Database():
    
    def __init__(self):
        self.database = "pokemon_database.db"

    def connectdb(self):
        '''Establish a connection to the SQLite database'''
        try:
            db_connection = sqlite3.connect(self.database) # Connect to the SQLite database
        except sqlite3.Error as e:
            print(f"Database connection error: {e}")

        return db_connection

    def execute(self,*args):
        '''Execute a SQL statement with optional values'''
        with self.connectdb() as connection: # Context manager to ensure connection is closed
            cursor = connection.cursor()
            cursor.execute(*args)
            connection.commit()

    def fetchone(self,sql_statement,value):
        '''Fetch a single record from the database'''
        with self.connectdb() as connection:
            cursor = connection.cursor()
            cursor.execute(sql_statement,value)
            result = cursor.fetchone()
        return result

    def create_table(self):
        '''Create the pokemon table if it doesn't exist'''
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
        
        try:
            self.execute('''CREATE TABLE IF NOT EXISTS stats( 
                                    number INTEGER PRIMARY KEY,
                                    hp INTEGER,
                                    atk INTEGER,
                                    def INTEGER,
                                    spatk INTEGER,
                                    spdef INTEGER,
                                    speed INTEGER,
                                    FOREIGN KEY(number) REFERENCES pokemon(number)
                            )''') 
            populate_sql = '''INSERT OR IGNORE INTO stats (number)
                              SELECT number FROM pokemon'''
            self.execute(populate_sql)# Populate stats table after creation
        except sqlite3.Error as e: 
            raise e
       
    def update_stats(self, number, hp, atk, defn, spatk, spdef, speed):
        '''Update a Pokemon's stats in the database'''
        self.create_stats_table()  # Ensure the stats table exists
        VALUES = (hp, atk, defn, spatk, spdef, speed, number)
        sql_statement = '''UPDATE stats 
                            SET hp = ?, atk = ?, def = ?, spatk = ?, spdef = ?, speed = ? 
                            WHERE number = ?'''
        try:  
            self.execute(sql_statement, VALUES)
        except sqlite3.Error as e:
            raise sqlite3.Error(f"The stats could not be updated. Error: {e}")

    def add_pokemon(self, name, number, t1, t2, a1, a2, ha):
        '''Add a new Pokemon to the database'''
        self.create_table()  # Ensure the pokemon table exists
        VALUES = (name, number, t1, t2, a1, a2, ha)
        sql_statement = '''INSERT INTO pokemon (name, number, type1, type2, ability1, ability2, hidden_ability)
                           VALUES (?, ?, ?, ?, ?, ?, ?)'''
 
        try:
            self.execute(sql_statement, VALUES) # Execute the insert statement and values
            self.create_stats_table()  # Ensure the stats table exists
        except sqlite3.Error as e:
            print(f"Database error: {e}")


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
                        LEFT JOIN stats s ON p.number = s.number
                        WHERE p.name = ? OR p.number = ?'''
        try:
            result = self.fetchone(sql_search, (identifier, identifier)) # Fetch the full Pokemon details by name or number
        except sqlite3.Error as e:
            raise e
 
        return result

    def show(self, values:tuple):
        '''Method to display the Pokemon's details in a formatted manner.'''
        #retrieve details from the database
        (name, number, t1, t2, a1, a2, ha, 
         hp, atk, defn, spatk, spdef, speed) = values

        #start the formatted output
        output = f"*----- {name} #{number:04} -----*\n"

        #build type string
        type_str = f"Type: {t1}"
        if t2 is not None:
            type_str += f" / {t2}"

        output += type_str + "\n" #append type string to output

        #build abilities strings
        output += f"Ability #1: {a1}\n"
        ability2_str = "Ability #2: "
        if a2:
            ability2_str += a2
        output += ability2_str + "\n"
        hidden_ability_str = "Hidden Ability: "
        if ha:
            hidden_ability_str += ha
        output += hidden_ability_str + "\n"

        stats_output = '*--------Stats--------*\n'
        stats_output += (f"HP: {hp}\nATK: {atk}\nDEF: {defn}\n" +
                         f"SP.ATK: {spatk}\nSP.DEF: {spdef}\nSPEED: {speed}")

        output += stats_output.center(30)  # Center the stats output
        print(output)

    

if __name__ == "__main__":
    Database().show(Database().get_full_pokemon('33'))


