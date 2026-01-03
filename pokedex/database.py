'''Module for managing the Pokemon database using SQLite.'''

import sqlite3
from typing import Any, Optional, Tuple, Union
from validation.sql_statements import *

DB_NAME = "pokemon_database.db"


class Database:
    '''Manages interactions with the Pokemon SQLite database.'''

    def __init__(self, db_name: str = DB_NAME):
        self.db_name = db_name
        self._initialize_tables()

    def _get_connection(self) -> sqlite3.Connection:
        '''Establish and return a connection to the SQLite database.'''
        try:
            return sqlite3.connect(self.db_name)
        except sqlite3.Error as e:
            print(f"Database connection error: {e}")
            raise

    def _initialize_tables(self) -> None:
        '''Create necessary tables if they do not exist.'''
        try:
            self.execute(CREATE_POKEMON_TABLE)
            self.execute(CREATE_STATS_TABLE)
            # Attempt to populate stats (e.g. defaults), ignoring errors if they exist
            try:
                self.execute(POPULATE_STATS)
            except sqlite3.Error:
                pass
        except sqlite3.Error as e:
            print(f"Error initializing tables: {e}")

    def execute(self, sql: str, parameters: tuple = ()) -> None:
        '''
        Execute a SQL statement with optional parameters.

        Args:
            sql (str): The SQL query to execute.
            parameters (tuple): The parameters to substitute into the query.
        '''
        with self._get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(sql, parameters)
            connection.commit()
            return cursor.rowcount > 0

    def fetchone(self, sql: str, parameters: tuple = ()) -> Optional[Tuple]:
        '''
        Fetch a single record from the database.

        Args:
            sql (str): The SQL query to execute.
            parameters (tuple): The parameters to substitute into the query.

        Returns:
            Optional[Tuple]: The fetched record or None.
        '''
        with self._get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(sql, parameters)
            return cursor.fetchone()

    def update_stats(self, pkmn: Any) -> None:
        '''
        Update a Pokemon's stats in the database.

        Args:
            pkmn: The Pokemon object containing stats and number.
        '''
        # pkmn.stats is iterable (Stats object)
        values = tuple(pkmn.stats)
        try:
            self.execute(UPDATE_STATS, (*values, pkmn.number))
        except sqlite3.Error as e:
            raise sqlite3.Error(f"The stats could not be updated. Error: {e}")

    def add_pokemon(self, pkmn: Any) -> None:
        '''
        Add a new Pokemon to the database.

        Args:
            pkmn: The Pokemon object to add.
        '''
        values = (
            pkmn.name, pkmn.number, pkmn.type1, pkmn.type2,
            pkmn.ability1, pkmn.ability2, pkmn.hidden_ability
        )
        self.execute(ADD_POKEMON, values)

    def exists_in_db(self, identifier: Union[str, int]) -> Optional[Tuple]:
        '''
        Check if a Pokemon exists in the database by name or number.

        Args:
            identifier (str | int): The name or number to check.

        Returns:
            bool: True if exists, False otherwise.
        '''
        return self.fetchone(EXIST_IN_DEX, (identifier, identifier))[0] > 0


    def get_stats(self, identifier: Union[str, int]) -> Optional[Tuple]:
        '''
        Get a Pokemon's stats from the database.

        Args:
            identifier (str | int): The name or number of the Pokemon.

        Returns:
            Optional[Tuple]: The stats record.
        '''
        return self.fetchone(GET_STATS, (identifier,))

    def get_pokemon(self, identifier: Union[str, int]) -> Optional[Tuple]:
        '''
        Get a Pokemon's full details including stats from the database.

        Args:
            identifier (str | int): The name or number of the Pokemon.

        Returns:
            Optional[Tuple]: The full Pokemon record.
        '''
        return self.fetchone(GET_POKEMON, (identifier, identifier))


if __name__ == "__main__":
    db = Database()
    # Example usage
    try:
        print(db.exists_in_db("Pikachu"))
    except sqlite3.Error as e:
        print(f"Error checking existence: {e}")
