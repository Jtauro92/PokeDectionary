'''Module defining the Pokemon class with attributes and methods to manage Pokemon data.'''

from pokedex.stats import stats as s
from validation import validate_name, set_number, set_type, set_ability


class Pokemon:
    '''Class representing a Pokemon with attributes and methods to manage its data.'''

    def __init__(self, name:str = "Default", number:int = 0, type1:str = "Default",
                 type2:str = None, ability1:str = "Default", ability2:str = None,
                 hidden_ability:str = None, stats:s = ()):
        self.__name = name
        self.__number = number
        self.__type1 = type1
        self.__type2 = type2
        self.__ability1 = ability1
        self.__ability2 = ability2
        self.__hidden_ability = hidden_ability
        self.__stats = s(*stats)

    def __str__(self):
        output = [f"*----- {self.__name} #{self.__number:04} -----*",
                  f"Type: {self.__type1}" + (f" / {self.__type2}" if self.__type2 else ""),
                  f"Ability #1: {self.__ability1}",
                  f"Ability #2: " + (f"{self.__ability2}" if self.__ability2 else ""),
                  f"Hidden Ability: " + (f"{self.__hidden_ability}" if self.__hidden_ability else ""),
                  '*--------Stats--------*',
                  f"HP: {self.__stats.hp}",
                  f"ATK: {self.__stats.atk}",
                  f"DEF: {self.__stats.defn}",
                  f"SP.ATK: {self.__stats.spatk}",
                  f"SP.DEF: {self.__stats.spdef}",
                  f"SPEED: {self.__stats.speed}"]
        return "\n".join(output)
        

    def __iter__(self):
        '''Iterator to yield Pokemon attributes in a specific order.'''
        yield from [self.__name, self.__number, self.__type1, self.__type2,
                    self.__ability1, self.__ability2, self.__hidden_ability,
                    self.__stats]
    #Getters and Setters for each attribute with validation decorators

    #Getter and Setter for name attribute
    @property
    def name(self) -> str:
        return self.__name

    @name.setter #Sets name attribute
    @validate_name #Decorator to validate and stardize name
    def name(self, new_name: str) -> None:            
        self.__name = new_name

    # Getter and Setter for number attribute
    @property
    def number(self) -> int:
        return self.__number

    @number.setter #Sets number attribute
    @set_number
    def number(self, new_number: int) -> None:
        self.__number = new_number

    # Getter and Setter for type attributes
    @property
    def type1(self) -> str:
        return self.__type1

    @type1.setter #Sets type1 attribute
    @set_type
    def type1(self, new_type: str) -> None:
        self.__type1 = new_type

    @property
    def type2(self) -> str:
        return self.__type2

    @type2.setter #Sets type2 attribute
    @set_type
    def type2(self, new_type: str) -> None:
        if self.__type1 == "Default":
            self.__type1 = new_type
        else:
            self.__type2 = new_type
        
    # Getter and Setter for ability attributes
    @property
    def ability1(self) -> str:
        return self.__ability1
   
    @ability1.setter #Sets ability1 attribute
    @set_ability
    def ability1(self, new_ability: str) -> None:
        self.__ability1 = new_ability
    
    @property
    def ability2(self) -> str:
        return self.__ability2
   
    @ability2.setter #Sets ability2 attribute
    @set_ability
    def ability2(self, new_ability: str) -> None:
        self.__ability2 = new_ability

    @property
    def hidden_ability(self) -> str:
        return self.__hidden_ability
    
    @hidden_ability.setter #Sets hidden_ability attribute
    @set_ability
    def hidden_ability(self, new_ability: str) -> None:
        self.__hidden_ability = new_ability

    # Getter for stats attribute
    @property
    def stats(self) -> tuple:
        return self.__stats
    

if __name__ == "__main__":
    pokemon = Pokemon()
    pokemon.name ="Pikachu"
    pokemon.number = 25
    pokemon.type1 = "Electric"
    pokemon.type2 = "Fire"
    print(pokemon)