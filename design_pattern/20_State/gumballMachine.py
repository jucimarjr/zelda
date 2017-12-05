from random import randint
class gumballMachine:
    global state, count, SOLD_OUT, NO_QUARTER, HAS_QUARTER, SOLD, WINNER_STATE
    SOLD_OUT = 0  # NAO MUDA DE VALOR
    NO_QUARTER = 1  # NAO MUDA DE VALOR
    HAS_QUARTER = 2  # NAO MUDA DE VALOR
    SOLD = 3  # NAO MUDA DE VALOR
    WINNER_STATE = 4 #NAO MUDA DE VALOR
    state = SOLD_OUT
    count = 0
    result = ""
    def __init__(self,count):
        global state, SOLD_OUT, NO_QUARTER, HAS_QUARTER, SOLD, WINNER_STATE
        self.count = count
        if(count > 0):
            state = NO_QUARTER
        else:
            state = SOLD_OUT

    def winnerState (self):
        global state, count, SOLD_OUT, NO_QUARTER, HAS_QUARTER, SOLD, WINNER_STATE
        total = randint(1,10)
        if(total == 1 and count >= 2):
            state = WINNER_STATE
        else:
            state = state


    def insertQuarter (self):
        global state, count, SOLD_OUT, NO_QUARTER, HAS_QUARTER, SOLD, WINNER_STATE
        if(state == HAS_QUARTER):
            print ("Voce nao pode inserir um quarto.")
        elif(state == SOLD_OUT):
            print ("Voce nao pode inserir um quarto, a maquina esta esgotada.")
        elif(state == SOLD):
            print ("Aguarde, nos ja estamos lhe dando um chiclete.")
        elif(state == NO_QUARTER):
            if(self.count > 0):
                state = HAS_QUARTER
                print ("Voce inseriu um quarto.")
            else:
                print("Voce nao pode inserir um quarto, a maquina esta esgotada.")
                state = SOLD_OUT
        elif(state == WINNER_STATE):
            state = NO_QUARTER


    def ejectQuarter (self):
        global state, count, SOLD_OUT, NO_QUARTER, HAS_QUARTER, SOLD, WINNER_STATE
        if(state == HAS_QUARTER):
            print ("Quarto retornado.")
            state = NO_QUARTER
        elif(state == SOLD_OUT):
            print ("Voce nao pode ejetar, voce ainda nao inseriu um quarto.")
        elif(state == SOLD):
            print ("Desculpe, você já virou a manivela.")
        elif(state == NO_QUARTER):
            print ("Voce nao inseriu um quarto.")
        elif(state == WINNER_STATE):
            state = WINNER_STATE


    def turnCrank(self):
        global state, count, SOLD_OUT, NO_QUARTER, HAS_QUARTER, SOLD, WINNER_STATE
        if(state == SOLD):
            print ("Virar duas vezes nao te dara outro chiclete.")
        elif(state == SOLD_OUT):
            print ("Voce virou, mas nao ha chicletes.")
        elif(state == HAS_QUARTER):
            print("Voce virou...")
            gumballMachine.winnerState(self)
            if(state == WINNER_STATE):
                print("Voce ganhou um chiclete a mais.")
                state = SOLD
                gumballMachine.dispense(self)
            state = SOLD
            gumballMachine.dispense(self)
        elif(state == NO_QUARTER):
            print ("Voce virou mas nao tem um quarto.")
        elif(state == WINNER_STATE):
            print("'-'")



    def dispense(self):
        global state, count, SOLD_OUT, NO_QUARTER, HAS_QUARTER, SOLD, WINNER_STATE
        if(state == SOLD):
            if(self.count > 0):
                print("O chiclete esta rolando para fora do slot.")
                self.count = self.count - 1
                state = NO_QUARTER
            else:
                print("Oops, sem chicletes!")
                state = SOLD_OUT

        elif(state == NO_QUARTER):
            print("Voce tem que pagar primeiro.")
        elif(state == SOLD_OUT):
            print("Nenhum chiclete dispensado.")
        elif(state == HAS_QUARTER):
            print("Nenhum chiclete dispensado.")
        elif(state == WINNER_STATE):
            print("Voce já ganhou seu chiclete extra.")

    def __str__(self):
        global state, count, SOLD_OUT, NO_QUARTER, HAS_QUARTER, SOLD, WINNER_STATE
        result = ""
        result += "\nO Incrivel mundo de Gumball, Inc."
        result += "\nPython-enabled Stading Gumball Model #2017"
        result += "\nInventory: " + str(self.count) + " gumball"

        if self.count == 1:
            result += "s"
        result += "\n"
        result += "Machine is " + str(state) + "\n"
        return result