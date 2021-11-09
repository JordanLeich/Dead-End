# https://stackoverflow.com/questions/47690020/python-3-unit-tests-with-user-input
from unittest import main
from unittest import mock
from unittest import TestCase
import sys

sys.path.insert(0, '..')
from io import StringIO
from choices import _player_choice

EXIT_CHOICES = ['e', 'exit', 'c', 'close']


class PlayerChoiceTests(TestCase):
    @mock.patch('choices.input', create=True)
    def testcorrect(self, mocked_input):
        # test setup
        choice_options = ['What would you like to set your volume level to (0 - 100) or exit: ']
        choices = [str(x) for x in range(101)]
        choices.extend(EXIT_CHOICES)
        test_inputs = ['0', '100']
        test_inputs.extend(EXIT_CHOICES)

        with mock.patch('sys.stdout', new=StringIO()) as std_out:  # suppress function printing
            mocked_input.side_effect = test_inputs  # used to take input for the function
            # run tests and check
            result = _player_choice(choices, choice_options)
            self.assertEqual(result, '0')
            result = _player_choice(choices, choice_options)
            self.assertEqual(result, '100')
            result = [_player_choice(choices, choice_options) for _ in EXIT_CHOICES]
            self.assertEqual(result, EXIT_CHOICES)

    @mock.patch('choices.input', create=True)
    def testwrong(self, mocked_input):
        choice_options = ['Which choice would you like to select: ']
        choices = [str(x) for x in range(1, 4)]
        test_inputs = ['5', '4', '3']
        mocked_input.side_effect = test_inputs  # used to take input for the function
        with mock.patch('sys.stdout', new=StringIO()) as std_out:  # suppress function printing
            result = _player_choice(choices, choice_options)
            self.assertEqual(result, '3')


print('player choice test cases')
main()
