import requests

__VK_API_VERSION = 5.131
__URL = "https://api.vk.com/method/friends.get"


def get_friends_info(user_id, token):
    friends = __parse_friends(user_id, token)

    for friend_info in friends:
        __reformat_friend_info(friend_info)

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
def __reformat_friend_info(friend):
    friend.pop('id')
    friend.pop('can_access_closed')
    friend.pop('is_closed')
    friend.pop('track_code')

    try:
        friend['country'] = friend['country']['title']
    except KeyError:
        friend['country'] = 'undefined'

    try:
        friend['city'] = friend['city']['title']
    except KeyError:
        friend['city'] = 'undefined'

    try:
        dates = friend['bdate'].split('.')
        if len(dates) < 3:
            date = 'XXXX-' + '-'.join(dates[::-1])
        else:
            date = '-'.join(dates[::-1])
    except KeyError:
        date = 'XXXX-XX-XX'

    friend['bdate'] = date
    friend['sex'] = 'male' if friend['sex'] == 2 else 'female'
