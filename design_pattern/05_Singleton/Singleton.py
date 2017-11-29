class ChocolateBoiler():
    class __Singleton():

        def __init__(self):
            self._is_instantiated = False
            self._instance = None
            self.empty = True
            self.boiled = False

        def print_boiler_state(self):
            print("empty  : " + str(self.empty))
            print("boiled : " + str(self.boiled))

        def get_instance(self):
            if(self._is_instantiated == False):
                self._instance = ChocolateBoiler()
                self._is_instantiated = True
                return self._instance
            else:
                return self._instance

    singleton = __Singleton()

    def fill(self):
        if(self.singleton.empty == True):
            self.singleton.empty = False
            self.singleton.boiled = False
            self.print_boiler_state()

    def drain(self):
        if(self.singleton.empty == False and self.singleton.boiled == True):
            self.singleton.empty = True
        self.print_boiler_state()

    def boil(self):
        if(self.singleton.empty == False and self.singleton.boiled == False):
            self.singleton.boiled = True
        self.print_boiler_state()

    def print_boiler_state(self):
        self.singleton.print_boiler_state()

    def get_instance(self):
        return self.singleton.get_instance()
