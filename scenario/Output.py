import csv
import json


def print_friends_table(friend_list):
    page_size = 15
    page_number = 0
    str = "{:<20} {:<20} {:<20} {:<20} {:<10} {:<6}"
    while True:
        print(f'Page {page_number + 1}')
        # Print the names of the columns.
        print(str.format('First Name', 'Last Name', 'Country', 'City', 'Birthday', 'Gender'))

        # Print each data item.
        start_index = page_number * page_size
        section = friend_list[start_index:start_index + page_size]
        for friend in section:
            fname = friend['first_name']
            lname = friend['last_name']
            sex = friend['sex']
            bdate = friend['bdate']
            city = friend['city']
            country = friend['country']
            print(str.format(fname, lname, country, city, bdate, sex))

        # Listen command.
        command = input('Input (next/prev/close): ')
        if command == 'next':
            if page_number < (len(friend_list) // page_size):
                page_number += 1
        elif command == 'prev':
            if page_number > 0:
                page_number -= 1
        elif command == 'close':
            return
        else:
            print('Written incorrect command.')


__headers = ['first_name', 'last_name', 'country', 'city', 'bdate', 'sex']


def to_csv(friend_list, path):
    with open(path, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=__headers)
        writer.writeheader()
        writer.writerows(friend_list)


def to_tsv(friend_list, path):
    with open(path, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=__headers, dialect='excel-tab')
        writer.writeheader()
        writer.writerows(friend_list)


def to_json(friend_list, path):
    with open(path, 'w') as file:
        json.dump(friend_list, file)
