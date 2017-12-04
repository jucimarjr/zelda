
# *
# * Duck interface que permite
# * um Duck quackar e voar
# *

class duck_interface(object):
    pass


# *
# * Uma subclasse de duck_interface,
# * a MallardDuck
# *

class mallard_duck(object):
    duck_interface = property()

    def quack(self):
        print("Quack")

    def fly(self):
        print("I'm flying")


# *
# * Agora conhecemos uma nova ave: a turkey.
# * Elas não quackam, fazem gobble; também
# * voam, porém por apenas poucos metros.
# *

class turkey_interface(object):
    pass


# *
# * Implementação concreta de um turkey.
# *

class wild_turkey(object):
    duck_interface = property()

    def gobble(self):
        print("Gobble gobble")

    def fly(self):
        print("I'm flying a short distance")


# *
# * Agora, digamos que você queira usar um objeto do tipo Turkey
# * no lugar de um Duck. Obviamente você não pode, pois eles possuem
# * interfaces diferentes. Então, vamos criar um Adapter.
# *


# *
# * Primeiro, você precisa implementar a interface do tipo que deseja
# * adaptar. Essa é a interface que o client espera ver.
# *

class turkey_adapter(object):
    duck_interface = property()

    def turkey_adapter(self, turkey):
        self.turkey = turkey;

    def quack(self, turkey):
        self.gobble()

    def fly(self):
        for i in range(5):
            self.fly()


# * Método para testarmos um duck

def test_duck(duck_interface):
    duck.quack()
    duck.fly()

# *
# * Test drive the adapter
# *

if __name__ == '__main__':

    # Vamos criar um duck...
    duck = mallard_duck()

    # ...e um turkey
    turkey = wild_turkey()

    # Então "embrulhe" o turkey no adapter,
    # fato que o faz parecer um duck
    turkey_adapter_obj = turkey_adapter()

    print("The turkey_interface says...")
    turkey.gobble()
    turkey.fly()

    # Testamos o duck passando-o como parâmetro para
    # o método de teste que espera um objeto do tipo duck_interface
    print("\nThe duck_interface says...")
    test_duck(duck)

    # Por fim, o grande teste: tentar passar um turkey como
    # se fosse um duck para o método teste
    print("\nThe turkey_adapter says...")
    test_duck(turkey_adapter_obj)
