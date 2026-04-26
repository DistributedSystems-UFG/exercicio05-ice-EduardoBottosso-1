import sys, Ice
import Demo
 
class PrinterI(Demo.Printer):
    def addPrefix(self, s):
        return "Servidor diz: " + s
     
    def formatText(self, s, current=None):
        return s.upper()
 
    def printString(self, s, current=None):
        s = self.formatText(s)
        s = self.addPrefix(s)
        print(s)

communicator = Ice.initialize(sys.argv) 

adapter = communicator.createObjectAdapterWithEndpoints("SimpleAdapter", "default -p 11000")
object = PrinterI()
adapter.add(object, communicator.stringToIdentity("SimplePrinter"))
adapter.activate()

communicator.waitForShutdown()
