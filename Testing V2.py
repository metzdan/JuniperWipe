import serial
import time
import sys

sys.setrecursionlimit(2000)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


SERIAL_PORT = "COM27"
SERIAL_RATE = 9600
MAP = "Testing..."
timestr = time.strftime("%Y-%m-%d")
ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)
filef = "Hub-Test_Failed_"
files = "Hub-Test_Results_"
reading = ser.readline().decode('utf-8', errors = 'ignore').strip()
x=1
timestr = time.strftime("%Y-%m-%d")
timelog = time.strftime("%Y-%m-%d-%H:%M")

def reading_ser():
    global reading
    reading = ser.readline().decode('utf-8', errors = 'ignore').strip()
    time.sleep(0.2)
    print(x, MAP, ": ", reading, flush=True)

def model_detection():
    global x
    global reading
    while(x==1):
        time.sleep(0.2)
        reading = ser.readline().decode('utf-8', errors = 'ignore').strip()
        print(x,MAP,f"{bcolors.WARNING} No model Detected{bcolors.ENDC}", reading)
        if "EX2200" in reading:
            x=10
            print(MAP + f"{bcolors.OKCYAN} Detecting EX2200{bcolors.ENDC}", flush=True)
            
        if "SRX_210" in reading:
            x=20
            print(MAP, f"{bcolors.OKCYAN} Detecting SRX210{bcolors.ENDC}", flush=True)
            
        if "SRX_320" in reading:
            x=30
            print(MAP, f"{bcolors.OKCYAN} Detecting SRX320{bcolors.ENDC}", flush=True)
            
        if "EX2300-48P" in reading:
            x=40
            print(MAP, f"{bcolors.OKCYAN} Detecting EX2300{bcolors.ENDC}", flush=True)
        if "00000000" in reading:
            x=200
            


#Models
def EX2200(): #Working
    global x
    global reading
    while True:
        reading_ser()
        if(x==10):
            boot_1()
        if(x==11):
            boot_2()
        if(x==12):
            boot_3()
        if(x==13):
            boot_4()

def SRX_210():
    global x
    global reading
    while True:
        reading_ser()
        if(x==20):
            boot_1()
        if(x==21):
            boot_2()
        if(x==22):
            boot_3()
        if(x==23):
            boot_4()

def SRX_320():
    global x
    global reading
    while True:
        reading_ser()
        if(x==30):
            boot_1()
        if(x==31):
            boot_2()
        if(x==32):
            boot_3()
        if(x==33):
            boot_4()

def EX2300(): # Working
    global x
    global reading
    while True:
        reading_ser()
        if(x==40):
            boot_2_1()
        if(x==41):
            boot_2_2()
        if(x==42):
            boot_4()
#Factory Reset EX2300
def boot_2_1():
        global x
        ser.write(b'\x03')
        if "Main Menu" in reading:
            x=(x+1)

def boot_2_2():
    global x
    if "Main Menu" in reading:
        time.sleep(10)
        ser.write("5".encode())
        time.sleep(2)
        ser.write("2".encode())
        x=(x+1)
#Factory reset others
def boot_1():
    global x
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
    if "Type '?'" in reading:
        ser.write("boot -s\r\n".encode())
        print(MAP, f"{bcolors.OKCYAN}Booting in Single-user mode{bcolors.ENDC}", flush=True)
        x=(x+1)

def boot_3():
    global x
    if "System watchdog timer disabled" in reading:
        time.sleep(0.5)
        ser.write('recovery\r\n'.encode())
        print(MAP, f"{bcolors.OKBLUE}Entering Recovery Mode...{bcolors.ENDC}")
        x=(x+1)

def boot_4():
    global x
    if "linecard:0" in reading:
        time.sleep(5)
        print(MAP, f"{bcolors.OKBLUE}Requesting System Zeroize{bcolors.ENDC}", flush=True)
        ser.write("request system zeroize\r".encode())
        time.sleep(2)
        ser.write("yes\r".encode())
        time.sleep(15)
        with open (files+timestr+".txt", "a") as file:
            print(MAP+"zeroized", file=file)
        x=100
    if "Starting CLI" in reading:
        time.sleep(10)
        print(MAP, f"{bcolors.OKBLUE}Requesting System Zeroize{bcolors.ENDC}", flush=True)
        ser.write("request system zeroize\r".encode())
        time.sleep(2)
        ser.write("yes\r".encode())
        time.sleep(15)
        with open (files+timestr+".txt", "a") as file:
            print(MAP+"zeroized", file=file)
        x=100
    if "error: filesystem consistency checks" in reading:
        print(MAP, f"{bcolors.WARNING} Startup Error...Rebooting...{bcolors.ENDC}", flush=True)
        ser.write("reboot\r\n".encode())
        time.sleep(1)
        ser.write("yes\r\n".encode())
        x=200
        
#Verify Erasure
def verify_erasure():
    global x
    global reading
    while True:
        reading_ser()
        if x==100:    
            verify_1()
        if x==101:
            verify_2()
        if x==102:
            verify_3()

def verify_1():
    global x
    if "chassis_init_hw_chassis_startup_time:" in reading:
        print("I see this")
        print(reading, flush=True)
        ser.write("\r".encode())
        x=(x+1)
    if "FreeBSD/arm" or "Amnesiac" in reading:
        print("I see FreeBSD/amnesiac")
        x=(x+1)
    if "Starting of initial processes complete" in reading:
        print("I see that!")
        x=(x+1)

def verify_2():
    global x
    if "login:" in reading:
        print(MAP, "Trying Root Account...", flush=True)
        ser.write("root\r".encode())
        time.sleep(5)

def verify_3():
    global x
    if "root@%" or "root@:RE:" in reading:
        with open (files+timestr+".txt", "a") as file:
            print(MAP+" cleared password", file=file)
        print(MAP + f"{bcolors.OKGREEN}Erasure Verified!!!{bcolors.ENDC}")
        x = (x+1)
    if "Password" in reading:
        with open (filef+timestr+".txt", "a") as file:
            print(MAP+" has Password", file=file)
        print(MAP, f"{bcolors.FAIL}Not Erased, please restart{bcolors.ENDC}", "and this program.", flush=True)
        x=200
#Main
def main():
    global x
    global reading
    with open (filef+timestr+".txt", "a") as file:
        print("==================NEW BATCH==================", file=file)
        print(timelog, file=file)
        print(f"{bcolors.HEADER}Log file created {bcolors.ENDC}" + timestr)
    with open (files+timestr+".txt", "a") as file:
        print("==================NEW BATCH==================", file=file)
        print(timelog, file=file)
        print(f"{bcolors.HEADER}Log file created {bcolors.ENDC}" + timestr)

    while True:
        if(x==1):
            model_detection()
        while(10<=x<=19):
            EX2200()
        if(20<=x<=29):
            SRX_210()
        if(30<=x<=39):
            SRX_320()
        if(40<=x<=49):
            EX2300()
        if(100<=x<=199):
            verify_erasure()
        if(x==200):
            print(MAP, "error")
            with open (filef+timestr+".txt", "a") as file:
                print(MAP+"Unexpected Error", file=file)
            break

if __name__ == "__main__":
    main()    