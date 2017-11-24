from compositor import Compositor

class TexCompositor(Compositor):
    #TexCompositor utiliza uma abordagem com uma estratégia mais global. Ele
    #examina um parágrafo de cada vez, levando em conta o tamanho dos components
    #e suas capacidade de expandir.
    def compose(natural, stretch, shrink, component_count, line_width, breaks):
        #trecho do algoritmo omitido para manter a brevidade.
        #...
        pass

#TexCompositor utiliza TODAS as informações que são passadas a ele pelo compose.
