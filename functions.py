def produce_func(val="default"):
    internal_val = val

    def configured_func(val):
        print("internal_val (by closure)=", internal_val)
        print("val=", val)
    return configured_func


def main():
    a_func = produce_func("configuration for a_func")
    a_func("arg to a_func")


if __name__ == '__main__':
    main()
else:
    # module-specific initialization code if any
    pass
