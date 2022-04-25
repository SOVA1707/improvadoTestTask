import requests


class User:
    __VK_API_VERSION = 5.131
    __URL = "https://api.vk.com/method/friends.get"

    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id

    def get_friends_info(self):
        friends = [self.__get_required_friend_info(item) for item in self.__parse_friends()]
        return sorted(friends, key=lambda item: item['first_name'])

    def __parse_friends(self):
        friends_list = []
        count = 5000
        max_count = 30_000_000
        i = 0
        while True:
            params = {
                'user_id': self.user_id,
                'fields': 'city, country, bdate, sex',
                'count': count,
                'offset': i * count,
                'access_token': self.token,
                'v': self.__VK_API_VERSION
            }
            r = requests.post(url=self.__URL, data=params)

            if 'error' in r.json():
                print(r.json()['error']['error_msg'])
                print('Exit program.')
                quit()

            friends = r.json()['response']['items']

            friends_list = friends_list + friends
            i += 1

            if len(friends) < count:
                break
            if len(friends_list) > max_count:
                print(f'{max_count} friends limit reached. Parsing stopped.')
                break
        return friends_list

    # Selecting the required data from json
    @staticmethod
    def __get_required_friend_info(friend):
        new_friend = {'first_name': friend['first_name'],
                      'last_name': friend['last_name'],
                      'country': friend['country']['title'] if 'country' in friend else 'undefined',
                      'city': friend['city']['title'] if 'city' in friend else 'undefined',
                      'sex': 'male' if friend['sex'] == 2 else 'female'}

        try:
            dates = friend['bdate'].split('.')
            if len(dates) < 3:
                date = 'XXXX-' + '-'.join(dates[::-1])
            else:
                date = '-'.join(dates[::-1])
        except KeyError:
            date = 'XXXX-XX-XX'
        new_friend['bdate'] = date

        return new_friend
