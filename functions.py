def produce_func(val="default"):
    """Create a function confgiured by closure"""
    internal_val = val

    def configured_func(val):
        print("internal_val (by closure)=", internal_val)
        print("val=", val)
    return configured_func


def append_func(a, alist=[]):
    """Argument default value is evaluated only once"""
    alist.append(a)
    return alist


def make_incrementor(n):
    """Returns lamda expression"""
    return lambda x: x + n


def main():
    a_func = produce_func("configuration for a_func")
    a_func("arg to a_func")

    my_list1 = append_func(1)
    print(my_list1)
    my_list2 = append_func(2)
    print(my_list2)
    my_list3 = append_func(3)
    print(my_list3)

    print("my_list1 == my_list2 == my_list3 is ",
          my_list1 == my_list2 == my_list3)

    increment_by_two = make_incrementor(2)
    print("3 incremented by 2 is ", increment_by_two(3))


if __name__ == '__main__':
    main()
else:
    # module-specific initialization code if any
    pass
