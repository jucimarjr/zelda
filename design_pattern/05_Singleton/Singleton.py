from ConfigManager import ConfigManager

ConfigManager().get_instance().set_server_name("ConfigManager's name")
s = ConfigManager().get_server_name()

config_manager = ConfigManager().get_instance()

s1 = config_manager.get_server_name()

print "Name: " + s
print "Name: " + s1
