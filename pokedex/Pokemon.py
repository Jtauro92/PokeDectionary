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

    def __str__(self) -> str:
        s = self.stats
        return (f"*----- {self.name or 'Default'}{f' #{self.number:04}' if self.number else ''} -----*\n"
                f"Type: {self.type1 or ''}{f' / {self.type2}' if self.type2 else ''}\n"
                f"Ability #1: {self.ability1 or ''}\nAbility #2: {self.ability2 or ''}\n"
                f"Hidden Ability: {self.hidden_ability or ''}\n\n*--------Stats--------*\n"
                f"HP: {s.hp}\nATK: {s.atk}\nDEF: {s.defn}\nSP.ATK: {s.spatk}\nSP.DEF: {s.spdef}\nSPEED: {s.speed}")

    def __iter__(self) -> Iterable:
        yield from (self.name, self.number, self.type1, self.type2, 
                    self.ability1, self.ability2, self.hidden_ability, self.stats)


if __name__ == "__main__":
    p = Pokemon()
    p.name = 'Jason'
    p.type2 = 'Poison'
    print(p)
