import serial
import time
import sys

sys.setrecursionlimit(2000)



SERIAL_PORT = "COM9"
SERIAL_RATE = 9600
MAP = "H1-P08"
timestr = time.strftime("%Y-%m-%d")
ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)
filef = "Hub-01_Failed"
files = "Hub-01_Results"
reading = ser.readline().decode('utf-8', errors = 'ignore').strip()
x=1
hwserial = " UnKnown"
stat = "Starting H1P08"

def send_status():
    with open("H1P08Status.txt", "w") as file:
        print(stat, file=file)
        


#Version 3.1
def reading_ser():
    global reading
    reading = ser.readline().decode('utf-8', errors = 'ignore').strip()
    time.sleep(0.2)
    #print(x, MAP, ": ", reading, flush=True)

def model_detection():
    global x
    global reading
    global stat
    while(x==1):
        stat = "Detecting Model..."
        send_status()
        time.sleep(0.2)
        reading = ser.readline().decode('utf-8', errors = 'ignore').strip()
        #print(x,MAP,f"{bcolors.WARNING} No model Detected{bcolors.ENDC}", reading)
        if "EX2200" in reading:
            x=10
            stat = "Detected EX2200..."
#            print(MAP + f"{bcolors.OKCYAN} Detecting EX2200{bcolors.ENDC}", flush=True)    
        if "SRX_210" in reading:
            x=20
            stat = "Detected SRX210..."
#            print(MAP, f"{bcolors.OKCYAN} Detecting SRX210{bcolors.ENDC}", flush=True)
        if "SRX_320" in reading:
            x=30
            stat = "Detected SRX320..."
#            print(MAP, f"{bcolors.OKCYAN} Detecting SRX320{bcolors.ENDC}", flush=True)    
        if "EX2300-48P" in reading:
            x=40
            stat = "Detected EX2300..."
#            print(MAP, f"{bcolors.OKCYAN} Detecting EX2300{bcolors.ENDC}", flush=True)
        if "0000000000000000000000" in reading:
            x=200
            stat = "Startup Errors..."
    send_status()
            


#Models
def EX2200(): #Working Serial
    global x
    global reading
    global stat
    while(10<=x<=19):
        reading_ser()
        if(x==10):
            boot_1()
        if(x==11):
            boot_2()
        if(x==12):
            boot_3()
        if(x==13):
            boot_4()
        if(x==14):
            boot_5()
        else:
            main()


def SRX_210():
    global x
    global reading
    while(20<=x<=29):
        reading_ser()
        if(x==20):
            boot_1()
        if(x==21):
            boot_2()
        if(x==22):
            boot_3()
        if(x==23):
            boot_4()
        if(x==24):
            boot_5()
        else:
            main()



def SRX_320():
    global x
    global reading
    while(30<=x<=39):
        reading_ser()
        if(x==30):
            boot_1()
        if(x==31):
            boot_2()
        if(x==32):
            boot_3()
        if(x==33):
            boot_4()
        if(x==34):
            boot_5()
        else:
            main()

def EX2300(): # Working
    global x
    global reading
    while(40<=x<=49):
        reading_ser()
        if(x==40):
            boot_2_1()
        if(x==41):
            boot_2_2()
        if(x==42):
            boot_4()
        if(x==43):
            boot_5()
        else:
            main()

#Factory Reset EX2300
def boot_2_1():
        global x
        global stat
        stat = "Navigating Main Menu..."
        send_status()
        ser.write(b'\x03')
        if "Main Menu" in reading:
            x=(x+1)

def boot_2_2():
    global x
    global stat
    stat = "Selecting Factory Reset..."
    send_status()
    if "Main Menu" in reading:
        time.sleep(10)
        ser.write("5".encode())
        time.sleep(2)
        ser.write("2".encode())
        x=(x+1)
#Factory reset others
def boot_1():
    global x
    global stat
    stat = "Breaking Startup..."
    send_status()
    if "Hit" in reading:
        ser.write(' '.encode())
        time.sleep(0.3)
        ser.write(' '.encode())
        ser.write(' '.encode())
        time.sleep(0.3)
        ser.write(' '.encode())
        ser.write(' '.encode())
        time.sleep(0.3)
        ser.write(' '.encode())
        ser.write(' '.encode())
        time.sleep(0.3)
        ser.write(' '.encode())
        x=(x+1)

def boot_2():
    global x
    global stat
    stat = "Booting to Single-User Mode"
    send_status()
    if "Type '?'" in reading:
        ser.write("boot -s\r\n".encode())
#        print(MAP, f"{bcolors.OKCYAN}Booting in Single-user mode{bcolors.ENDC}", flush=True)
        x=(x+1)

def boot_3():
    global x
    global stat
    stat = "Entering Recovery Mode..."
    send_status()
    if "System watchdog timer disabled" in reading:
        time.sleep(0.5)
        ser.write('recovery\r\n'.encode())
#        print(MAP, f"{bcolors.OKBLUE}Entering Recovery Mode...{bcolors.ENDC}")
        x=(x+1)


