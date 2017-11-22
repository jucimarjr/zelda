from prototype.PrototypeHuman import PrototypeHuman


def main():
    prototypeHuman = PrototypeHuman()

    human1 = prototypeHuman.clone()
    human2 = prototypeHuman.clone()

    print(human1)
    print(human2)


if __name__ == '__main__':
    main()