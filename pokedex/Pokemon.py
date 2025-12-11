'''Module defining the Pokemon class with attributes and methods to manage Pokemon data.'''

from pokedex import set_name, set_number, set_type, set_ability, get_pokemon


class Pokemon():
    '''Class representing a Pokemon with attributes and methods to manage its data.'''
    def __init__(self,name = "Default",number = 0,type1 = "Default",type2 ="Default",ability1="Default",ability2=None,hidden_ability=None):
        super().__init__()
        self.__name = name
        self.__number = number
        self.__type1 = type1
        self.__type2 = type2
        self.__ability1 = ability1
        self.__ability2 = ability2
        self.__hidden_ability = hidden_ability

    def __str__(self):
        return (f"Name: {self.__name}\n"
                f"Number: {self.__number}\n"
                f"Type 1: {self.__type1}\n"
                f"Type 2: {self.__type2}\n"
                f"Ability 1: {self.__ability1}\n"
                f"Ability 2: {self.__ability2}\n"
                f"Hidden Ability: {self.__hidden_ability}")

    #Getters and Setters for each attribute with validation decorators

    #Getter and Setter for name attribute
    @property
    def name(self):
        return self.__name

    @name.setter #Sets name attribute
    @set_name #Decorator to validate and stardize name
    def name(self, new_name):            
        self.__name = new_name

    '''Getter and Setter for number attribute'''
    @property
    def number(self):
        return self.__number

    @number.setter #Sets number attribute
    @set_number 
    def number(self, new_number):
        self.__number = new_number
    
    '''Getter and Setter for type attributes'''
    @property
    def type1(self):
        return self.__type1

    @type1.setter #Sets type1 attribute
    @set_type 
    def type1(self, new_type):        
        self.__type1 = new_type

    @property
    def type2(self):
        return self.__type2

    @type2.setter #Sets type2 attribute
    @set_type 
    def type2(self, new_type): 
        self.__type2 = new_type
        
 
    '''Getter and Setter for ability attributes ensuring unique values'''
    @property
    def ability1(self):
        return self.__ability1
   
    @ability1.setter #Sets ability1 attribute
    @set_ability
    def ability1(self, new_ability):
        self.__ability1 = new_ability
    
    @property
    def ability2(self):
        return self.__ability2
   
    @ability2.setter #Sets ability2 attribute
    @set_ability
    def ability2(self, new_ability):
        self.__ability2 = new_ability

    @property
    def hidden_ability(self):
        return self.__hidden_ability
    
    @hidden_ability.setter #Sets hidden_ability attribute
    @set_ability
    def hidden_ability(self, new_ability):
        self.__hidden_ability = new_ability


    def show(self):
        '''Method to display the Pokemon's details in a formatted manner.'''
        name, number, t1, t2, a1, a2, ha = get_pokemon(self.name) # Retrieve details from the database

        result = [f"Name: {name}\nNumber: {number:04}"]
        
        type_str = f"Type: {t1}"
        if t2 is not None:
            type_str += f" / {t2}"
        result.append(type_str)

        result.append(f"Ability #1: {a1}")

        ability2_str = "Ability #2: "
        if a2:
            ability2_str += a2
        result.append(ability2_str)

        hidden_ability_str = "Hidden Ability: "
        if ha:
            hidden_ability_str += ha
        result.append(hidden_ability_str)
        
        print( "\n".join(result))
    

if __name__ == "__main__":
    pokemon = Pokemon()
    pokemon.name ="Pikachu"
    pokemon.show()