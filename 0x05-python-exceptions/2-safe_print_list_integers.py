def safe_print_list_integers(my_list=[], x=0):
    printed_integers = 0

    try:
        for i in range(x):
            value = my_list[i]
            if isinstance(value, int):
                print("{:d}".format(value), end="")
                printed_integers += 1
    except IndexError:
        import traceback
        traceback.print_exc()

    finally:
        print()
    
    return printed_integers
