'''Module for managing the Pokemon database using SQLite.'''

from sqlite3 import Connection as conn, Error as se
from typing import Optional, Tuple, Union
from validation.sql_statements import * 
from pokedex.constants import NUM_OF_POKEMON
from pokedex.pokemon import Pokemon as pkmn
import requests

DB_NAME = "pokemon_database.db"

base_url = "https://pokeapi.co/api/v2/pokemon/"

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
            return
        start = self._get_resume_id()
        if start <= NUM_OF_POKEMON:
            self._populate_from_PokeAPI(start)

    def _get_resume_id(self) -> int:
        '''Get the ID of the last Pokemon added to the database.'''
        result = self.fetchone("SELECT COUNT(*) FROM pokemon")
        return result[0] + 1 if result else 0

    def _populate_from_PokeAPI(self, start_id: int) -> None:
        '''Populate the database with Pokemon data from the PokeAPI starting from a specific ID.'''
        for count in range(start_id, NUM_OF_POKEMON + 1):
            try:
                response = requests.get(f"{base_url}{count}")
                if response.status_code == 200:
                    data = response.json()
                    pk = pkmn()
                    pk.name = data['name'].title()
                    pk.number = data['id']
                    pk.type1 = data['types'][0]['type']['name'].upper() if len(data['types']) > 0 else None
                    pk.type2 = data['types'][1]['type']['name'].upper() if len(data['types']) > 1 else None
                    pk.ability1 = data['abilities'][0]['ability']['name'].replace('-', ' ').title() if len(data['abilities']) > 0 else None
                    pk.ability2 = next((ab['ability']['name'].replace('-', ' ').title() for ab in data['abilities'][1:] if not ab.get('is_hidden')), None)
                    pk.hidden_ability = next((ab['ability']['name'].replace('-', ' ').title() for ab in data['abilities'] if ab.get('is_hidden')), None)
                    pk.stats.hp = data['stats'][0]['base_stat']
                    pk.stats.atk = data['stats'][1]['base_stat']
                    pk.stats.defn = data['stats'][2]['base_stat']
                    pk.stats.spatk = data['stats'][3]['base_stat']
                    pk.stats.spdef = data['stats'][4]['base_stat']
                    pk.stats.speed = data['stats'][5]['base_stat']

                    # Add the Pokemon to the database
                    self.add_pokemon(pk)
                    self.update_stats(pk)
                    print(f"Added Pokemon {pk.name} (#{pk.number:04}) to the database.")

            except Exception as e:
                print(f"Error fetching data for Pokemon {count}: {e}")
                break

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
        values = (pkmn.stats)
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
