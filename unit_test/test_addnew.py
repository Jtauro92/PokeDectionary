import unittest
from unittest.mock import patch
from jobs.addnew import AddNewPokemon



class TestAddNewPokemon(unittest.TestCase):
    '''Test the AddNewPokemon class.'''

    def test_set_name_numerical_input_raises_value_error(self):
        '''Test that set_name raises a ValueError when a numerical input is provided.'''
        add_new = AddNewPokemon()
        with patch('builtins.input', return_value='123'): #patch input to return a numerical string
            with self.assertRaisesRegex(ValueError, "Names cannot be numerical!"): #expect a ValueError with the specific message
                add_new.set_name() #invoke the method that should validate the input

    def test_set_name_existing_pokemon_raises_value_error(self):
        add_new = AddNewPokemon()
        with patch('builtins.input', return_value='Pikachu'):
            with self.assertRaises(ValueError):
                add_new.set_name()

    def test_set_name_valid_input_capitalization(self):
        add_new = AddNewPokemon()
        with patch('builtins.input', return_value='jason'):
                add_new.set_name()
                self.assertEqual(add_new.pkmn.name, 'Jason')

    def test_set_number_string_input_raises_value_error(self):
        add_new = AddNewPokemon()
        with patch('builtins.input', return_value='abc'):
            with self.assertRaises(ValueError):
                add_new.set_number()

    def test_set_number_existing_pokemon_raises_value_error(self):
        add_new = AddNewPokemon()
        with patch('builtins.input', return_value='25'):
            with self.assertRaises(ValueError):
                add_new.set_number()

if __name__ == "__main__":
    unittest.main()
        


