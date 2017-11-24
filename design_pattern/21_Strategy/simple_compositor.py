from compositor import Compositor

class SimpleCompositor(Compositor):
    #SimpleCompositor examina os components linha a linha para determinar onde
    #devem ir os line breaks.
    def compose(natural, stretch, shrink, component_count, line_width, breaks):
        #trecho do algoritmo omitido para manter a brevidade.
        #...
        pass

#SimpleCompositor só utiliza o tamanho natural dos components, passado pelo
#compose.
