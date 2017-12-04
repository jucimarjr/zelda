class gumballMachine:
    global state, count, SOLD_OUT, NO_QUARTER, HAS_QUARTER, SOLD
    SOLD_OUT = 0  # NAO MUDA DE VALOR
    NO_QUARTER = 1  # NAO MUDA DE VALOR
    HAS_QUARTER = 2  # NAO MUDA DE VALOR
    SOLD = 3  # NAO MUDA DE VALOR
    state = SOLD_OUT
    count = 0
    print("Wayne Enterprises.")
    def __init__(self,count):
        global state, SOLD_OUT, NO_QUARTER, HAS_QUARTER, SOLD
        self.count = count
        if(count > 0):
            state = NO_QUARTER
        #return None

    def insertQuarter (self):
        global state, count, SOLD_OUT, NO_QUARTER, HAS_QUARTER, SOLD
        if(state == HAS_QUARTER):
            print ("Voce nao pode inserir um quarto.")
        elif(state == SOLD_OUT):
            print ("Voce nao pode inserir um quarto, a maquina esta esgotada.")
        elif(state == SOLD):
            print ("Aguarde, nos ja estamos lhe dando um chiclete.")
        elif(state == NO_QUARTER):
            state = HAS_QUARTER
            print ("Voce inseriu um quarto.")

    def ejectQuarter (self):
        global state, count, SOLD_OUT, NO_QUARTER, HAS_QUARTER, SOLD
        if(state == HAS_QUARTER):
            print ("Quarto retornado.")
            state = NO_QUARTER
        elif(state == SOLD_OUT):
            print ("Voce nao pode ejetar, voce ainda nao inseriu um quarto.")
        elif(state == SOLD):
            print ("Desculpe, você já virou a manivela.")
        elif(state == NO_QUARTER):
            print ("Voce nao inseriu um quarto.")

    def turnCrank(self):
        global state, count, SOLD_OUT, NO_QUARTER, HAS_QUARTER, SOLD
        if(state == SOLD):
            print ("Virar duas vezes nao te dara outro chiclete.")
        elif(state == SOLD_OUT):
            print ("Voce virou, mas nao ha chicletes.")
        elif(state == HAS_QUARTER):
            print ("Voce virou...")
            state = SOLD
            gumballMachine.dispense(self)
        elif(state == NO_QUARTER):
            print ("Voce virou mas nao tem um quarto.")

    def dispense(self):
        global state, count, SOLD_OUT, NO_QUARTER, HAS_QUARTER, SOLD
        if(state == SOLD):
            print("O chiclete esta rolando para fora do slot.")
            count = count - 1
            if(count == 0):
                print("Oops, sem chicletes!")
                state = SOLD_OUT
            else:
                state = NO_QUARTER
        elif(state == NO_QUARTER):
            print("Voce tem que pagar primeiro.")
        elif(state == SOLD_OUT):
            print("Nenhum chiclete dispensado.")
        elif(state == HAS_QUARTER):
            print("Nenhum chiclete dispensado.")