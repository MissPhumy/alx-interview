#!/usr/bin/python3
'''A script that reads stdin line by line and computes metrics'''

import sys

# Initialize cache for storing HTTP status code counts
cache = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
counter = 0

try:
    for line in sys.stdin:
        try:
            # Split the line by spaces
            line_list = line.split(" ")
            
            # Ensure the line has enough parts to extract status code and size
            if len(line_list) > 4:
                # Extract status code and size from the line
                code = line_list[-2]
                size = int(line_list[-1])
                
                # Update the cache for the status code
                if code in cache.keys():
                    cache[code] += 1
                
                # Update the total file size
                total_size += size
                
                # Increment the line counter
                counter += 1

                # Print metrics every 10 lines
                if counter == 10:
                    counter = 0
                    print('File size: {}'.format(total_size))
                    for key, value in sorted(cache.items()):
                        if value != 0:
                            print('{}: {}'.format(key, value))
        
        except ValueError:
            # Handle cases where conversion to int fails
            continue
        except IndexError:
            # Handle cases where line format is incorrect
            continue

except KeyboardInterrupt:
    # Handle script interruption (e.g., Ctrl+C)
    pass

finally:
    # Print final metrics
    print('File size: {}'.format(total_size))
    for key, value in sorted(cache.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
