import abc

class Pedido(metaclass=abc.ABCMeta):

    def __init__(self, status):
        self.status = status

    def alterar(self):
        return self.status

    def cancelar(self):
        return self.status

    def enviar(self):
        return self.status

    def setStatus(self, status):
        self.status = status

    def getStatus(self, status):
        return status



class PedidoCancelado:
    def alterar(self):
        print("Não é possível realizar alterações. Este pedido está cancelado.")

    def cancelar(self):
        print("O pedido já foi cancelado.")

    def enviar(self):
        print("Não é possível realizar o envio do pedido. Este pedido está cancelado.")


class PedidoEnviado:
    def alterar(self):
        print("Não é possível realizar alterações. O pedido já foi enviado.")

    def cancelar(self, pedido):
        print("Pedido enviado cancelado, será realizada a devolução do pedido.")
        pedido.setStatus(PedidoCancelado())

    def enviar(self):
        print("Pedido já está em processo de envio.")

class PedidoEmprocesso:
    def alterar(self):
        print("O pedido em processamento está sendo alterado.")

    def cancelar(self, pedido):
        print("O pedido em processamento foi cancelado.")
        pedido.setStatus(PedidoCancelado())

    def enviar(self, pedido):
        print("O pedido em processamento foi enviado.")
        pedido.setStatus(PedidoEnviado())

class StatusPedido:
    @abc.abstractmethod
    def alterar(self):
        pass
    def cancelar(self):
        pass
    def enviar(self):
        pass

class Status:

        pedido1 = Pedido()
        pedido1.setStatus(PedidoEmprocesso())

        pedido1.alterar()
        pedido1.cancelar()
        pedido1.enviar()

        pedido2 = Pedido()
        pedido2.setStatus(PedidoCancelado())

        pedido2.alterar()
        pedido2.cancelar()
        pedido2.enviar()

        pedido3 = Pedido()
        pedido3.setStatus(PedidoEnviado())

        pedido3.alterar()
        pedido3.cancelar()
        pedido3.enviar()