import unittest

from vk.user import User

token = ''
user_id = 0

class MyTestCase(unittest.TestCase):
    def test_get_friends_info(self):
        user1 = User(user_id, token)
        self.assertEqual(type([]), type(user1.get_friends_info()))


if __name__ == '__main__':
    unittest.main()
