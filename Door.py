from machine import Pin
import time

class Chickerdoor():

    def __init__(self, close_Relay_1, close_Relay_2, open_Relay_1, open_Relay_2, default_state_relays, sunrises, sunsets, min_buffer_evening, open_close_button, check_button, start_state_door, rtc):

        self.close_relay_1 = Pin(close_Relay_1, Pin.OUT)
        self.close_relay_2 = Pin(close_Relay_2, Pin.OUT)

        self.open_relay_1  = Pin(open_Relay_1, Pin.OUT)
        self.open_relay_2  = Pin(open_Relay_2, Pin.OUT)

        #set all Relay's in default(off)
        self.close_relay_1(default_state_relays)
        self.close_relay_2(default_state_relays)

        self.open_relay_1(default_state_relays)
        self.open_relay_2(default_state_relays)

        #var to save the state of thes tate door
        self.state = start_state_door

        #to contol relays later
        self.default_state_relays = default_state_relays

        self.sunrises = sunrises
        self.sunsets  = sunsets

        #a button to open/close the door
        self.open_close_button = Pin(open_close_button, Pin.IN , Pin.PULL_DOWN)

        #a button to chseck if the door is closed (0 = open, 1 = close)
        self.check_button = Pin(check_button, Pin.IN, Pin.PULL_DOWN)
        
        self.rtc = rtc

        #to have an buffer at the evening for the chickens to go in
        self.min_buffer_evening = min_buffer_evening

    def state_open_close_Button(self):
        return self.open_close_button.value()

    def check_button(self):
        return self.check_button.value()
        
    def open(self):
        if self.state == "close":
            self.open_relay_1(not self.default_state_relays)
            self.open_relay_2(not self.default_state_relays)

            #time needed to open door: ca.35sec
            counter = 0

            while counter < 350:
                if self.state_open_close_Button():
                    counter = 350
                counter +=1
                time.sleep_ms(100)

            self.open_relay_1(self.default_state_relays)
            self.open_relay_2(self.default_state_relays)

            self.state = "open"

    def close(self):

        if self.state == "open":
            self.close_relay_1(not self.default_state_relays)
            self.close_relay_2(not self.default_state_relays)

            #time needed to open door: ca.35sec
            counter = 0

            while counter < 350:
                if self.state_open_close_Button():
                    counter = 350
                counter +=1
                time.sleep_ms(100)

            self.close_relay_1(self.default_state_relays)
            self.close_relay_2(self.default_state_relays)

            self.state = "close"

    def check_state(self):

        #getting information out of the RTC
        month = int(str(self.rtc.datetime()).replace(("("), "").replace(")","").split(",")[1])
        day   = int(str(self.rtc.datetime()).replace(("("), "").replace(")","").split(",")[2])

        hour = int(str(self.rtc.datetime()).replace(("("), "").replace(")","").split(",")[4])
        minute = int(str(self.rtc.datetime()).replace(("("), "").replace(")","").split(",")[5])

        #getting values out of the lists
        sunrise   = self.sunrises.get("%s,%s" % (month,day))
        sunset = self.sunsets.get("%s,%s" % (month,day))

        #checking the time

        #subtrac 30 min from time to get a buffer for the chickens to go in
        #also needed to make sure the door wont open automatic nigthtimes
        minute_for_evening = minute
        hour_for_evening = hour
        
        minute_for_evening -= self.min_buffer_evening
        
        if minute_for_evening < 0:
            hour_for_evening -= 1
            minute_for_evening = 60 - int((minute_for_evening**2)**0.5)
        
        #if time = sunrise ----> open door
        if [hour, minute] == sunrise and self.state == "close":
            self.open()
            
        #if time = sunset -----> close door
        elif [hour_for_evening, minute_for_evening] == sunset and self.state =="open":
            self.close()
