from Factory import ShapeFactory


def main():
    factory = ShapeFactory()

    shape = factory.produce("Triangle")
    
    shape.draw()
    shape.erase()


if __name__ == '__main__':
    main()