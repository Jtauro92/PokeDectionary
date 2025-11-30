import sqlite3
 
class Database:

    def __init__(self):
        self.conn = sqlite3.connect


    '''Connect to the database'''
    def connectdb(self):
        try:
            db_connection = self.conn("pokemon_database.db") # Connect to the SQLite database
        except sqlite3.Error as e:
            print(f"Database connection error: {e}")

        return db_connection

    '''Create the Pokemon table if it doesn't exist'''

    def create_table(self, cursor): 
            try:
                cursor.execute('''CREATE TABLE IF NOT EXISTS pokemon (
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

    '''Add a new Pokemon to the database'''

    def add_pokemon(self, pokemon):
        VALUES = (pokemon.name,
                  pokemon.number, 
                  pokemon.type1, 
                  pokemon.type2,
                  pokemon.ability1, 
                  pokemon.ability2, 
                  pokemon.hidden_ability
            )
        sql_statement = '''INSERT INTO pokemon (name, number, type1, type2, ability1, ability2, hidden_ability)
                           VALUES (?, ?, ?, ?, ?, ?, ?)'''


        with self.connectdb() as connection: # Use the connection context manager
            cursor = connection.cursor()
            self.create_table(cursor) # Ensure the table exists
            
            try:
                cursor.execute(sql_statement, VALUES) # Execute the insert statement and values
                connection.commit() # Commit the transaction and close the connection
            except sqlite3.Error as e:
                raise f"The pokemon could not be added. Error: {e}"

    '''Check if a Pokemon name already exists in the database'''
    def if_name_exist(self, name):
        sql_statement = '''SELECT COUNT(*) FROM pokemon WHERE name = ?'''
        with self.connectdb() as connection:
            cursor = connection.cursor()
            try:
                cursor.execute(sql_statement, (name,))
                count = cursor.fetchone()[0]
                return count > 0
            except sqlite3.Error:
                print("This pokemon does not exist!")
                return False

    def if_number_exist(self, number):
        sql_statement = '''SELECT COUNT(*) FROM pokemon WHERE number = ?'''
        with self.connectdb() as connection:
            cursor = connection.cursor()
            try:
                cursor.execute(sql_statement, (number,))
                count = cursor.fetchone()[0]
                return count > 0
            except sqlite3.Error:
                print("This pokemon number does not exist!")
                return False

if __name__ == "__main__":
    db = Database()
    conn = db.connectdb()
    cursor = conn.cursor()
    db.create_table(cursor)
    conn.close()

