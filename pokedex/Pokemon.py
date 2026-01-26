# -*- coding: utf-8 -*-
'''Module defining the Pokemon class with attributes and methods to manage Pokemon data.'''

from typing import Iterable, Optional, Tuple
from validation.descriptors import AttrDescriptor, StatsDescriptor

class Pokemon:
    '''Class representing a Pokemon with attributes and methods to manage its data.'''
    __slots__ = ('_name', '_number', '_type1', '_type2', '_ability1', '_ability2', '_hidden_ability', '_stats')

    name, number, type1, type2 = (AttrDescriptor() for _ in range(4))
    ability1, ability2, hidden_ability = (AttrDescriptor() for _ in range(3))
    stats = StatsDescriptor()

    def __init__(self, 
                 name: Optional[str] = None, 
                 number: Optional[int] = None, 
                 type1: Optional[str] = None, 
                 type2: Optional[str] = None, 
                 ability1: Optional[str] = None, 
                 ability2: Optional[str] = None, 
                 hidden_ability: Optional[str] = None, 
                 stats: Optional[Iterable[int]] = ()):

        self.name, self.number = name, number
        self.type1, self.type2 = type1, type2
        self.ability1, self.ability2, self.hidden_ability = ability1, ability2, hidden_ability
        self.stats = stats

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Pokemon):
            return NotImplemented
        return (self.name, self.number) == (other.name, other.number)

    def __str__(self) -> str:
        s = self.stats
        return "\n".join([f"*----- {self.name or 'Default'} {f'#{self.number:04}' if self.number else ''}-----*",
                f"Type: {self.type1 or ''}{f"/ {self.type2}" if self.type2 else ''}",
                f"Ability #1: {self.ability1 or ''}",
                f"Ability #2: {self.ability2 or ''}",
                f"Hidden Ability: {self.hidden_ability or ''}",
                f"\n*--------Stats--------*",
                f"HP: {s.hp}",
                f"ATK: {s.atk}",
                f"DEF: {s.defn}",
                f"SP.ATK: {s.spatk}",
                f"SP.DEF: {s.spdef}",
                f"SPEED: {s.speed}"
                ])


    def __iter__(self) -> Iterable:
        yield from (self.name, self.number, self.type1, self.type2, 
                    self.ability1, self.ability2, self.hidden_ability, self.stats)


if __name__ == "__main__":
    p = Pokemon()
    p.number = 25
    p.type2 = 'Poison'
    print(p)
