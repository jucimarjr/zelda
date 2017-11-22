from EmailLogger import EmailLogger
from StderrLogger import StderrLogger
from StdoutLogger import StdoutLogger

def main():
    #x1 = Logger()
    x2 = EmailLogger(None)
    x3 = StderrLogger(None)
    x4 = StdoutLogger(None)
    x2.writeMessage("1");
    x3.writeMessage("2");
    x4.writeMessage("3");

if __name__ == "__main__":
    main()
