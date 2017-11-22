class ConfigManager():
    class __Singleton():

        def __init__(self):
            self._is_instantiated = False
            self._instance = None
            self._server_name = "iaia"

        def get_instance(self):
            if(self._is_instantiated == False):
                self._instance = ConfigManager()
                self._is_instantiated = True
                return self._instance
            else:
                return self._instance

    singleton = __Singleton()

    def get_server_name(self):
        return self.singleton._server_name

    def set_server_name(self, server_name):
        self.singleton._server_name = server_name

    def get_instance(self):
        return self.singleton.get_instance()
