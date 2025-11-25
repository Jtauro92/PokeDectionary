

#Constants
NUM_OF_POKEMON = 1025
TYPE_LIST = [
    "NORMAL", "FIRE", "WATER", "ELECTRIC", "GRASS", "ICE", "FIGHTING",
    "POISON", "GROUND", "FLYING", "PSYCHIC", "BUG", "ROCK", "GHOST",
    "DRAGON", "DARK", "STEEL", "FAIRY"
]

# Function to validate and set a Pokemon's ability
def set_ability(func):

    def wrapper(self,value):
        value = value.title()

        with open("abilities.txt", "r") as file:
            abilities = file.read().split(",")
            abilities = [ability.strip() for ability in abilities]

        if (value not in abilities) or ([self.ability1,self.ability2,self.hidden_ability].count(value) > 0): 
            return

        return func(self,value)
    return wrapper

def set_type(new_type):
    new_type = new_type.upper()
    if new_type not in TYPE_LIST:
        return
    return new_type


# Definition of the Pokemon class with attributes and validation methods 
class Pokemon():
    def __init__(self,name = "Default",number = 0,type1 = "Default",type2 ="Default",ability1="Default",ability2="Default",hidden_ability="Default"):
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

    # Getter and Setter for name attribute

    @property
    def name(self):
        return self.__name

    #Sets the name attribute, capitalizing it if it's not numeric
    @name.setter
    def name(self, new_name):
        name = new_name

        if not name.isnumeric():
            name = name.title()
        else:
            raise ValueError("Names cannot be numerical!")
            
        self.__name = name

    @property
    def number(self):
        return self.__number

    '''Sets the number attribute, ensuring it's within valid range'''
    @number.setter
    def number(self, new_number):

        #Try to convert new_number to an integer
        try:
            number = int(new_number)
        except (TypeError, ValueError): 
            return #Exit if conversion fails

        #Check if number is within valid range
        if not (1 <= number <= NUM_OF_POKEMON):
            return #Exit if number is out of range
            
        self.__number = number

    # Getter and Setter for type1 attribute
    @property
    def type1(self):
        return self.__type1

    @type1.setter
    def type1(self, new_type):
        type1 = set_type(new_type) #Validate type using set_type method
        if type1 is None:
            return
        self.__type1 = type1

    # Getter and Setter for type2 attribute
    @property
    def type2(self):
        return self.__type2

    @type2.setter
    def type2(self, new_type):
        type2 = set_type(new_type)

        if not((type2 != None) and (type2 != self.type1)): #Ensure type2 is valid and different from type1
            return
        
        self.__type2 = type2

    # Getter and Setter for ability1 attribute
    @property
    def ability1(self):
        return self.__ability1
    
    #Sets the ability1 attribute, validating it using the set_ability decorator
   
    @ability1.setter
    @set_ability
    def ability1(self, new_ability):
        self.__ability1 = new_ability
    
    #sets ability2 attribute
    @property
    def ability2(self):
        return self.__ability2
    
    #Sets the ability1 attribute, validating it using the set_ability decorator
   
    @ability2.setter
    @set_ability
    def ability2(self, new_ability):
        self.__ability2 = new_ability

    #sets hidden_ability attribute
    @property
    def hidden_ability(self):
        return self.__hidden_ability
    
    #Sets the hidden_ability attribute, validating it using the set_ability decorator
   
    @hidden_ability.setter
    @set_ability
    def hidden_ability(self, new_ability):
        self.__hidden_ability = new_ability
    

if __name__ == "__main__":
    pokemon = Pokemon()
    pokemon.type1 = "fire"
    pokemon.type2 = "water"
    pokemon.ability2 ="overgrow"
    pokemon.ability1 = "overgrow"
    pokemon.name = "123"
    print(pokemon)
