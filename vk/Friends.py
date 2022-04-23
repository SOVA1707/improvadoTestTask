import requests

__VK_API_VERSION = 5.131
__URL = "https://api.vk.com/method/friends.get"


def get_friends_info(user_id, token):
    friends = [__get_friend_info(item) for item in __parse_friends(user_id, token)]
    return sorted(friends, key=lambda item: item['first_name'])


def __parse_friends(user_id, token):
    friends_list = []
    count = 5000
    max_count = 30_000_000
    i = 0
    while True:
        params = {
            'user_id': user_id,
            'fields': 'city, country, bdate, sex',
            'count': count,
            'offset': i * count,
            'access_token': token,
            'v': __VK_API_VERSION
        }
        r = requests.post(url=__URL, data=params)

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


# Removes unnecessary fields and updates the required fields
def __get_friend_info(friend):
    new_friend = {'first_name': friend['first_name'],
                  'last_name': friend['last_name']}

    try:
        new_friend['country'] = friend['country']['title']
    except KeyError:
        new_friend['country'] = 'undefined'

    try:
        new_friend['city'] = friend['city']['title']
    except KeyError:
        new_friend['city'] = 'undefined'

    try:
        dates = friend['bdate'].split('.')
        if len(dates) < 3:
            date = 'XXXX-' + '-'.join(dates[::-1])
        else:
            date = '-'.join(dates[::-1])
    except KeyError:
        date = 'XXXX-XX-XX'

    new_friend['bdate'] = date
    new_friend['sex'] = 'male' if friend['sex'] == 2 else 'female'
    return new_friend
