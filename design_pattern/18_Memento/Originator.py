class Memento():
        
        def __init__(self, stateToSave):
            self._state = stateToSave

        def getSavedState(self):
            return self._state

class Originator():
    def __init__(self):
        self._state = " "

    def set(self, state):
        print("Originator: Setting state to %s" %state)
        self._state = state

    def saveToMemento(self):
        print("Originator: Saving to Memento.")
        m = Memento(self._state)
        return m

    def restoreFromMemento(self, memento):
        self._state = memento.getSavedState()
        print("Originator: State after restoring from Memento: %s" %self._state)

    
