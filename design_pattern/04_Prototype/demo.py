from Dog import Dog
from Person import Person


def main():
    print("Creating person 1...")
    person1 = Person("Fred")
    print("person 1: " , person1)

    print("Cloning person 1 to become person 2...")
    person2 = person1.clone()
    print("person 2: " , person2)

    print("Creating dog 1...")
    dog1 = Dog("Wooof!")
    print("dog 1: " , dog1)

    print("Cloning dog 1 to become dog 2...")
    dog2 = dog1.clone()
    print("dog 2: " , dog2)


if __name__ == "__main__":
    main()
