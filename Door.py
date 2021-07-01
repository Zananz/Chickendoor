class Chickerdoor():

    def __init__(int:close_Relay_1, int:close_Relay_2, int:open_Relay_1, int:Relay_2, bool:default_state_relays, dict:sunrises, dict:sunrises, min_buffer_evening, int:open_close_button, str:start_state_door, rtc):

        from machine import Pin
        import time

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
        self.default_state_relays = default_state_relays

        self.sunrises = sunrises
        self.sunsets  = sunsets

        self.open_close_button = Pin(open_close_button, Pin.IN , PIN.PULL_DOWN)

        self.rtc = rtc

        #to have an buffer at the evening for the chickens to go in
        self.min_buffer_evening = min_buffer_evening

    def state_open_close_Button(self):
        return self.open_close_button.value()

    def open(self):
        if self.state == "close":
            self.open_relay_1(not self.default_state_relays)
            self.open_relay_2(not self.default_state_relays)

            #time needed to open door: ca.35sec
            counter = 0

            while counter > 350:
                if self.state_open_close_Button():
                    counter = 350
                counter +=1
                time.sleep_ms(1000)

            self.open_relay_1(self.default_state_relays)
            self.open_relay_2(self.default_state_relays)

            self.state = "open"

    def close(self):
        if self.state == "open":
            self.close_relay_1(not self.default_state_relays)
            self.close_relay_2(not self.default_state_relays)

            #time needed to open door: ca.35sec
            counter = 0

            while counter > 350:
                if self.state_open_close_Button():
                    counter = 350
                counter +=1
                time.sleep_ms(1000)

            self.close_relay_1(self.default_state_relays)
            self.close_relay_2(self.default_state_relays)

            self.state = "close"

    def check_state(self):


        #getting information out of the RTC
        month = int(str(date.datetime()).replace(("("), "").replace(")","").split(",")[1])
        day   = int(str(date.datetime()).replace(("("), "").replace(")","").split(",")[2])

        hour = int(str(date.datetime()).replace(("("), "").replace(")","").split(",")[4])
        minute = int(str(date.datetime()).replace(("("), "").replace(")","").split(",")[5])

        #getting values out of the lists
        sunrise   = sunrises.get("%s,%s" % (month,day))
        sunset = sunsets.get("%s,%s" % (month,day))

        #checking the time

        #subtrac 30 min from time to get a buffer for the chickens to go in
        #also needed to make sure the door wont open automatic nigthtimes
        minute_for_evening = minute
        hour_for_evening = hour
        minute_for_evening -= self.min_buffer_evening
        if minute_for_evening < 0:
            hour_for_evening -= 1
            minute_for_evening = 60 - int((minute**2)**0.5)

        #if time = sunrise ----> open door
        if [hour, minute] >= sunrise and self.state == "close" and [hour_for_evening, minute_for_evening] < sunset:
            self.open()

        #if time = sunset -----> close door
        elif [hour_for_evening, minute_for_evening] >= sunset and self.state =="open":
            self.close()
