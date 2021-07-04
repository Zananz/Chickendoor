#date and time with which shoude be started:
year = 2021
month = 7
day = 4

hour = 16
minute = 4

import Door
import LoRa_UART_Module
import sun
import time
from machine import RTC, PWM, Pin

#look for enable_start.txt if 1 start skripit else blink on board LED to show something is wrong
#if enable_start.txt holds 1 it will be changed zo 0 to protect form a start with wrong time
with open("enable_start.txt", "r") as txt:

    for line in txt:
        pass

    able = bool(int(line))

    if able == True:

        txt.close()

        with open("enable_start.txt", "w") as txt:

            txt.write("""#enable main.py to start\n
#1 enalble\n
#0 unable\n
1
""")
    else:
        txt.close()

        led = PWM(Pin(25))
        led.freq(10)

        led.duty_u16(2000)

        raise NameError("check enable_start.txt")

#show that the progam started using the onboard LED
def show_start():
    
    led = PWM(Pin(25))
    led.freq(100)
    
    for i in range(256):
        led.duty_u16(i**2)
        time.sleep_ms(4)
        
    for i in range(256):
        led.duty_u16(65025-i**2)
        time.sleep_ms(4)
        
    del led

show_start()

#init the real time clock
rtc = RTC()
rtc.datetime((year, month, day, 1, hour, minute, 0, 0))

door = Door.Chickerdoor(close_Relay_1 = 0, close_Relay_2 = 1, open_Relay_1 = 2, open_Relay_2 = 3, default_state_relays = 1, sunrises = sun.sunrises, sunsets = sun.sunsets, min_buffer_evening = 45, open_close_button = 18, check_button =19, start_state_door = "open", rtc = rtc)

LoRa = LoRa_UART_Module.LoRa_UART_Module(tx = 16, rx = 17, networkkey = "Zananz", networkID = "0004")

masange_counter = 600 #a counter to send a masange per 5min

while True:
    #check if the door is in the right state for the datetime
    #if not the door will be opend/closed
    door.check_state()

    #get and send informations about the doorstate's with LoRa_UART_Module
    
    if masange_counter == 600:
        #state_software is a str holding either "open" or "close"
        state_software = door.state

        #convert state_software to 0(open) or 1(closed)
        if state_software == "open":
            state_software = 0
        elif state_software == "close": #not else to be sure
            state_software = 1

        #door.check_button() returns either 1(for door closed) or 0(for door open)
        state_hardware = door.check_button()
        
    
        
        mesagne = str(state_software) + str(state_hardware)
        print(mesagne)
        LoRa.send(mesagne)
        
        masange_counter = 0
    
    else:
        masange_counter +=1
        
    #check if the button to open/close the door manuel
    if door.state_open_close_Button() == 1:
        while door.state_open_close_Button() == 1:
            time.sleep_ms(100)
        if door.state == "open":
            door.close()
        else:
            door.open()
    time.sleep_ms(500)
