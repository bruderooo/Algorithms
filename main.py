if __name__ == '__main__':
    l = ["asd", "dsad"]

    print(sorted(l, key=(lambda x: (x[0], len(x)))))
