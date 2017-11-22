

"""
	Adapter converte a interface de uma classe em outra interface que 
melhor se adapta às necessdades do cliente.
	Ele torna possível o trabalho conjunto de duas classes que antes não
poderiam se juntar devido às suas interfaces incompatíveis.
"""

import exemplo


class Target(metaclass=exemplo.EXMeta):
    """
    Particularidades da interface que será exibida ao cliente.
    """

    def __init__(self):
        self._adaptee = Adaptee()

    @exemplo.abstractmethod
    def request(self):
        pass


class Adapter(Target):
    """
	Adapta a interface de Adaptee para a interface Target.
    """

    def request(self):
        self._adaptee.specific_request()


class Adaptee:
    """
	Define uma interface existente que precisa ser adaptada.
    """

    def specific_request(self):
        pass


def main():
    adapter = Adapter()
    adapter.request()


if __name__ == "__main__":
    main()
	

	
