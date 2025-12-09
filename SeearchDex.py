from Pokemon import Pokemon as p, sqlite3, db
from ErrorHandling import DuplicateValueError, validation_loop as vl, InvalidValueError

'''Class to search for a Pokemon in the database'''
class search_dex(p):
    def __init__(self):
        super().__init__()

    '''Method to get Pokemon details from user input and fetch from database'''
    @vl
    def get_details(self):
        identifier = input("Enter Pokemon name or number to search: ").strip().title()
        if identifier == '0':
            raise KeyboardInterrupt

        sql_search = '''SELECT name, number, type1, type2, ability1, ability2, hidden_ability 
                        FROM pokemon 
                        WHERE name = ? OR number = ?'''
        try:
            result = self.fetchone(sql_search, (identifier, identifier))
            if result:
                self.name = result[0]
                self.number = result[1]
                self.type1 = result[2]
                self.type2 = result[3]
                self.ability1 = result[4]
                self.ability2 = result[5]
                self.hidden_ability = result[6]
            else:
                raise InvalidValueError("Pokemon not found.")
        except DuplicateValueError:
            pass
        except sqlite3.Error as e:
            raise e("Database error: self.fetchone(sql_search, (identifier, identifier))")


    def show_details(self):

            self.get_details()
  

            self.show()
 

    def main(self):
        while True:
            try:
                self.show_details()
            except KeyboardInterrupt:
                print("Exiting search.")
                break

if __name__ == "__main__":
    sd = search_dex()
    sd.main()

