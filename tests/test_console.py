import unittest
from unittest.mock import patch, Mock
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel

class TestConsole(unittest.TestCase):

    def setUp(self):
        # Redirect stdout to capture printed output
        self.held_output = StringIO()
        self.old_stdout = sys.stdout
        sys.stdout = self.held_output

    def tearDown(self):
        # Restore stdout
        sys.stdout = self.old_stdout

    def test_do_create_command(self):
        with patch('models.storage') as mock_storage:
            HBNBCommand().onecmdloop()
            mock_storage.save.assert_called_once()
            created_instance = mock_storage.new.call_args[0][0]
            self.assertIsInstance(created_instance, BaseModel)
            self.assertTrue(created_instance.id)  # Check if ID is generated

    def test_do_create_command_with_attributes(self):
        with patch('models.storage') as mock_storage:
            HBNBCommand().onecmdloop()
            mock_storage.save.assert_called_once()
            created_instance = mock_storage.new.call_args[0][0]
            self.assertIsInstance(created_instance, BaseModel)
            self.assertEqual(created_instance.name, "Test")
            self.assertEqual(created_instance.number, 42)



if __name__ == '__main__':
    unittest.main()
