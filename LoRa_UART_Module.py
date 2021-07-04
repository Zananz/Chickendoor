#a class to manage the SX1276 UART module with M= and M1 pulled down
class LoRa_UART_Module():

    def __init__(self, tx , rx, networkkey, networkID):

        self.tx = int(tx)
        self.rx = int(rx)

        self.networkkey = networkkey
        self.networkID  = networkID

        from machine import UART, Pin

        if self.tx == 0 or self.tx == 12 or self.tx == 16:
            if self.rx == 1 or self.rx == 13 or self.rx == 17:

                self.uart = UART(0, 9600, tx = Pin(self.tx), rx = Pin(self.rx))
            else: #if tx and rx dosnt fit together
                raise UARTEerror("tx and rx dosnt fit together... they need to be from same chanal")

        elif self.tx == 4 or self.tx == 8:
            if self.rx == 5 or self.rx == 9:

                self.uart = UART(1, 9600, tx = Pin(self.tx), rx = Pin(self.rx) )
            else: #if tx and rx dosnt fit together
                raise UARTerror("tx and rx dosnt fit together... they need to be from same chanal")

        if not self.uart:
            raise UARTerror("something goes wrong check out... LoRa_UART_Module: def __init__")

    def send(self, mesagne):
        self.uart.write("%s%s%s"%(self.networkkey, self.networkID, mesagne))

    def read(self):
        self.uart.read()

    def readline(self):
        self.uart.readline()
