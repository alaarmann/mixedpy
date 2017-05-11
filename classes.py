

def main():
    my_bag = Bag()
    my_bag.add("coin")
    my_bag.addtwice("button")
    print("Inside my bag are ", my_bag.data)

    print("Attribute __class__ of String is ", "xyz".__class__)

    my_midas_bag = MidasBag()
    my_midas_bag.add("coin")
    my_midas_bag.addtwice("button")
    print("Inside my midas bag are ", my_midas_bag.data)
    print("In reverse order (iterator returned by generator method):")
    for item in my_midas_bag.reversecontent():
        print("Item is ", item)

    # wrap long line
    print("Inside my midas bag are "
          "in reverse order", my_midas_bag.reverse_data())


class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)

    # generator expression returns iterator
    def reversecontent(self):
        for index in range(len(self.data)-1, -1, -1):
            yield self.data[index]

    def reverse_data(self):
        # generator expression
        return list(self.data[i] for i in range(len(self.data)-1, -1, -1))


class MidasBag(Bag):
    def add(self, x):
        self.data.append("golden " + x)


if __name__ == '__main__':
    main()
else:
    # module-specific initialization code if any
    pass
