from Tree import Tree

class TreeManager:

    def __init__(self):

        self.__tree = Tree()
        self.__tree_states = {}
    
    def include_state(self, x, y, age):
        if age not in self.__tree_states:
            self.__tree_states[age] = [(x,y)]
        elif (x,y) not in self.__tree_states[age][0]:
            self.__tree_states[age].append((x,y))
    
    def draw_tree(self, age, x, y):

        if age not in self.__tree_states:
            self.__tree_states[age] = [(x,y)]
            self.__tree.display(x, y, age)

        elif (x,y) not in self.__tree_states[age][0]:
            self.__tree_states[age].append((x,y))
            self.__tree.display(x, y, age)

        else:
            __tree.draw_tree(x, y, age)

    def display_trees(self):
        for age, coordinates in self.__tree_states.items():
            for coordinate in coordinates:
                self.__tree.display(coordinate[0], coordinate[1], age)
    
    def display_tree_states(self):
        print(self.__tree_states)