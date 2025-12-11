import sqlite3

class Database:
    
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
        with self.connectdb() as connection:
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

    '''Add a new Pokemon to the database'''
    def add_pokemon(self):
        VALUES = (self.name, self.number, self.type1, self.type2, self.ability1, self.ability2, self.hidden_ability)
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

    '''Retrieve a Pokemon's details by name or number'''
    def get_pokemon(self, identifier):
        sql_search = '''SELECT name, number, type1, type2, ability1, ability2, hidden_ability 
                        FROM pokemon 
                        WHERE name = ? OR number = ?'''

        try:
            result = self.fetchone(sql_search, (identifier, identifier))
        except sqlite3.Error as e:
            raise e
 
        return result

    

if __name__ == "__main__":
    print(Database().get_pokemon('pikachu'))

