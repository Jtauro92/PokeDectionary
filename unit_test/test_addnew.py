import unittest
from unittest.mock import patch
from jobs.addnew import AddNewPokemon



class TestAddNewPokemon(unittest.TestCase):

    def test_set_name_numerical_input_raises_value_error(self):
        add_new = AddNewPokemon()
        with patch('builtins.input', return_value='123'):
            with self.assertRaises(ValueError):
                add_new.set_name()

    def test_set_name_existing_pokemon_raises_value_error(self):
        add_new = AddNewPokemon()
        with patch('builtins.input', return_value='Pikachu'):
            with self.assertRaises(ValueError):
                add_new.set_name()

    def test_set_name_valid_input_capitalization(self):
        add_new = AddNewPokemon()
        with patch('builtins.input', return_value='pikachu') \
            as input_mock, \
            patch('jobs.addnew.get_pokemon', return_value=None) \
            as get_pokemon_mock:
                add_new.set_name()
                self.assertEqual(add_new.pkmn.name, 'Pikachu')

    def test_set_number_string_input_raises_value_error(self):
        add_new = AddNewPokemon()
        with patch('builtins.input', return_value='abc'):
            with self.assertRaises(ValueError):
                add_new.set_number()

if __name__ == "__main__":
    unittest.main()
        


