from ErrorHandling import set_name, set_number, set_type, set_ability
from Database import Database as db, sqlite3


# Definition of the Pokemon class with attributes and validation methods 
class Pokemon():

    def __init__(self,name = "Default",number = 0,type1 = "Default",type2 ="Default",ability1="Default",ability2=None,hidden_ability=None):
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
    @set_name
    def name(self, new_name):            
        self.__name = new_name

    @property
    def number(self):
        return self.__number

    #Sets the number attribute, ensuring it's within valid range'''
    @number.setter
    @set_number
    def number(self, new_number):
        self.__number = new_number


    # Getter and Setter for type1 attribute
    @property
    def type1(self):
        return self.__type1

    
    @type1.setter
    @set_type
    def type1(self, new_type):        
        self.__type1 = new_type

    # Getter and Setter for type2 attribute
    @property
    def type2(self):
        return self.__type2

    @type2.setter
    @set_type
    def type2(self, new_type):
        self.__type2 = new_type


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
    
    #Sets the hidden_ability attribute, validating it using the set_ability decoratoion
    @hidden_ability.setter
    @set_ability
    def hidden_ability(self, new_ability):
        self.__hidden_ability = new_ability

    '''Behavioral methods for adding and checking Pokemon in the database'''
    def add_to_dex(self):
        VALUES = (self.name, self.number, self.type1, self.type2, self.ability1, self.ability2, self.hidden_ability)
        try:
            db().add_pokemon(VALUES)
        except sqlite3.Error as e:
            raise e

    def name_in_dex(self):
        return db().if_name_exist(self.name)

    def number_in_dex(self):
        return db().if_number_exist(self.number)

    def show(self,identifier):
        p = db().get_pokemon(identifier)
        if not p:
            return f"Pokemon '{identifier}' not found."

        result = [f"Name: {p[0]}\nNumber: {p[1]:04}"]
        
        type_str = f"Type: {p[2]}"
        if p[3] is not None:
            type_str += f" / {p[3]}"
        result.append(type_str)

        result.append(f"Ability #1: {p[4]}")

        ability2_str = "Ability #2: "
        if p[5]:
            ability2_str += p[5]
        result.append(ability2_str)

        hidden_ability_str = "Hidden Ability: "
        if p[6]:
            hidden_ability_str += p[6]
        result.append(hidden_ability_str)
        
        return "\n".join(result)
    

if __name__ == "__main__":
    pokemon = Pokemon()
    pokemon.show("Hydrapple")
