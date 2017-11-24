from compositor import Compositor

class ArrayCompositor(Compositor):
    #ArrayCompositor quebra os components em linhas utilizando um intervalo
    #regular.
    def compose(natural, stretch, shrink, component_count, line_width, breaks):
        #trecho do algoritmo omitido para manter a brevidade.
        #...
        pass

#ArrayCompositor ignora todas as informações passada para ele pelo compose
