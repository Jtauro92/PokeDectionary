# -*- coding: utf-8 -*-
'''Module defining the Pokemon class with attributes and methods to manage Pokemon data.'''

from typing import Iterable
from pokedex.stats import Stats
from validation import validate_name, validate_number, set_type, set_ability, DEFAULT


class Pokemon:
    '''
    Class representing a Pokemon with attributes and methods to manage its data.
    Uses __slots__ for memory optimization and faster attribute access.
    '''
    __slots__ = (
        '_name', '_number', '_type1', '_type2',
        '_ability1', '_ability2', '_hidden_ability', '_stats'
    )

    def __init__(self, name: str = DEFAULT, number: int = DEFAULT, type1: str = DEFAULT,
                 type2: str = DEFAULT, ability1: str = DEFAULT, ability2: str = DEFAULT,
                 hidden_ability: str = DEFAULT, stats: Iterable[int] | Stats = ()) -> None:
        '''
        Initialize a new Pokemon instance.

        Args:
            name (str): The name of the Pokemon.
            number (int): The Pokedex number.
            type1 (str): The primary type.
            type2 (str): The secondary type.
            ability1 (str): The first ability.
            ability2 (str): The second ability.
            hidden_ability (str): The hidden ability.
            stats (Iterable[int] | Stats): A tuple of stats or a Stats object.
        '''
        # Initialize all slots to defaults to prevent AttributeErrors
        for slot in self.__slots__:
            setattr(self, slot, DEFAULT)
        
        self._stats = Stats()

        # Initialize stats first, then route others through validated setters
        self.name = name
        self.number = number
        self.type1 = type1
        self.type2 = type2
        self.ability1 = ability1
        self.ability2 = ability2
        self.hidden_ability = hidden_ability
        self.stats = stats

    def __str__(self) -> str:
        '''Return a formatted string representation of the Pokemon.'''
        name_display = self.name or 'Default'
        number_display = f"#{self.number:04}" if self.number else '\b'
        type_display = f"{self.type1 or ''}"
        if self.type2:
            type_display += f" / {self.type2}"

        output = [
            f"*----- {name_display} {number_display} -----*",
            f"Type: {type_display}",
            f"Ability #1: {self.ability1 or ''}",
            f"Ability #2: {self.ability2 or ''}",
            f"Hidden Ability: {self.hidden_ability or ''}",
            '\n*--------Stats--------*',
            f"HP: {self.stats.hp}",
            f"ATK: {self.stats.atk}",
            f"DEF: {self.stats.defn}",
            f"SP.ATK: {self.stats.spatk}",
            f"SP.DEF: {self.stats.spdef}",
            f"SPEED: {self.stats.speed}"
        ]
        return "\n".join(output)

    def __iter__(self):
        '''Iterator to yield Pokemon attributes in a specific order.'''
        yield from [self.name, self.number, self.type1, self.type2,
                    self.ability1, self.ability2, self.hidden_ability,
                    self.stats]

    # Name
    @property
    def name(self) -> str:
        '''Get the Pokemon's name.'''
        return self._name

    @name.setter
    @validate_name
    def name(self, value: str) -> None:
        self._name = value

    # Number
    @property
    def number(self) -> int:
        '''Get the Pokemon's number.'''
        return self._number

    @number.setter
    @validate_number
    def number(self, value: int) -> None:
        self._number = value

    # Types
    @property
    def type1(self) -> str:
        '''Get the primary type.'''
        return self._type1

    @type1.setter
    @set_type
    def type1(self, value: str) -> None:
        self._type1 = value

    @property
    def type2(self) -> str:
        '''Get the secondary type.'''
        return self._type2

    @type2.setter
    @set_type
    def type2(self, value: str) -> None:
        # If type1 is not set, assign to type1 instead
        if self._type1 == DEFAULT:
            self._type1 = value
        else:
            self._type2 = value

    # Abilities
    @property
    def ability1(self) -> str:
        '''Get the first ability.'''
        return self._ability1

    @ability1.setter
    @set_ability
    def ability1(self, value: str) -> None:
        self._ability1 = value

    @property
    def ability2(self) -> str:
        '''Get the second ability.'''
        return self._ability2

    @ability2.setter
    @set_ability
    def ability2(self, value: str) -> None:
        self._ability2 = value

    @property
    def hidden_ability(self) -> str:
        '''Get the hidden ability.'''
        return self._hidden_ability

    @hidden_ability.setter
    @set_ability
    def hidden_ability(self, value: str) -> None:
        self._hidden_ability = value

    # Stats
    @property
    def stats(self) -> Stats:
        '''Get the Pokemon's stats.'''
        return self._stats

    @stats.setter
    def stats(self, value: Iterable[int] | Stats) -> None:
        self._stats = Stats(*value)

if __name__ == "__main__":
    pokemon = Pokemon(stats=(45, 49, 49, 65, 65))
    # Example stats for Bulbasaur
    print(*pokemon.stats)