from TreeManager import TreeManager

manager = TreeManager()

manager.draw_tree(4,1,2)

manager.include_state(4,1,2)
manager.include_state(0,5,2)
manager.include_state(4,3,5)
manager.include_state(7,8,9)

manager.display_trees()

manager.display_tree_states()