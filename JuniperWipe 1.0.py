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


SERIAL_PORT = "COM35"
SERIAL_RATE = 9600
MAP = "H3-P01"

timestr = time.strftime("%Y-%m-%d")
ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)
filef = "Hub-03_Failed_"
files = "Hub-03_Results_"
    

def model_detection():
    global reading 
    global model
    #global stage
    #stage = "model_detection"
    reading = ser.readline().decode('utf-8', errors = 'ignore').strip()
    time.sleep(0.2)
    print(MAP,"No Model Detected... You may need to restart This Switch!", reading, flush=True)
    if "EX2200" in reading:
        model = "EX2200"
        print(MAP + f"{bcolors.OKCYAN} Detecting EX2200{bcolors.ENDC}", flush=True)
        EX2200()
    else:
        if "SRX_210" in reading:
            model = "SRX210"
            print(MAP, f"{bcolors.OKCYAN} Detecting SRX210{bcolors.ENDC}", flush=True)
            SRX210()
        else:
             if "SRX_320" in reading:
                model = "SRX320"
                print(MAP, f"{bcolors.OKCYAN} Detecting SRX320{bcolors.ENDC}")
                SRX320()

def reading_serial():
    global reading
    global model
    reading = ser.readline().decode('utf-8', errors = 'ignore').strip()
    time.sleep(0.2)
    #print(MAP, model,": ", reading, flush=True)
    error_correct()

def reading_serial_verify():
     global reading
     global model
     reading = ser.readline().decode('utf-8', errors = 'ignore').strip()
     time.sleep(1)
     print(MAP, "Verifying: ", reading, flush=True)

def reading_serial_flush():
    global reading
    global model
    reading = ser.readline().decode('utf-8', errors = 'ignore').strip()
    time.sleep(10)
    ser.write("\r".encode())
    print (MAP, "Flushing: ", reading, flush=True)

def boot_1():
    global reading
    if "Hit" in reading:
        ser.write(' '.encode())
        time.sleep(0.3)
        ser.write(' '.encode())
        ser.write(' '.encode())
        time.sleep(0.3)
        ser.write(' '.encode())
        print(MAP, f"{bcolors.OKCYAN}Tapping Spacebar{bcolors.ENDC}")
        ser.write(' '.encode())
        time.sleep(0.3)
        ser.write(' '.encode())
        ser.write(' '.encode())
        time.sleep(0.3)
        ser.write(' '.encode())
def boot_2():
    global reading
    if "Type '?'" in reading:
        ser.write("boot -s\r\n".encode())
        print(MAP, f"{bcolors.OKCYAN}Booting in Single-user mode{bcolors.ENDC}", flush=True)
def boot_3():
    global reading
    if "System watchdog timer disabled" in reading:
        time.sleep(0.5)
        ser.write('recovery\r\n'.encode())
        print(MAP, f"{bcolors.OKBLUE}Entering Recovery Mode...{bcolors.ENDC}")

def zero():
    global reading
    if "linecard:0" in reading:
        time.sleep(5)
        print(MAP, f"{bcolors.OKBLUE}Requesting System Zeroize{bcolors.ENDC}", flush=True)
        ser.write("request system zeroize\r".encode())
        time.sleep(2)
        ser.write("yes\r".encode())
        print(MAP, "EX2200 Zeroizing on ",MAP, flush=True)
        verify_erasure()
    else:
        if "Starting CLI ..." in reading:
            time.sleep(2)
            ser.write("request system zeroize\r".encode())
            time.sleep(2)
            ser.write("yes\r".encode())
            print("Zeroizing on ", MAP, flush=True)
            verify_erasure()
        else:
            factory_reset()

def amnesiac():
    global reading
    if "Amnesiac" in reading:
        print(MAP, "Looking for login...", flush=True)
        ser.write("\r\n".encode())
        time.sleep(5)

def final():
    global reading
    if "login:" in reading:
        print(MAP, "Trying Root Account...", flush=True)
        ser.write("root\r\n".encode())
        time.sleep(5)

def root():
    global reading
    if "root@%" in reading:
        with open(files+timestr+".txt", "a") as f:
            print(MAP, " Erasure Verified!")
        print(MAP + f"{bcolors.OKGREEN}Erasure Verified!!!{bcolors.ENDC}")
    else:
        if "root@:RE:" in reading:
            print(MAP + f"{bcolors.OKGREEN}Erasure Verified!!!{bcolors.ENDC}")
            with open(files+timestr+".txt", "a") as f:
                    print(MAP, " Erasure Verified!")
        else:
            if "Password" in reading:
                with open(filef+timestr+".txt", "a") as f:
                    print(MAP, " has password, retry erasure")
                print(MAP, f"{bcolors.FAIL}Not Erased, please restart{bcolors.ENDC}", model, "and this program.", flush=True)
            else:
                time.sleep(5)
                verify_erasure()

def error_correct():
    global reading
    if "error: filesystem consistency checks" in reading:
        print(MAP, f"{bcolors.WARNING} Startup Error...Rebooting...{bcolors.ENDC}", flush=True)
        ser.write("reboot\r\n".encode())
        time.sleep(1)
        ser.write("yes\r\n".encode())
        flush()

def flush():
        with open (filef+timestr+".txt", "a") as f:
            print(MAP+" is restarting...Standby for restart notice...", file = f)
        while True:
             reading_serial_flush()
             if "Access to this equipment and associated network, resources " in reading:
                print(MAP + " is ready for restart...")
                with open (filef+timestr+".txt", "a") as f:
                    print(MAP+" is ready for restart", file = f)
                break
             

                
def factory_reset():
        while True:
            reading_serial()
            boot_1()
            boot_2()
            boot_3()
            zero()
            
def verify_erasure():
        while True:
            reading_serial_verify()
            amnesiac()
            final()
            root()
            
def EX2200():
        print(MAP, f"{bcolors.OKGREEN}Now using EX2200 Profile{bcolors.ENDC}", flush=True)
        model = "EX2200"
        while True:
            reading_serial()
            factory_reset()
            verify_erasure()
            print(MAP, " Verified Factory Reset", flush=True)
            with open (files+timestr+".txt", "a") as f:
                print(MAP+"Erased", file = f)
            

def SRX210():
        print(MAP, f"{bcolors.OKGREEN} Now Using SRX210 Profile{bcolors.ENDC}", flush=True)
        model = "SRX210"
        while True:
          reading_serial()
          factory_reset()
          verify_erasure()
          print(MAP, f"{bcolors.OKGREEN} Verified Factory Reset{bcolors.ENDC}", flush=True)
          with open (files+timestr+".txt", "a") as f:
            print(MAP+"Erased", file = f)


def SRX320():
     print(MAP, f"{bcolors.OKGREEN} Now using SRX320 Profile{bcolors.ENDC}", flush=True)
     model = "SRX320"
     while True:
          reading_serial()
          factory_reset()
          verify_erasure()
          print(MAP, f"{bcolors.OKGREEN} Verified Factory Reset{bcolors.ENDC}", flush=True)
          with open (files+timestr+".txt", "a") as f:
            print(MAP+"Erased", file = f)

def main():
        print(f"{bcolors.HEADER}Script Started on {bcolors.ENDC}", MAP)
        while True:
            model_detection()
            
            
            
if __name__ == "__main__":
    main()
