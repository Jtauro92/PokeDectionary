from jobs import pk, get_pokemon
from validation import(DuplicateValueError,
                         validation_loop as vl,
                        InvalidValueError,
                        sqlite3_error)



'''Class to search for a Pokemon in the database'''
class search_dex(pk):
    def __init__(self):
        super().__init__()

    '''Method to get Pokemon details from user input and fetch from database'''
    @vl
    def get_details(self):
        identifier = input("Enter Pokemon name or number to search: ").strip().title()
        if identifier == '0':
            raise KeyboardInterrupt

        try:
            name, number, t1, t2, a1, a2, ha = get_pokemon(identifier)
            self.name = name
            self.number = number
            self.type1 = t1
            self.type2 = t2
            self.ability1 = a1
            self.ability2 = a2
            self.hidden_ability = ha
        except TypeError:
                raise InvalidValueError("Pokemon not found in the database.")
        except DuplicateValueError:
            pass
        except sqlite3_error as e:
            raise e("Database error: self.fetchone(sql_search, (identifier, identifier))")


    def show_details(self):

        self.get_details()
        self.show()
        print()
 

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

