# -*- coding: utf-8 -*-
'''Module defining the Pokemon class with attributes and methods to manage Pokemon data.'''

from typing import Iterable
from validation.descriptors import AttrDescriptor, StatsDescriptor
from tools import Table, Bar_Graph
from pokedex.stats import Stats

class Pokemon:
    '''Class representing a Pokemon with attributes and methods to manage its data.'''
    __slots__ = ('_name', '_number', '_type1', '_type2', 
                 '_ability1', '_ability2', '_hidden_ability', '_stats')

    # Using descriptors for validation and automatic conversion
    name, number, type1, type2 = (AttrDescriptor() for _ in range(4))
    ability1, ability2, hidden_ability = (AttrDescriptor() for _ in range(3))
    stats = StatsDescriptor()

    def __init__(self, 
                name: str | None = None, 
                number: str | None = None, 
                type1: str | None = None, 
                type2: str | None = None, 
                ability1: str | None = None, 
                ability2: str | None = None, 
                hidden_ability: str | None = None, 
                hp: int | None = None,
                atk: int | None = None,
                defn: int | None = None,
                spa: int | None = None,
                spdef: int | None = None,
                speed: int | None = None
                    ):

        self.name, self.number = name, number
        self.type1, self.type2 = type1, type2
        self.ability1, self.ability2, self.hidden_ability = ability1, ability2, hidden_ability
        self.stats = Stats(hp, atk, defn, spa, spdef, speed)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Pokemon):
            return NotImplemented
        return (self.name, self.number) == (other.name, other.number)

    def __str__(self) -> str:
        table = Table()
        table.data = self
        return str(table)


    def __iter__(self) -> Iterable:
        yield from (self.name, self.number, self.type1, self.type2, 
                    self.ability1, self.ability2, self.hidden_ability, *self.stats)


if __name__ == "__main__":
    p = Pokemon()
    p.name = 'Pikachu'
    p.number = 25
    p.ability1 = 'Static'
    p.hidden_ability = 'Lightning Rod'
    p.type1 = 'Electric'
    p.type2 = 'Poison'
    p.stats = (35, 55, 40, 50, 50, 600)
    print(p)
