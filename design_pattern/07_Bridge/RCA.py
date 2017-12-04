from TV import *

class RCA(TV):

    def on(self):
        print("A TV está ligada")

    def off(self):
        print("A TV está desligada")

    def tune_channel(self, channel):
        print("Canal {}".format(channel))
        
