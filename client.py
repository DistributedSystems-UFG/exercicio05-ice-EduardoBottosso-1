import sys, Ice
import Demo
 
communicator = Ice.initialize(sys.argv)

base1 = communicator.stringToProxy("SimplePrinter1:tcp -h 54.234.163.189 -p 11000")
base2 = communicator.stringToProxy("SimplePrinter2:tcp -h 54.234.163.189 -p 11000")

printer1 = Demo.PrinterPrx.checkedCast(base1)
printer2 = Demo.PrinterPrx.checkedCast(base2)

if (not printer1) or (not printer2):
    raise RuntimeError("Invalid proxy")

printer1.printString("Hello World from object 1!")
printer1.printUpperText("Hello World from object 1!")

printer2.printString("Hello World from object 2!")
printer2.printUpperText("Hello World from object 2!")

communicator.destroy()
