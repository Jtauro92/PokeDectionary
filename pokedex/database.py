'''Module for managing the Pokemon database using SQLite.'''

from sqlite3 import Connection as conn, Error as se
from typing import Optional, Tuple, Union
from validation.sql_statements import *

DB_NAME = "pokemon_database.db"


class Database(conn):
    '''Manages interactions with the Pokemon SQLite database.'''

    def __init__(self):
        super().__init__(DB_NAME, isolation_level=None)
        self._initialize_tables()

    def _initialize_tables(self) -> None:
        '''Create necessary tables if they do not exist.'''
        try:
            self.execute(CREATE_POKEMON_TABLE)
            self.execute(CREATE_STATS_TABLE)
            # Attempt to populate stats (e.g. defaults), ignoring errors if they exist
            try:
                self.execute(POPULATE_STATS)
            except se:
                pass
        except se as e:
            print(f"Error initializing tables: {e}")

    def execute(self, sql: str, parameters: tuple = ()) -> None:
        '''
        Execute a SQL statement with optional parameters.

        Args:
            sql (str): The SQL query to execute.
            parameters (tuple): The parameters to substitute into the query.
        '''
        with self:
            cursor = self.cursor()
            cursor.execute(sql, parameters)
            return cursor.rowcount

    def fetchone(self, sql: str, parameters: tuple = ()) -> Optional[Tuple]:
        '''
        Fetch a single record from the database.

        Args:
            sql (str): The SQL query to execute.
            parameters (tuple): The parameters to substitute into the query.

        Returns:
            Optional[Tuple]: The fetched record or None.
        '''
        with self:
            cursor = self.cursor()
            cursor.execute(sql, parameters)
            return cursor.fetchone()

    def update_stats(self, pkmn: object) -> None:
        '''
        Update a Pokemon's stats in the database.

        Args:
            pkmn: The Pokemon object containing stats and number.
        '''
        # pkmn.stats is iterable (Stats object)
        values = tuple(pkmn.stats)
        try:
            self.execute(UPDATE_STATS, (*values, pkmn.number))
        except se:
            raise se(f"The stats could not be updated. Error: {se}")

    def add_pokemon(self, pkmn: object) -> None:
        '''
        Add a new Pokemon to the database.

        Args:
            pkmn: The Pokemon object to add.
        '''
        result = self.execute(ADD_POKEMON, tuple(pkmn)[0:7])
        if result:
            self._add_to_stats(pkmn)
        else:
            print("Failed to add Pokemon to the database.")

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

    def _add_to_stats(self, pkmn: object) -> None:
        '''
        Add a stats record for a Pokemon in the database.
        Args:
            pkmn: The Pokemon object containing stats and number.
        '''
        if self.execute(ADD_TO_STATS, (pkmn.number,)) == 0:
            raise se


if __name__ == "__main__":
    db = Database()
    # Example usage
    try:
        print(db.exists_in_db("jhlk"))
    except se:
        print(f"Error checking existence: {se}")
