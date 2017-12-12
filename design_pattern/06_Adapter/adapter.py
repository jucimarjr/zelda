from duck_interface import *
from wild_turkey import *
from mallard_duck import *
from turkey_adapter import *
from turkey_interface import *
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
