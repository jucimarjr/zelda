

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
