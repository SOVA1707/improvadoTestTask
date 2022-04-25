import unittest

from vk.user import User

token = ''
user_id = 0

class MyTestCase(unittest.TestCase):
    def test_get_friends_info(self):
        user1 = User(token, user_id)
        user1_friend_info = user1.get_friends_info()
        self.assertEqual(type([]), type(user1_friend_info))
        self.assertTrue('first_name' in user1_friend_info[0])
        self.assertTrue('last_name' in user1_friend_info[0])
        self.assertTrue('country' in user1_friend_info[0])
        self.assertTrue('city' in user1_friend_info[0])
        self.assertTrue('bdate' in user1_friend_info[0])
        self.assertTrue('sex' in user1_friend_info[0])


if __name__ == '__main__':
    unittest.main()
