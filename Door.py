class Chickerdoor():

    def __init__(int:close_Relay_1, int:close_Relay_2, int:open_Relay_1, int:Relay_2, bool:default_state_Relays, dict:sunrises, dict:sunrises, int:open_close_Button, LoRa_UART_Module, str:start_state_door):

        from machine import Pin

        self.close_relay_1 = Pin(close_Relay_1, Pin.OUT)
        self.close_relay_2 = Pin(close_Relay_2, Pin.OUT)

        self.open_relay_1  = Pin(open_Relay_1, Pin.OUT)
        self.open_relay_2  = Pin(open_Relay_2, Pin.OUT)

        #set all Relay's in default(off)
        self.close_relay_1(default_state_Relays)
        self.close_relay_2(default_state_Relays)

        self.open_relay_1(default_state_Relays)
        self.open_relay_2(default_state_Relays)

        #var to save the state of thes tate door
        self.state = start_state_door

        #to contol relays later
        self.default_state_relays = default_state_Relays

        self.sunrises = sunrises
        self.sunsets  = sunsets
