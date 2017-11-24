from composition import Composition
from compositor import Compositor
from array_compositor import ArrayCompositor
from simple_compositor import SimpleCompositor
from tex_compositor import TexCompositor

def main():
    quick = Composition(SimpleCompositor)
    slick = Composition(TexCompositor)
    iconic = Composition(ArrayCompositor)

main()
