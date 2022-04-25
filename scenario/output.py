import csv
import json


class OutputScripts:
    __HEADERS = ['first_name', 'last_name', 'country', 'city', 'bdate', 'sex']

    def print_friends_table(self, friend_list):
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
                print(str.format(friend['first_name'], friend['last_name'], friend['country'],
                                 friend['city'], friend['bdate'], friend['sex']))

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

    def to_csv(self, friend_list, path):
        with open(path, 'w') as file:
            writer = csv.DictWriter(file, fieldnames=self.__HEADERS)
            writer.writeheader()
            writer.writerows(friend_list)

    def to_tsv(self, friend_list, path):
        with open(path, 'w') as file:
            writer = csv.DictWriter(file, fieldnames=self.__HEADERS, dialect='excel-tab')
            writer.writeheader()
            writer.writerows(friend_list)

    def to_json(self, friend_list, path):
        with open(path, 'w') as file:
            json.dump(friend_list, file)
