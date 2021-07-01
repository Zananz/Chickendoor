#date and time with which shoude by started:
year = 2020
month = 10
day = 31
day_oft_the_week = 6  #monday = 1, tuesday = 2, ... #not imprtend for code just for completeness

hour = 14
minute = 46

from machine import RTC #real time clock
import time
from machine import Pin, PWM

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
                         0\
                         """)
    else:
        txt.close()
        
        led = PWM(Pin(25))
        led.freq(10)
        
        led.duty_u16(2000)
        
        while True:
            time.sleep(99999999)
            
#start will be shown using the on board LED
def show_start():
    
    led = PWM(Pin(25))
    led.freq(1000)
    
    for i in range(255):
        
        led.duty_u16(i**2)
        
        time.sleep_ms(5)
        
    for i in range(255):
        
        led.duty_u16(65025 - i**2)
        
        time.sleep_ms(5)
        
    led.deinit()
    
show_start()

#pin1/2  high ---> open door, pin3/4  high ---> close door
pin_1 = Pin(0,Pin.OUT)
pin_2 = Pin(1,Pin.OUT)
pin_3 = Pin(2,Pin.OUT)
pin_4 = Pin(3,Pin.OUT)

pin_1.low()
pin_2.low()
pin_3.low()
pin_4.low()

#init the real time clock
datum = RTC()
datum.datetime((year, month, day, day_oft_the_week, hour, minute, 0, 0))

#keys = date, vaules = time( [0] = hour, [1] = minute )
sunrises = { "1,1" : [7,17],
                    "1,2" : [7,17],
                    "1,3" : [7,17],
                    "1,4" : [7,16],
                    "1,5" : [7,16],
                    "1,6" : [7,16],
                    "1,7" : [7,15],
                    "1,8" : [7,15],
                    "1,9" : [7,14],
                    "1,10" : [7,14],
                    "1,11" : [7,13],
                    "1,12" : [7,12],
                    "1,13" : [7,12],
                    "1,14" : [7,11],
                    "1,15" : [7,10],
                    "1,16" : [7,9],
                    "1,17" : [7,8],
                    "1,18" : [7,7],
                    "1,19" : [7,6],
                    "1,20" : [7,5],
                    "1,21" : [7,4],
                    "1,22" : [7,3],
                    "1,23" : [7,2],
                    "1,24" : [7,0],
                    "1,25" : [6,59],
                    "1,26" : [6,58],
                    "1,27" : [6,56],
                    "1,28" : [6,55],
                    "1,29" : [6,53],
                    "1,30" : [6,52],
                    "1,31" : [6,50],
                    "2,1" : [6,49],
                    "2,2" : [6,47],
                    "2,3" : [6,46],
                    "2,4" : [6,44],
                    "2,5" : [6,42],
                    "2,6" : [6,40],
                    "2,7" : [6,39],
                    "2,8" : [6,37],
                    "2,9" : [6,35],
                    "2,10" : [6,33],
                    "2,11" : [6,31],
                    "2,12" : [6,29],
                    "2,13" : [6,27],
                    "2,14" : [6,26],
                    "2,15" : [6,24],
                    "2,16" : [6,22],
                    "2,17" : [6,20],
                    "2,18" : [6,18],
                    "2,19" : [6,15],
                    "2,20" : [6,13],
                    "2,21" : [6,11],
                    "2,22" : [6,9],
                    "2,23" : [6,7],
                    "2,24" : [6,5],
                    "2,25" : [6,3],
                    "2,26" : [6,1],
                    "2,27" : [5,58],
                    "2,28" : [5,56],
                    "2,29" : [5,54],
                    "2,29" : [5,54],
                    "2,29" : [5,54],
                    "3,1" : [5,52],
                    "3,2" : [5,50],
                    "3,3" : [5,47],
                    "3,4" : [5,45],
                    "3,5" : [5,43],
                    "3,6" : [5,40],
                    "3,7" : [5,38],
                    "3,8" : [5,36],
                    "3,9" : [5,34],
                    "3,10" : [5,31],
                    "3,11" : [5,29],
                    "3,12" : [5,27],
                    "3,13" : [5,24],
                    "3,14" : [5,22],
                    "3,15" : [5,20],
                    "3,16" : [5,17],
                    "3,17" : [5,15],
                    "3,18" : [5,13],
                    "3,19" : [5,10],
                    "3,20" : [5,8],
                    "3,21" : [5,6],
                    "3,22" : [5,3],
                    "3,23" : [5,1],
                    "3,24" : [4,58],
                    "3,25" : [4,56],
                    "3,26" : [4,54],
                    "3,27" : [4,51],
                    "3,28" : [4,49],
                    "3,29" : [4,47],
                    "3,30" : [4,44],
                    "3,31" : [4,42],
                    "4,1" : [4,40],
                    "4,2" : [4,37],
                    "4,3" : [4,35],
                    "4,4" : [4,33],
                    "4,5" : [4,30],
                    "4,6" : [4,28],
                    "4,7" : [4,26],
                    "4,8" : [4,24],
                    "4,9" : [4,21],
                    "4,10" : [4,19],
                    "4,11" : [4,17],
                    "4,12" : [4,14],
                    "4,13" : [4,12],
                    "4,14" : [4,10],
                    "4,15" : [4,8],
                    "4,16" : [4,6],
                    "4,17" : [4,3],
                    "4,18" : [4,1],
                    "4,19" : [3,59],
                    "4,20" : [3,57],
                    "4,21" : [3,55],
                    "4,22" : [3,53],
                    "4,23" : [3,50],
                    "4,24" : [3,48],
                    "4,25" : [3,46],
                    "4,26" : [3,44],
                    "4,27" : [3,42],
                    "4,28" : [3,40],
                    "4,29" : [3,38],
                    "4,30" : [3,36],
                    "4,30" : [3,36],
                    "5,1" : [3,34],
                    "5,2" : [3,32],
                    "5,3" : [3,30],
                    "5,4" : [3,28],
                    "5,5" : [3,27],
                    "5,6" : [3,25],
                    "5,7" : [3,23],
                    "5,8" : [3,21],
                    "5,9" : [3,19],
                    "5,10" : [3,18],
                    "5,11" : [3,16],
                    "5,12" : [3,14],
                    "5,13" : [3,13],
                    "5,14" : [3,11],
                    "5,15" : [3,10],
                    "5,16" : [3,8],
                    "5,17" : [3,7],
                    "5,18" : [3,5],
                    "5,19" : [3,4],
                    "5,20" : [3,2],
                    "5,21" : [3,1],
                    "5,22" : [3,0],
                    "5,23" : [2,59],
                    "5,24" : [2,57],
                    "5,25" : [2,56],
                    "5,26" : [2,55],
                    "5,27" : [2,54],
                    "5,28" : [2,53],
                    "5,29" : [2,52],
                    "5,30" : [2,51],
                    "5,31" : [2,50],
                    "6,1" : [2,49],
                    "6,2" : [2,48],
                    "6,3" : [2,48],
                    "6,4" : [2,47],
                    "6,5" : [2,46],
                    "6,6" : [2,46],
                    "6,7" : [2,45],
                    "6,8" : [2,45],
                    "6,9" : [2,44],
                    "6,10" : [2,44],
                    "6,11" : [2,44],
                    "6,12" : [2,43],
                    "6,13" : [2,43],
                    "6,14" : [2,43],
                    "6,15" : [2,43],
                    "6,16" : [2,43],
                    "6,17" : [2,43],
                    "6,18" : [2,43],
                    "6,19" : [2,43],
                    "6,20" : [2,43],
                    "6,21" : [2,43],
                    "6,22" : [2,43],
                    "6,23" : [2,44],
                    "6,24" : [2,44],
                    "6,25" : [2,44],
                    "6,26" : [2,45],
                    "6,27" : [2,45],
                    "6,28" : [2,46],
                    "6,29" : [2,47],
                    "6,30" : [2,47],
                    "6,30" : [2,47],
                    "7,1" : [2,48],
                    "7,2" : [2,49],
                    "7,3" : [2,50],
                    "7,4" : [2,50],
                    "7,5" : [2,51],
                    "7,6" : [2,52],
                    "7,7" : [2,53],
                    "7,8" : [2,54],
                    "7,9" : [2,55],
                    "7,10" : [2,56],
                    "7,11" : [2,57],
                    "7,12" : [2,58],
                    "7,13" : [3,0],
                    "7,14" : [3,1],
                    "7,15" : [3,2],
                    "7,16" : [3,3],
                    "7,17" : [3,5],
                    "7,18" : [3,6],
                    "7,19" : [3,7],
                    "7,20" : [3,9],
                    "7,21" : [3,10],
                    "7,22" : [3,11],
                    "7,23" : [3,13],
                    "7,24" : [3,14],
                    "7,25" : [3,16],
                    "7,26" : [3,17],
                    "7,27" : [3,19],
                    "7,28" : [3,20],
                    "7,29" : [3,22],
                    "7,30" : [3,23],
                    "7,31" : [3,25],
                    "8,1" : [3,26],
                    "8,2" : [3,28],
                    "8,3" : [3,30],
                    "8,4" : [3,31],
                    "8,5" : [3,33],
                    "8,6" : [3,34],
                    "8,7" : [3,36],
                    "8,8" : [3,38],
                    "8,9" : [3,39],
                    "8,10" : [3,41],
                    "8,11" : [3,43],
                    "8,12" : [3,44],
                    "8,13" : [3,46],
                    "8,14" : [3,48],
                    "8,15" : [3,49],
                    "8,16" : [3,51],
                    "8,17" : [3,53],
                    "8,18" : [3,54],
                    "8,19" : [3,56],
                    "8,20" : [3,58],
                    "8,21" : [3,59],
                    "8,22" : [4,1],
                    "8,23" : [4,3],
                    "8,24" : [4,4],
                    "8,25" : [4,6],
                    "8,26" : [4,8],
                    "8,27" : [4,9],
                    "8,28" : [4,11],
                    "8,29" : [4,13],
                    "8,30" : [4,14],
                    "8,31" : [4,16],
                    "9,1" : [4,18],
                    "9,2" : [4,19],
                    "9,3" : [4,21],
                    "9,4" : [4,23],
                    "9,5" : [4,24],
                    "9,6" : [4,26],
                    "9,7" : [4,28],
                    "9,8" : [4,29],
                    "9,9" : [4,31],
                    "9,10" : [4,33],
                    "9,11" : [4,34],
                    "9,12" : [4,36],
                    "9,13" : [4,38],
                    "9,14" : [4,39],
                    "9,15" : [4,41],
                    "9,16" : [4,43],
                    "9,17" : [4,44],
                    "9,18" : [4,46],
                    "9,19" : [4,48],
                    "9,20" : [4,49],
                    "9,21" : [4,51],
                    "9,22" : [4,53],
                    "9,23" : [4,54],
                    "9,24" : [4,56],
                    "9,25" : [4,58],
                    "9,26" : [4,59],
                    "9,27" : [5,1],
                    "9,28" : [5,3],
                    "9,29" : [5,4],
                    "9,30" : [5,6],
                    "9,30" : [5,6],
                    "10,1" : [5,8],
                    "10,2" : [5,10],
                    "10,3" : [5,11],
                    "10,4" : [5,13],
                    "10,5" : [5,15],
                    "10,6" : [5,16],
                    "10,7" : [5,18],
                    "10,8" : [5,20],
                    "10,9" : [5,22],
                    "10,10" : [5,23],
                    "10,11" : [5,25],
                    "10,12" : [5,27],
                    "10,13" : [5,29],
                    "10,14" : [5,30],
                    "10,15" : [5,32],
                    "10,16" : [5,34],
                    "10,17" : [5,36],
                    "10,18" : [5,38],
                    "10,19" : [5,39],
                    "10,20" : [5,41],
                    "10,21" : [5,43],
                    "10,22" : [5,45],
                    "10,23" : [5,47],
                    "10,24" : [5,48],
                    "10,25" : [5,50],
                    "10,26" : [5,52],
                    "10,27" : [5,54],
                    "10,28" : [5,56],
                    "10,29" : [5,57],
                    "10,30" : [5,59],
                    "10,31" : [6,1],
                    "11,1" : [6,3],
                    "11,2" : [6,5],
                    "11,3" : [6,7],
                    "11,4" : [6,9],
                    "11,5" : [6,10],
                    "11,6" : [6,12],
                    "11,7" : [6,14],
                    "11,8" : [6,16],
                    "11,9" : [6,18],
                    "11,10" : [6,19],
                    "11,11" : [6,21],
                    "11,12" : [6,23],
                    "11,13" : [6,25],
                    "11,14" : [6,27],
                    "11,15" : [6,29],
                    "11,16" : [6,30],
                    "11,17" : [6,32],
                    "11,18" : [6,34],
                    "11,19" : [6,36],
                    "11,20" : [6,37],
                    "11,21" : [6,39],
                    "11,22" : [6,41],
                    "11,23" : [6,42],
                    "11,24" : [6,44],
                    "11,25" : [6,46],
                    "11,26" : [6,47],
                    "11,27" : [6,49],
                    "11,28" : [6,50],
                    "11,29" : [6,52],
                    "11,30" : [6,53],
                    "11,30" : [6,53],
                    "12,1" : [6,55],
                    "12,2" : [6,56],
                    "12,3" : [6,57],
                    "12,4" : [6,59],
                    "12,5" : [7,0],
                    "12,6" : [7,1],
                    "12,7" : [7,3],
                    "12,8" : [7,4],
                    "12,9" : [7,5],
                    "12,10" : [7,6],
                    "12,11" : [7,7],
                    "12,12" : [7,8],
                    "12,13" : [7,9],
                    "12,14" : [7,10],
                    "12,15" : [7,11],
                    "12,16" : [7,12],
                    "12,17" : [7,12],
                    "12,18" : [7,13],
                    "12,19" : [7,14],
                    "12,20" : [7,14],
                    "12,21" : [7,15],
                    "12,22" : [7,15],
                    "12,23" : [7,16],
                    "12,24" : [7,16],
                    "12,25" : [7,16],
                    "12,26" : [7,17],
                    "12,27" : [7,17],
                    "12,28" : [7,17],
                    "12,29" : [7,17],
                    "12,30" : [7,17],
                    "12,31" : [7,17], }

#keys = date, vaules = time( [0] = hour, [1] = minute )
sunsets =    {"1,1" : [15,1],
                        "1,2" : [15,3],
                        "1,3" : [15,4],
                        "1,4" : [15,5],
                        "1,5" : [15,6],
                        "1,6" : [15,7],
                        "1,7" : [15,9],
                        "1,8" : [15,10],
                        "1,9" : [15,11],
                        "1,10" : [15,13],
                        "1,11" : [15,14],
                        "1,12" : [15,16],
                        "1,13" : [15,17],
                        "1,14" : [15,19],
                        "1,15" : [15,20],
                        "1,16" : [15,22],
                        "1,17" : [15,24],
                        "1,18" : [15,25],
                        "1,19" : [15,27],
                        "1,20" : [15,29],
                        "1,21" : [15,30],
                        "1,22" : [15,32],
                        "1,23" : [15,34],
                        "1,24" : [15,36],
                        "1,25" : [15,38],
                        "1,26" : [15,39],
                        "1,27" : [15,41],
                        "1,28" : [15,43],
                        "1,29" : [15,45],
                        "1,30" : [15,47],
                        "1,31" : [15,49],
                        "2,1" : [15,51],
                        "2,2" : [15,52],
                        "2,3" : [15,54],
                        "2,4" : [15,56],
                        "2,5" : [15,58],
                        "2,6" : [16,0],
                        "2,7" : [16,2],
                        "2,8" : [16,4],
                        "2,9" : [16,6],
                        "2,10" : [16,8],
                        "2,11" : [16,10],
                        "2,12" : [16,11],
                        "2,13" : [16,13],
                        "2,14" : [16,15],
                        "2,15" : [16,17],
                        "2,16" : [16,19],
                        "2,17" : [16,21],
                        "2,18" : [16,23],
                        "2,19" : [16,25],
                        "2,20" : [16,27],
                        "2,21" : [16,29],
                        "2,22" : [16,30],
                        "2,23" : [16,32],
                        "2,24" : [16,34],
                        "2,25" : [16,36],
                        "2,26" : [16,38],
                        "2,27" : [16,40],
                        "2,28" : [16,42],
                        "2,29" : [16,43],
                        "2,29" : [16,43],
                        "2,29" : [16,43],
                        "3,1" : [16,45],
                        "3,2" : [16,47],
                        "3,3" : [16,49],
                        "3,4" : [16,51],
                        "3,5" : [16,53],
                        "3,6" : [16,54],
                        "3,7" : [16,56],
                        "3,8" : [16,58],
                        "3,9" : [17,0],
                        "3,10" : [17,2],
                        "3,11" : [17,3],
                        "3,12" : [17,5],
                        "3,13" : [17,7],
                        "3,14" : [17,9],
                        "3,15" : [17,11],
                        "3,16" : [17,12],
                        "3,17" : [17,14],
                        "3,18" : [17,16],
                        "3,19" : [17,18],
                        "3,20" : [17,19],
                        "3,21" : [17,21],
                        "3,22" : [17,23],
                        "3,23" : [17,25],
                        "3,24" : [17,26],
                        "3,25" : [17,28],
                        "3,26" : [17,30],
                        "3,27" : [17,32],
                        "3,28" : [17,33],
                        "3,29" : [17,35],
                        "3,30" : [17,37],
                        "3,31" : [17,39],
                        "4,1" : [17,40],
                        "4,2" : [17,42],
                        "4,3" : [17,44],
                        "4,4" : [17,46],
                        "4,5" : [17,47],
                        "4,6" : [17,49],
                        "4,7" : [17,51],
                        "4,8" : [17,53],
                        "4,9" : [17,54],
                        "4,10" : [17,56],
                        "4,11" : [17,58],
                        "4,12" : [18,0],
                        "4,13" : [18,1],
                        "4,14" : [18,3],
                        "4,15" : [18,5],
                        "4,16" : [18,7],
                        "4,17" : [18,8],
                        "4,18" : [18,10],
                        "4,19" : [18,12],
                        "4,20" : [18,14],
                        "4,21" : [18,15],
                        "4,22" : [18,17],
                        "4,23" : [18,19],
                        "4,24" : [18,21],
                        "4,25" : [18,22],
                        "4,26" : [18,24],
                        "4,27" : [18,26],
                        "4,28" : [18,28],
                        "4,29" : [18,29],
                        "4,30" : [18,31],
                        "4,30" : [18,31],
                        "5,1" : [18,33],
                        "5,2" : [18,34],
                        "5,3" : [18,36],
                        "5,4" : [18,38],
                        "5,5" : [18,39],
                        "5,6" : [18,41],
                        "5,7" : [18,43],
                        "5,8" : [18,44],
                        "5,9" : [18,46],
                        "5,10" : [18,48],
                        "5,11" : [18,49],
                        "5,12" : [18,51],
                        "5,13" : [18,53],
                        "5,14" : [18,54],
                        "5,15" : [18,56],
                        "5,16" : [18,57],
                        "5,17" : [18,59],
                        "5,18" : [19,0],
                        "5,19" : [19,2],
                        "5,20" : [19,3],
                        "5,21" : [19,5],
                        "5,22" : [19,6],
                        "5,23" : [19,8],
                        "5,24" : [19,9],
                        "5,25" : [19,10],
                        "5,26" : [19,12],
                        "5,27" : [19,13],
                        "5,28" : [19,14],
                        "5,29" : [19,15],
                        "5,30" : [19,17],
                        "5,31" : [19,18],
                        "6,1" : [19,19],
                        "6,2" : [19,20],
                        "6,3" : [19,21],
                        "6,4" : [19,22],
                        "6,5" : [19,23],
                        "6,6" : [19,24],
                        "6,7" : [19,25],
                        "6,8" : [19,26],
                        "6,9" : [19,27],
                        "6,10" : [19,27],
                        "6,11" : [19,28],
                        "6,12" : [19,29],
                        "6,13" : [19,29],
                        "6,14" : [19,30],
                        "6,15" : [19,30],
                        "6,16" : [19,31],
                        "6,17" : [19,31],
                        "6,18" : [19,32],
                        "6,19" : [19,32],
                        "6,20" : [19,32],
                        "6,21" : [19,32],
                        "6,22" : [19,32],
                        "6,23" : [19,33],
                        "6,24" : [19,33],
                        "6,25" : [19,33],
                        "6,26" : [19,32],
                        "6,27" : [19,32],
                        "6,28" : [19,32],
                        "6,29" : [19,32],
                        "6,30" : [19,32],
                        "6,30" : [19,32],
                        "7,1" : [19,31],
                        "7,2" : [19,31],
                        "7,3" : [19,30],
                        "7,4" : [19,30],
                        "7,5" : [19,29],
                        "7,6" : [19,29],
                        "7,7" : [19,28],
                        "7,8" : [19,27],
                        "7,9" : [19,27],
                        "7,10" : [19,26],
                        "7,11" : [19,25],
                        "7,12" : [19,24],
                        "7,13" : [19,23],
                        "7,14" : [19,22],
                        "7,15" : [19,21],
                        "7,16" : [19,20],
                        "7,17" : [19,19],
                        "7,18" : [19,18],
                        "7,19" : [19,16],
                        "7,20" : [19,15],
                        "7,21" : [19,14],
                        "7,22" : [19,12],
                        "7,23" : [19,11],
                        "7,24" : [19,9],
                        "7,25" : [19,8],
                        "7,26" : [19,7],
                        "7,27" : [19,5],
                        "7,28" : [19,3],
                        "7,29" : [19,2],
                        "7,30" : [19,0],
                        "7,31" : [18,58],
                        "8,1" : [18,57],
                        "8,2" : [18,55],
                        "8,3" : [18,53],
                        "8,4" : [18,51],
                        "8,5" : [18,50],
                        "8,6" : [18,48],
                        "8,7" : [18,46],
                        "8,8" : [18,44],
                        "8,9" : [18,42],
                        "8,10" : [18,40],
                        "8,11" : [18,38],
                        "8,12" : [18,36],
                        "8,13" : [18,34],
                        "8,14" : [18,32],
                        "8,15" : [18,30],
                        "8,16" : [18,28],
                        "8,17" : [18,26],
                        "8,18" : [18,24],
                        "8,19" : [18,22],
                        "8,20" : [18,20],
                        "8,21" : [18,17],
                        "8,22" : [18,15],
                        "8,23" : [18,13],
                        "8,24" : [18,11],
                        "8,25" : [18,9],
                        "8,26" : [18,6],
                        "8,27" : [18,4],
                        "8,28" : [18,2],
                        "8,29" : [18,0],
                        "8,30" : [17,57],
                        "8,31" : [17,55],
                        "9,1" : [17,53],
                        "9,2" : [17,50],
                        "9,3" : [17,48],
                        "9,4" : [17,46],
                        "9,5" : [17,43],
                        "9,6" : [17,41],
                        "9,7" : [17,39],
                        "9,8" : [17,36],
                        "9,9" : [17,34],
                        "9,10" : [17,32],
                        "9,11" : [17,29],
                        "9,12" : [17,27],
                        "9,13" : [17,25],
                        "9,14" : [17,22],
                        "9,15" : [17,20],
                        "9,16" : [17,17],
                        "9,17" : [17,15],
                        "9,18" : [17,13],
                        "9,19" : [17,10],
                        "9,20" : [17,8],
                        "9,21" : [17,6],
                        "9,22" : [17,3],
                        "9,23" : [17,1],
                        "9,24" : [16,58],
                        "9,25" : [16,56],
                        "9,26" : [16,54],
                        "9,27" : [16,51],
                        "9,28" : [16,49],
                        "9,29" : [16,47],
                        "9,30" : [16,44],
                        "9,30" : [16,44],
                        "10,1" : [16,42],
                        "10,2" : [16,40],
                        "10,3" : [16,37],
                        "10,4" : [16,35],
                        "10,5" : [16,33],
                        "10,6" : [16,30],
                        "10,7" : [16,28],
                        "10,8" : [16,26],
                        "10,9" : [16,23],
                        "10,10" : [16,21],
                        "10,11" : [16,19],
                        "10,12" : [16,17],
                        "10,13" : [16,14],
                        "10,14" : [16,12],
                        "10,15" : [16,10],
                        "10,16" : [16,8],
                        "10,17" : [16,6],
                        "10,18" : [16,3],
                        "10,19" : [16,1],
                        "10,20" : [15,59],
                        "10,21" : [15,57],
                        "10,22" : [15,55],
                        "10,23" : [15,53],
                        "10,24" : [15,51],
                        "10,25" : [15,49],
                        "10,26" : [15,47],
                        "10,27" : [15,45],
                        "10,28" : [15,43],
                        "10,29" : [15,41],
                        "10,30" : [15,39],
                        "10,31" : [15,37],
                        "11,1" : [15,35],
                        "11,2" : [15,33],
                        "11,3" : [15,31],
                        "11,4" : [15,30],
                        "11,5" : [15,28],
                        "11,6" : [15,26],
                        "11,7" : [15,24],
                        "11,8" : [15,23],
                        "11,9" : [15,21],
                        "11,10" : [15,19],
                        "11,11" : [15,18],
                        "11,12" : [15,16],
                        "11,13" : [15,15],
                        "11,14" : [15,13],
                        "11,15" : [15,12],
                        "11,16" : [15,10],
                        "11,17" : [15,9],
                        "11,18" : [15,8],
                        "11,19" : [15,7],
                        "11,20" : [15,5],
                        "11,21" : [15,4],
                        "11,22" : [15,3],
                        "11,23" : [15,2],
                        "11,24" : [15,1],
                        "11,25" : [15,0],
                        "11,26" : [14,59],
                        "11,27" : [14,58],
                        "11,28" : [14,57],
                        "11,29" : [14,56],
                        "11,30" : [14,56],
                        "11,30" : [14,56],
                        "12,1" : [14,55],
                        "12,2" : [14,54],
                        "12,3" : [14,54],
                        "12,4" : [14,53],
                        "12,5" : [14,53],
                        "12,6" : [14,52],
                        "12,7" : [14,52],
                        "12,8" : [14,52],
                        "12,9" : [14,52],
                        "12,10" : [14,51],
                        "12,11" : [14,51],
                        "12,12" : [14,51],
                        "12,13" : [14,51],
                        "12,14" : [14,51],
                        "12,15" : [14,51],
                        "12,16" : [14,52],
                        "12,17" : [14,52],
                        "12,18" : [14,52],
                        "12,19" : [14,52],
                        "12,20" : [14,53],
                        "12,21" : [14,53],
                        "12,22" : [14,54],
                        "12,23" : [14,55],
                        "12,24" : [14,55],
                        "12,25" : [14,56],
                        "12,26" : [14,57],
                        "12,27" : [14,57],
                        "12,28" : [14,58],
                        "12,29" : [14,59],
                        "12,30" : [15,0],
                        "12,31" : [15,1], }

while 1:

    #getting information out of the RTC
    month = int(str(datum.datetime()).replace(("("), "").replace(")","").split(",")[1])
    day   = int(str(datum.datetime()).replace(("("), "").replace(")","").split(",")[2])

    hour = int(str(datum.datetime()).replace(("("), "").replace(")","").split(",")[4])
    minute = int(str(datum.datetime()).replace(("("), "").replace(")","").split(",")[5])

    #getting values out of the lists
    sonnen_aufgang   = sunrises.get("%s,%s" % (month,day))
    sonnen_untergang = sunsets.get("%s,%s" % (month,day))

    #checking the time

    #if time = sunrise ----> open door
    if [hour, minute] == sonnen_aufgang:
        pin_1.high()
        pin_2.high()
        time.sleep(35)
        pin_1.low()
        pin_2.low()

    #subtrac 30 min from time to get a buffer for the chickens to go in
    minute -= 30
    if minute < 0:
        hour -= 1
        minute = 60 - int((minute**2)**0.5)

    #if time = sunset -----> close door
    elif [hour, minute-15] == sonnen_untergang:
        pin_3.high()
        pin_4.high()
        time.sleep(35)
        pin_3.low()
        pin_4.low()

    #less than 1 min too protct for skiping 1min (run time code)
    time.sleep(59)