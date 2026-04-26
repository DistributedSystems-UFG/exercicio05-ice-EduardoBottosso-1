import sys, Ice
import Demo
 
class PrinterI(Demo.Printer):
    def addPrefix(self, s):
        return "Servidor diz: " + s
     
    def printUpperText(self, s, current=None):
        print (s.upper())
 
    def printString(self, s, current=None):
        s = self.addPrefix(s.upper())
        print(s)
     
class PrinterII(Demo.Printer):
    def addPrefix(self, s):
        return "Servidor 2 diz: " + s
     
    def printUpperText(self, s, current=None):
        print ("Objeto2: " ,s.upper())
 
    def printString(self, s, current=None):
        s = self.addPrefix(s.upper())
        print(s)

communicator = Ice.initialize(sys.argv) 

adapter = communicator.createObjectAdapterWithEndpoints("SimpleAdapter", "default -p 11000")
object1 = PrinterI()
object2 = PrinterII()
adapter.add(object1, communicator.stringToIdentity("SimplePrinter1"))
adapter.add(object2, communicator.stringToIdentity("SimplePrinter2"))
adapter.activate()

communicator.waitForShutdown()
