"""Manipulating systin
   I lov you to a new line
 """
#!/usr/bin/python3
import sys
codes_list = {
            '200': 0, '301': 0, '400': 0, '401': 0,
            '403': 0, '404': 0, '405': 0, '500': 0
            }

total_size = 0
count = 0

try:
    for line in sys.stdin:
        lines = line.split(" ")

        if len(lines) > 4:
            status = lines[-2]
            size = int(lines[-1])

            if status in codes_list.keys():
                codes_list[status] += 1

            total_size += size

            count += 1

        if count == 10:
            count = 0
            print('File size: {}'.format(total_size))

            for key, value in sorted(codes_list.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(total_size))
    for key, value in sorted(codes_list.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
