

class Command():
    def execute(self):
        self.execute = execute


class BtnBook(Command):
    def __init__(self, m):
        self.med = m
        self.registerBook(self) 

    def execute(self):
        self.med.book = med.book()

    def setEnable(self, b):
        if (b == True):
            print ("BtnBook Enable")
        else:
            print ("BtnBook Disable")


class BtnSearch(Command):
    def __init__(self, m):
        self.med = m
        self.med.registerSearch(self) 

    def setEnable(self, b):
        if (b == True):
            print ("BtnSearch Enable")
        else:
            print ("BtnSearch Disable")

    def execute(self):
        self.med.search = med.search()


class BtnView(Command):
    def __init__(self, m):
        self.med = m
        self.med.registerView(self) 
        
    def setEnable(self, b):
        if(b == True):
            print("BtnView Enable")
        else:
            print("BtnView Disable")

    def execute (self):
        self.med.view = med.view()

    
class IMediator():
    def book(self):
        self.book = book

    def view(self):
        self.view = view

    def search(self):
        self.search = search

    def registerView(self, v):
        self.registerView = v

    def registerSearch(self, s):
        self.registerSearch = s

    def registerDisplay(self, d):
        self.registerDisplay = d

    def registerBook(self, btnView):
        self.registerView = btnView


class LblDisplay():
    def __init__(self, m):
        self.med = m
        self.med.registerDisplay(self) 

    def setText(string):
        print(string)


class Mediator(IMediator):
    def registerView(self, v):
        self.btnView = v

    def def registerSearch(self, s):
        self.btnSearch = s

    def registerBook(self, b):
        self.btnBook = b

    def registerDisplay(self, d):
        self.show = d

    def book(self):
        self.btnView.setEnable(True)
        self.btnSearch.setEnable(True)
        self.btnBook.setEnable(False)
        self.show.setText("booking...")

    def view(self):
        self.btnView.setEnable(False)
        self.btnSearch.setEnable(True)
        self.btnBook.setEnable(True)
        self.show.setText("viewing...")

    def search(self):
        self.btnView.setEnable(True)
        self.btnSearch.setEnable(False)
        self.btnBook.setEnable(True)
        self.show.setText("searching...")


class MediatorDemo():
    def __init__(self):
        self.btnBook = BtnBook(med)
        self.btnSearch = BtnSearch(med)
        self.btnView = BtnView(med)
        self.label = LblDisplay(med)

        med.book()
        med.search()
        med.view()
        label.setText("Hello Word")



MediatorDemo()
    
    