def boot_4(): #Grab Serial Numbers
    global x
    global stat
    stat = "Waiting for next stage..."
    send_status()
    if "linecard:0" in reading:
        time.sleep(5)
        x=(x+1)
    if "Starting CLI" in reading:
        time.sleep(5)
        x=(x+1)
    if "error: filesystem consistency checks" in reading:
#        print(MAP, f"{bcolors.WARNING} Startup Error...Rebooting...{bcolors.ENDC}", flush=True)
        with open (filef+".txt", "a") as file:
            print(MAP+" has errors", file=file)
        ser.write("reboot\r\n".encode())
        time.sleep(1)
        ser.write("yes\r\n".encode())
        x=200
        stat = "Startup Error...Rebooting..."






def boot_5():
    global x
    global stat
    stat = "Requesting System Zeroize"
    send_status()
    if "linecard:0" in reading:
        time.sleep(3)
#        print(MAP, f"{bcolors.OKBLUE}Requesting System Zeroize{bcolors.ENDC}", flush=True)
        time.sleep(2)
        ser.write("request system zeroize\r".encode())
        time.sleep(2)
        ser.write("yes\r".encode())
        time.sleep(10)
        x=100
        main()
    if "Starting CLI" in reading:
        time.sleep(3)
#        print(MAP, f"{bcolors.OKBLUE}Requesting System Zeroize{bcolors.ENDC}", flush=True)
        time.sleep(2)
        ser.write("request system zeroize\r".encode())
        time.sleep(2)
        ser.write("yes\r".encode())
        time.sleep(10)
        x=100
        main()
    if "error: filesystem consistency checks" in reading:
#        print(MAP, f"{bcolors.WARNING} Startup Error...Rebooting...{bcolors.ENDC}", flush=True)
        with open (filef+".txt", "a") as file:
            print(MAP+" has errors", file=file)
        ser.write("reboot\r\n".encode())
        time.sleep(1)
        ser.write("yes\r\n".encode())
        stat = "Startup Error...Rebooting..."
        send_status()
        x=200
    



def verify_1():
    global x
    global reading
    while(x==100):
        reading_ser()
        time.sleep(1)
        if "Amnesiac" in reading:
            #print("I see this", flush=True)
            time.sleep(1)
            ser.write("root\r\n".encode())
            time.sleep(10)
            x=(x+1)
        else:
            verify_1()
        


def verify_2():
    global x
    global reading
    while(x==101):
        reading_ser()
        if "root" in reading:
#            print(MAP + f"{bcolors.OKGREEN} No Password!{bcolors.ENDC}")
            x=(x+1)
        if "Password" in reading:
            with open (filef+".txt", "a") as file:
                print(MAP+" has Password", file=file)
#            print(MAP, f"{bcolors.FAIL} Not Erased, please restart{bcolors.ENDC}", "and this program.", flush=True)
            x=200

def verify_3():
    global x
    global reading
    while(x==102):
        time.sleep(10)
        reading_ser()
        ser.write("\r\n".encode())
        time.sleep(5)
        ser.write("cli\r\n".encode())
        time.sleep(1)
        if "root" in reading:
            x=(x+1)
        
def verify_4():
    global x
    global reading
    global hwserial
    while(x==103):
        reading_ser()
        ser.write("show chassis hardware\r".encode())
        time.sleep(1)
        if "Chassis" in reading:
            time.sleep(5)
            hwserial=(reading)
            print(hwserial)
            x=(x+1)

def verify_5():
    global x
    global hwserial
    global stat
    #print(MAP, " is erased and SN obtained:"+hwserial)
    with open(files+".txt", "a") as file:
        print(MAP+" sanitized. SN = "+hwserial, file=file)
    stat = MAP+" sanitized. SN = "+hwserial
    send_status()
    x=0
    


def verify_erasure():
    global x
    global reading
    global stat
    stat = "Switching to Verify Mode..."
    send_status()
    while(100<=x<=104):
        reading_ser()
        if(x==100):
            stat = "Checking Erasure Status..."
            send_status()
            verify_1()
        if(x==101):
            stat = "Logging in..."
            send_status()
            verify_2()
        if(x==102):
            stat = "Entering CLI..."
            send_status()
            verify_3()
        if(x==103):
            stat = "Grabbing Serial..."
            send_status()
            verify_4()
        if(x==104):
            stat = "Loading Results..."
            send_status()
            verify_5()
        else:
            main()

#Main
def main():
    global x
    global reading
    global stat
    while(0<x):
        if(x==1):
            model_detection()
        while(10<=x<=19):
            EX2200()
        while(20<=x<=29):
            SRX_210()
        while(30<=x<=39):
            SRX_320()
        while(40<=x<=49):
            EX2300()
        while(100<=x<=199):
            verify_erasure()
        if(x==200):
            print(MAP, "error")
            #with open (filef+".txt", "a") as file:
            #    print(MAP+"Unexpected Error", file=file)
            stat = "Error...Script Ending..."
            break

if __name__ == "__main__":
    main()    