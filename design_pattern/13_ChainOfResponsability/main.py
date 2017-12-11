from NewLockHandler import NewLockHandler
from ComplainHandler import ComplainHandler
from FanHandler import FanHandler
from SpamHandler import SpamHandler

def main():
	print("")

	complain_handler = ComplainHandler('Agente 1')
	fan_handler = FanHandler('Agente 2')
	new_lock_handler = NewLockHandler('Agente 3')
	spam_handler = SpamHandler('Agente 4')

	complain_handler.HandleRequest("Mensagem 1\n")
	fan_handler.HandleRequest("Mensagem 2\n")
	new_lock_handler.HandleRequest("Mensagem 3\n")
	spam_handler.HandleRequest("Mensagem 4\n")

if __name__ == "__main__":
	main()