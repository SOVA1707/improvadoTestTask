import sys

from scenario.output import OutputScripts
from vk.user import User


try:
    user1 = User(sys.argv[1], sys.argv[2])
    out = OutputScripts()
    output_ext = sys.argv[3].lower() if len(sys.argv) > 3 else 'csv'
    output_path = sys.argv[4] if len(sys.argv) > 4 else 'report'
    filename = output_path + '.' + output_ext

    user1_friends_info = user1.get_friends_info()

    out.print_friends_table(user1_friends_info)

    if output_ext == 'csv':
        out.to_csv(user1_friends_info, filename)
    elif output_ext == 'tsv':
        out.to_tsv(user1_friends_info, filename)
    elif output_ext == 'json':
        out.to_json(user1_friends_info, filename)
    else:
        print('\n  Invalid file extension input. File not saved!\n')
except IndexError:
    print("  Missing required parameters. Exit program.")
    quit()
