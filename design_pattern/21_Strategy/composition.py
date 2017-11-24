from compositor import Compositor
from array_compositor import ArrayCompositor
from simple_compositor import SimpleCompositor
from tex_compositor import TexCompositor

class Composition:
    __compositor = []
    __components = [] #lista de componentes
    __component_count = 0 #número de componentes
    __line_width = 0 #tamanho da linha do Composition
    __breaks = [] #a posição do linebreak nos componentes
    __line_count = 0 #quantidade de linhas

    def __init__(self, compositor):
        self.compositor = compositor

    def repair(self):
        natural = [] #lista com tam natural de cada componente
        stretchability = [] #lista com a capacidade de cada componente de expandir
        shrinkability = [] #lista com a capacidade de cada componente de encolher

        #trecho do algoritmo que prepara as listas com os tamanhos desejados dos
        #componentes. Trecho omitido para manter a brevidade do exemplo.
        #...

        #determinando on ficarão os linebreaks
        break_count = 0
        break_count = self.compositor.compose(natural, stretchability, shrinkability, self.__component_count, self.__line_width, self.__breaks)

        #trecho do algoritmo que dispõe os components do documento. Também
        #omitido para manter a brevidade.
        #...
