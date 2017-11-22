from factory import ShapeFactory


def main():
    factory = ShapeFactory()

    shape = factory.produce("Elipse")
    
    shape.draw()
    shape.erase()


if __name__ == '__main__':
    main()