import unittest

from vk.Friends import get_friends_info

token = ''
user_id = 0

class MyTestCase(unittest.TestCase):
    def test_get_friends_info(self):
        self.assertEqual(type([]), type(get_friends_info(user_id, token)))


if __name__ == '__main__':
    unittest.main()
