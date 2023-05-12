#!/usr/bin/python3
"""
Reading from system input
"""
import re
import sys

if __name__ == '__main__':
    number_of_staus = {}
    possible_staus = ['200', '301', '400', '401', '403', '404', '405', '500']
    total_size = 0
    count = 0
    pattern = re.compile(
        r'^\d+\.\d+\.\d+\.\d+ - \[.+\] "GET /pro\w+/260 HTTP/1.1" (\d+) (\d+)$'
        )
    try:
        for line in sys.stdin:
            result = pattern.search(line)
            if result:
                status = result.group(1)
                size = result.group(2)
                if status in possible_staus:
                    if status in number_of_staus.keys():
                        number_of_staus[status] += 1
                    else:
                        number_of_staus[status] = 1
                total_size += int(size)
                count += 1
                if count % 10 == 0:
                    print("File Size: {}".format(total_size))
                    for key in possible_staus:
                        if key in number_of_staus.keys():
                            print("{}: {}".format(key, number_of_staus[key]))
    except Exception:
        pass
    finally:
        print("File Size: {}".format(total_size))
        for key in possible_staus:
            if key in number_of_staus.keys():
                print("{}: {}".format(key, number_of_staus[key]))
