from Originator import Originator,Memento

class Caretaker ():
    savedStates = []
    originator = Originator()
    originator.set("State1")
    originator.set("State2")
    savedStates.append(originator.saveToMemento())
    originator.set("State3")
    savedStates.append(originator.saveToMemento())
    originator.set("State4")

    originator.restoreFromMemento(savedStates[1])

c = Caretaker() 
