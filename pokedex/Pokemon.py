'''Module defining the Pokemon class with attributes and methods to manage Pokemon data.'''

from stats import Stats as s
from validation import validate_name, validate_number, set_type, set_ability, DEFAULT

class Pokemon:
    '''
    Class representing a Pokemon with attributes and methods to manage its data.
    '''

    def __init__(self, name: str = DEFAULT, number: int = DEFAULT, type1: str = DEFAULT,
                 type2: str = DEFAULT, ability1: str = DEFAULT, ability2: str = DEFAULT,
                 hidden_ability: str = DEFAULT, stats: s = ()) -> None:
        self._name = name
        self._number = number
        self._type1 = type1
        self._type2 = type2
        self._ability1 = ability1
        self._ability2 = ability2
        self._hidden_ability = hidden_ability
        self._stats = s(*stats)

    def __str__(self):
        output = [f"*----- {self._name or 'Default'} " +
                 (f"#{self._number:04}" if self._number else "Default") +"-----*",
                  f"Type: {self._type1 or "Default"}" + 
                  (f" / {self._type2}" if self._type2 else ''),
                  f"Ability #1: {self._ability1}",
                  f"Ability #2: " + (f"{self._ability2}" if self._ability2 else ""),
                  f"Hidden Ability: " + (f"{self._hidden_ability}" 
                                         if self._hidden_ability else ""),
                  '*--------Stats--------*',
                  f"HP: {self._stats.hp}",
                  f"ATK: {self._stats.atk}",
                  f"DEF: {self._stats.defn}",
                  f"SP.ATK: {self._stats.spatk}",
                  f"SP.DEF: {self._stats.spdef}",
                  f"SPEED: {self._stats.speed}"]
        return "\n".join(output)
        

    def __iter__(self):
        '''
        Iterator to yield Pokemon attributes in a specific order.
        '''
        yield from [self._name, self._number, self._type1, self._type2,
                    self._ability1, self._ability2, self._hidden_ability,
                    self._stats]
    
        
    #Getters and Setters for each attribute with validation decorators

    #Getter and Setter for name attribute
    @property
    def name(self) -> str:
        return self._name

    @name.setter 
    @validate_name  # Wraps name setter with validate_name function
    def name(self, new_name: str) -> None:
        '''
        Sets the name attribute using the validate_name decorator.
        '''
        self._name = new_name


    # Getter and Setter for number attribute
    @property
    def number(self) -> int:
        return self._number

    @number.setter
    @validate_number  # Wraps number setter with validate_number function
    def number(self, number: int) -> None:
        '''
        Sets the number attribute using the validate_number decorator.
        '''
        self._number = number


    # Getter and Setter for type attributes
    @property
    def type1(self) -> str:
        return self._type1

    @type1.setter 
    @set_type  # Wraps type1 setter with set_type function
    def type1(self, new_type: str) -> None:
        '''
        Sets the type1 attribute using the set_type decorator.
        '''
        self._type1 = new_type


    @property
    def type2(self) -> str:
        return self.__type2

    @type2.setter 
    @set_type  # Wraps type2 setter with set_type function
    def type2(self, new_type: str) -> None:
        '''
        Sets the type2 attribute using the set_type decorator.
        '''
        if self._type1 == DEFAULT:
            self._type1 = new_type
        else:
            self._type2 = new_type


    # Getter and Setter for ability attributes
    @property
    def ability1(self) -> str:
        return self._ability1
   
    @ability1.setter 
    @set_ability  # Wraps ability1 setter with set_ability function
    def ability1(self, new_ability: str) -> None:
        '''
        Sets the ability1 attribute using the set_ability decorator.
        '''
        self._ability1 = new_ability
    

    @property
    def ability2(self) -> str:
        return self._ability2

    @ability2.setter  
    @set_ability  # Wraps ability2 setter with set_ability function
    def ability2(self, new_ability: str) -> None:
        '''
        Sets the ability2 attribute using the set_ability decorator.
        '''
        self._ability2 = new_ability


    @property
    def hidden_ability(self) -> str:
        return self._hidden_ability

    @hidden_ability.setter
    @set_ability  # Wraps hidden_ability setter with set_ability function
    def hidden_ability(self, ability: str) -> None:
        '''
        Sets the hidden_ability attribute using the set_ability decorator.
        arg: ability - new hidden ability to set
        '''
        self._hidden_ability = ability

    @property
    def stats(self) -> tuple:  # Getter for stats attribute
        return self._stats


if __name__ == "__main__":
    pokemon = Pokemon()
    print(pokemon)