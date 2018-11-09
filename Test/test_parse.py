import sys
sys.path.append('..')
from Parse import parse_multiple_key


def main():
    test_data = {
        'app_msg_ext_info': {
            'comm_msg_info': {
                'datetime': 1537230773,
            },
        },
    }
    test_data2 = {'app_msg_ext_info': {'comm_msg_infos': 123}}
    test_string = 'app_msg_ext_info.comm_msg_info.datetime'
    assert parse_multiple_key(test_data, test_string) == 1537230773
    assert parse_multiple_key(test_data2, test_string) == None


if __name__ == '__main__':
    main()
