#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    int_str = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            int_str += 1
        except (ValueError, TypeError):
            continue
    print("")
    return int_str
