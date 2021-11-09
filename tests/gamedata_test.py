# https://stackoverflow.com/questions/47690020/python-3-unit-tests-with-user-input
from unittest import mock
from unittest import TestCase
import sys
sys.path.insert(0,'..')
import gamedata

class DictCreateTests(TestCase):
    @mock.patch('gamedata.input', create=True)
    def testdictCreateSimple(self, mocked_input):
        mocked_input.side_effect = ['Albert Einstein', '42.81', 'done']
        result = dictCreate(1)
        self.assertEqual(result, {'Albert Einstein': [42.81]})