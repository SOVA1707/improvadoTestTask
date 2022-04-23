from vk.Friends import get_friends_info
from scenario.Output import print_friends_table, to_csv, to_tsv, to_json
import sys


def __save_report(friends_info):
    output_ext = sys.argv[3].lower() if len(sys.argv) > 3 else 'csv'
    output_path = sys.argv[4] if len(sys.argv) > 4 else 'report'
    filename = output_path + '.' + output_ext
    if output_ext == 'csv':
        to_csv(friends_info, filename)
    elif output_ext == 'tsv':
        to_tsv(friends_info, filename)
    elif output_ext == 'json':
        to_json(friends_info, filename)
    else:
        print('\n  Invalid file extension input. File not saved!\n')


try:
    TOKEN = sys.argv[1]
    USER_ID = sys.argv[2]
    friends_info_list = get_friends_info(USER_ID, TOKEN)
    print_friends_table(friends_info_list)
    __save_report(friends_info_list)
except IndexError:
    print("  Missing parameters. Exit program.")
    quit()
