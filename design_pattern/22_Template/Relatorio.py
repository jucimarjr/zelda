import abc

class Relatorio():

    def montarRelatorio(self):
        return str(self.montarCabecalho()) + " " + str(self.montarCorpo()) + " " + str(self.montarRodape())

    @abc.abstractmethod
    def montarCabecalho(self):
        pass

    @abc.abstractmethod
    def montarCorpo(self):
        pass

    @abc.abstractmethod
    def montarRodape(self):
        pass

class RelatorioUmidade(Relatorio):

    def montarCabecalho(self):
        return "Relatorio de Umidade"
    def montarCorpo(self):
        return "Apresenta a escala de umidade"
    def montarRodape(self):
        return "Data do acontecimento da umidade"

class RelatorioTerremoto(Relatorio):

    def montarCabeçalho(self):
        return "Relatório de Terremoto"
    def montarCorpo(self):
        return "Apresenta a escala de terremoto"
    def montarRodape(self):
        return "Data do acontecimento"
    
class Template(metaclass=abc.ABCMeta):
    if __name__ == '__main__':
        terremoto = RelatorioTerremoto()
        umidade = RelatorioUmidade()

        print(terremoto.montarRelatorio())
        print(umidade.montarRelatorio())


