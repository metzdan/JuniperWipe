from tkinter import *
from tkinter import ttk
import subprocess
import threading
import time




def update_GUI01():
        global h1p1status
        global h1p2status
        global h1p3status
        global h1p4status
        global h1p5status
        global h1p6status
        global h1p7status
        global h1p8status
        global h1p9status
        global h1p10status
        global h1p11status
        global h1p12status
        global h1p13status
        global h1p14status
        global h1p15status
        global h1p16status


        root.after(50000, update_GUI01)

        with open("H1P01Status.txt", 'r') as file:
            h1p1status = file.readline()
        h1p1l.config(text=h1p1status)
        time.sleep(.1)


        with open("H1P02Status.txt", 'r') as file:
            h1p2status = file.readline()
        h1p2l.config(text=h1p2status)
        time.sleep(.1)


        with open("H1P03Status.txt", 'r') as file:
            h1p3status = file.readline()
        h1p3l.config(text=h1p3status)
        time.sleep(.1)


        with open("H1P04Status.txt", 'r') as file:
            h1p4status = file.readline()
        h1p4l.config(text=h1p4status)
        time.sleep(.1)


        with open("H1P05Status.txt", 'r') as file:
            h1p5status = file.readline()
        h1p5l.config(text=h1p5status)
        time.sleep(.1)


        with open("H1P06Status.txt", 'r') as file:
            h1p6status = file.readline()
        h1p6l.config(text=h1p6status)
        time.sleep(.1)


        with open("H1P07Status.txt", 'r') as file:
            h1p7status = file.readline()
        h1p7l.config(text=h1p7status)
        time.sleep(.1)

        with open("H1P08Status.txt", 'r') as file:
            h1p8status = file.readline()
        h1p8l.config(text=h1p8status)
        time.sleep(.1)


        with open("H1P09Status.txt", 'r') as file:
            h1p9status = file.readline()
        h1p9l.config(text=h1p9status)
        time.sleep(.1)

        with open("H1P10Status.txt", 'r') as file:
            h1p10status = file.readline()
        h1p10l.config(text=h1p10status)
        time.sleep(.1)


        with open("H1P11Status.txt", 'r') as file:
            h1p11status = file.readline()
        h1p11l.config(text=h1p11status)
        time.sleep(.1)


        with open("H1P12Status.txt", 'r') as file:
            h1p12status = file.readline()
        h1p12l.config(text=h1p12status)
        time.sleep(.1) 


        with open("H1P13Status.txt", 'r') as file:
            h1p13status = file.readline()
        h1p13l.config(text=h1p13status)
        time.sleep(.1)


        with open("H1P14Status.txt", 'r') as file:
            h1p14status = file.readline()
        h1p14l.config(text=h1p14status)
        time.sleep(.1) 


        with open("H1P15Status.txt", 'r') as file:
            h1p15status = file.readline()
        h1p15l.config(text=h1p15status)
        time.sleep(.1) 
        

        with open("H1P16Status.txt", 'r') as file:
            h1p16status = file.readline()
        h1p16l.config(text=h1p16status)
        time.sleep(.1) 


def update_GUI02():
        global h2p1status
        global h2p2status
        global h2p3status
        global h2p4status
        global h2p5status
        global h2p6status
        global h2p7status
        global h2p8status
        global h2p9status
        global h2p10status
        global h2p11status
        global h2p12status
        global h2p13status
        global h2p14status
        global h2p15status
        global h2p16status

        root.after(50000, update_GUI02)

        with open("H2P01Status.txt", 'r') as file:
            h2p1status = file.readline()
        h2p1l.config(text=h2p1status)
        time.sleep(.1)


        with open("H2P02Status.txt", 'r') as file:
            h2p2status = file.readline()
        h2p2l.config(text=h2p2status)
        time.sleep(.1)


        with open("H2P03Status.txt", 'r') as file:
            h2p3status = file.readline()
        h2p3l.config(text=h2p3status)
        time.sleep(.1)


        with open("H2P04Status.txt", 'r') as file:
            h2p4status = file.readline()
        h2p4l.config(text=h2p4status)
        time.sleep(.1)


        with open("H2P05Status.txt", 'r') as file:
            h2p5status = file.readline()
        h2p5l.config(text=h2p5status)
        time.sleep(.1)


        with open("H2P06Status.txt", 'r') as file:
            h2p6status = file.readline()
        h2p6l.config(text=h2p6status)
        time.sleep(.1)


        with open("H2P07Status.txt", 'r') as file:
            h2p7status = file.readline()
        h2p7l.config(text=h2p7status)
        time.sleep(.1)

        with open("H2P08Status.txt", 'r') as file:
            h2p8status = file.readline()
        h2p8l.config(text=h2p8status)
        time.sleep(.1)


        with open("H2P09Status.txt", 'r') as file:
            h2p9status = file.readline()
        h2p9l.config(text=h2p9status)
        time.sleep(.1)

        with open("H2P10Status.txt", 'r') as file:
            h2p10status = file.readline()
        h2p10l.config(text=h2p10status)
        time.sleep(.1)


        with open("H2P11Status.txt", 'r') as file:
            h2p11status = file.readline()
        h2p11l.config(text=h2p11status)
        time.sleep(.1)


        with open("H2P12Status.txt", 'r') as file:
            h2p12status = file.readline()
        h2p12l.config(text=h2p12status)
        time.sleep(.1) 


        with open("H2P13Status.txt", 'r') as file:
            h2p13status = file.readline()
        h2p13l.config(text=h2p13status)
        time.sleep(.1)


        with open("H2P14Status.txt", 'r') as file:
            h2p14status = file.readline()
        h2p14l.config(text=h2p14status)
        time.sleep(.1) 


        with open("H2P15Status.txt", 'r') as file:
            h2p15status = file.readline()
        h2p15l.config(text=h2p15status)
        time.sleep(.1) 
        

        with open("H2P16Status.txt", 'r') as file:
            h2p16status = file.readline()
        h2p16l.config(text=h2p16status)
        time.sleep(.1)

def update_GUI03():
        global h3p1status
        global h3p2status
        global h3p3status
        global h3p4status
        global h3p5status
        global h3p6status
        global h3p7status
        global h3p8status
        global h3p9status
        global h3p10status
        global h3p11status
        global h3p12status
        global h3p13status
        global h3p14status
        global h3p15status
        global h3p16status

        root.after(50000, update_GUI03)

        with open("H3P01Status.txt", 'r') as file:
            h3p1status = file.readline()
        h3p1l.config(text=h3p1status)
        time.sleep(.1)


        with open("H3P02Status.txt", 'r') as file:
            h3p2status = file.readline()
        h3p2l.config(text=h3p2status)
        time.sleep(.1)


        with open("H3P03Status.txt", 'r') as file:
            h3p3status = file.readline()
        h3p3l.config(text=h3p3status)
        time.sleep(.1)


        with open("H3P04Status.txt", 'r') as file:
            h3p4status = file.readline()
        h3p4l.config(text=h3p4status)
        time.sleep(.1)


        with open("H3P05Status.txt", 'r') as file:
            h3p5status = file.readline()
        h3p5l.config(text=h3p5status)
        time.sleep(.1)


        with open("H3P06Status.txt", 'r') as file:
            h3p6status = file.readline()
        h3p6l.config(text=h3p6status)
        time.sleep(.1)


        with open("H3P07Status.txt", 'r') as file:
            h3p7status = file.readline()
        h3p7l.config(text=h3p7status)
        time.sleep(.1)

        with open("H3P08Status.txt", 'r') as file:
            h3p8status = file.readline()
        h3p8l.config(text=h3p8status)
        time.sleep(.1)


        with open("H3P09Status.txt", 'r') as file:
            h3p9status = file.readline()
        h3p9l.config(text=h3p9status)
        time.sleep(.1)

        with open("H3P10Status.txt", 'r') as file:
            h3p10status = file.readline()
        h3p10l.config(text=h3p10status)
        time.sleep(.1)


        with open("H3P11Status.txt", 'r') as file:
            h3p11status = file.readline()
        h3p11l.config(text=h3p11status)
        time.sleep(.1)


        with open("H3P12Status.txt", 'r') as file:
            h3p12status = file.readline()
        h3p12l.config(text=h3p12status)
        time.sleep(.1) 


        with open("H3P13Status.txt", 'r') as file:
            h3p13status = file.readline()
        h3p13l.config(text=h3p13status)
        time.sleep(.1)


        with open("H3P14Status.txt", 'r') as file:
            h3p14status = file.readline()
        h3p14l.config(text=h3p14status)
        time.sleep(.1) 


        with open("H3P15Status.txt", 'r') as file:
            h3p15status = file.readline()
        h3p15l.config(text=h3p15status)
        time.sleep(.1) 
        

        with open("H3P16Status.txt", 'r') as file:
            h3p16status = file.readline()
        h3p16l.config(text=h3p16status)
        time.sleep(.1) 

def update_GUI04():
        global h4p1status
        global h4p2status
        global h4p3status
        global h4p4status
        global h4p5status
        global h4p6status
        global h4p7status
        global h4p8status
        global h4p9status
        global h4p10status
        global h4p11status
        global h4p12status
        global h4p13status
        global h4p14status
        global h4p15status
        global h4p16status


        root.after(50000, update_GUI04)


        with open("H4P01Status.txt", 'r') as file:
            h4p1status = file.readline()
        h4p1l.config(text=h4p1status)
        time.sleep(.1)


        with open("H4P02Status.txt", 'r') as file:
            h4p2status = file.readline()
        h4p2l.config(text=h4p2status)
        time.sleep(.1)


        with open("H4P03Status.txt", 'r') as file:
            h4p3status = file.readline()
        h4p3l.config(text=h4p3status)
        time.sleep(.1)


        with open("H4P04Status.txt", 'r') as file:
            h4p4status = file.readline()
        h4p4l.config(text=h4p4status)
        time.sleep(.1)


        with open("H4P05Status.txt", 'r') as file:
            h4p5status = file.readline()
        h4p5l.config(text=h4p5status)
        time.sleep(.1)


        with open("H4P06Status.txt", 'r') as file:
            h4p6status = file.readline()
        h4p6l.config(text=h4p6status)
        time.sleep(.1)


        with open("H4P07Status.txt", 'r') as file:
            h4p7status = file.readline()
        h4p7l.config(text=h4p7status)
        time.sleep(.1)

        with open("H4P08Status.txt", 'r') as file:
            h4p8status = file.readline()
        h4p8l.config(text=h4p8status)
        time.sleep(.1)


        with open("H4P09Status.txt", 'r') as file:
            h4p9status = file.readline()
        h4p9l.config(text=h4p9status)
        time.sleep(.1)

        with open("H4P10Status.txt", 'r') as file:
            h4p10status = file.readline()
        h4p10l.config(text=h4p10status)
        time.sleep(.1)


        with open("H4P11Status.txt", 'r') as file:
            h4p11status = file.readline()
        h4p11l.config(text=h4p11status)
        time.sleep(.1)


        with open("H4P12Status.txt", 'r') as file:
            h4p12status = file.readline()
        h4p12l.config(text=h4p12status)
        time.sleep(.1) 


        with open("H4P13Status.txt", 'r') as file:
            h4p13status = file.readline()
        h4p13l.config(text=h4p13status)
        time.sleep(.1)


        with open("H4P14Status.txt", 'r') as file:
            h4p14status = file.readline()
        h4p14l.config(text=h4p14status)
        time.sleep(.1) 


        with open("H4P15Status.txt", 'r') as file:
            h4p15status = file.readline()
        h4p15l.config(text=h4p15status)
        time.sleep(.1) 
        

        with open("H4P16Status.txt", 'r') as file:
            h4p16status = file.readline()
        h4p16l.config(text=h4p16status)
        time.sleep(.1)



def start01():
    global status
    update_GUI01()
    status = "Starting..."
    print("Start Button")
    time.sleep(.5)
    subprocess.Popen(["python", "H1P01.py"], shell=True)
    time.sleep(.1)
    with open("H1P01Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H1P02.py"], shell=True)
    time.sleep(.1)
    with open("H1P02Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H1P03.py"], shell=True)
    time.sleep(.1)
    with open("H1P03Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H1P04.py"], shell=True)
    time.sleep(.1)
    with open("H1P04Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H1P05.py"], shell=True)
    time.sleep(.1)
    with open("H1P05Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H1P06.py"], shell=True)
    time.sleep(.1)
    with open("H1P06Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H1P07.py"], shell=True)
    time.sleep(.1)
    with open("H1P07Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H1P08.py"], shell=True)
    time.sleep(.1)
    with open("H1P08Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H1P09.py"], shell=True)
    time.sleep(.1)
    with open("H1P09Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H1P10.py"], shell=True)
    time.sleep(.1)
    with open("H1P10Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H1P11.py"], shell=True)
    time.sleep(.1)
    with open("H1P11Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H1P12.py"], shell=True)
    time.sleep(.1)
    with open("H1P12Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H1P13.py"], shell=True)
    time.sleep(.1)
    with open("H1P13Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H1P14.py"], shell=True)
    time.sleep(.1)
    with open("H1P14Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H1P15.py"], shell=True)
    time.sleep(.1)
    with open("H1P15Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H1P16.py"], shell=True)
    time.sleep(.1)
    with open("H1P16Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H1P01.py"], shell=True)
    time.sleep(.1)


def start02():
    global status
    update_GUI02()
    status = "Starting..."
    print("Start Button")
    time.sleep(.5)
    with open("H2P01Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H1P02.py"], shell=True)
    time.sleep(.1)
    with open("H2P02Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H1P03.py"], shell=True)
    time.sleep(.1)
    with open("H2P03Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H1P04.py"], shell=True)
    time.sleep(.1)
    with open("H2P04Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H1P05.py"], shell=True)
    time.sleep(.1)
    with open("H2P05Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H1P06.py"], shell=True)
    time.sleep(.1)
    with open("H2P06Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H1P07.py"], shell=True)
    time.sleep(.1)
    with open("H2P07Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H1P08.py"], shell=True)
    time.sleep(.1)
    with open("H2P08Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H1P09.py"], shell=True)
    time.sleep(.1)
    with open("H2P09Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H1P10.py"], shell=True)
    time.sleep(.1)
    with open("H2P10Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H1P11.py"], shell=True)
    time.sleep(.1)
    with open("H2P11Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H1P12.py"], shell=True)
    time.sleep(.1)
    with open("H2P12Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H1P13.py"], shell=True)
    time.sleep(.1)
    with open("H2P13Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H1P14.py"], shell=True)
    time.sleep(.1)
    with open("H2P14Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H1P15.py"], shell=True)
    time.sleep(.1)
    with open("H2P15Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H1P16.py"], shell=True)
    time.sleep(.1)
    with open("H2P16Status.txt", 'w') as file:
        print("Starting", file=file)

def start03():
    global status
    update_GUI03()
    status = "Starting..."
    print("Start Button")
    time.sleep(.5)
    subprocess.Popen(["python", "H3P01.py"], shell=True)
    time.sleep(.1)
    with open("H3P01Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H3P02.py"], shell=True)
    time.sleep(.1)
    with open("H3P02Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H3P03.py"], shell=True)
    time.sleep(.1)
    with open("H3P03Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H3P04.py"], shell=True)
    time.sleep(.1)
    with open("H3P04Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H3P05.py"], shell=True)
    time.sleep(.1)
    with open("H3P05Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H3P06.py"], shell=True)
    time.sleep(.1)
    with open("H3P06Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H3P07.py"], shell=True)
    time.sleep(.1)
    with open("H3P07Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H3P08.py"], shell=True)
    time.sleep(.1)
    with open("H3P08Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H3P09.py"], shell=True)
    time.sleep(.1)
    with open("H3P09Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H3P10.py"], shell=True)
    time.sleep(.1)
    with open("H3P10Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H3P11.py"], shell=True)
    time.sleep(.1)
    with open("H3P11Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H3P12.py"], shell=True)
    time.sleep(.1)
    with open("H3P12Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H3P13.py"], shell=True)
    time.sleep(.1)
    with open("H3P13Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H3P14.py"], shell=True)
    time.sleep(.1)
    with open("H3P14Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H3P15.py"], shell=True)
    time.sleep(.1)
    with open("H3P15Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "HP16.py"], shell=True)
    time.sleep(.1)
    with open("H3P16Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H3P01.py"], shell=True)
    time.sleep(.1)


def start04():
    global status
    update_GUI04()
    status = "Starting..."
    print("Start Button")
    time.sleep(.5)
    with open("H4P01Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H4P02.py"], shell=True)
    time.sleep(.1)
    with open("H4P02Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H4P03.py"], shell=True)
    time.sleep(.1)
    with open("H4P03Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H4P04.py"], shell=True)
    time.sleep(.1)
    with open("H4P04Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H4P05.py"], shell=True)
    time.sleep(.1)
    with open("H4P05Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H4P06.py"], shell=True)
    time.sleep(.1)
    with open("H4P06Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H4P07.py"], shell=True)
    time.sleep(.1)
    with open("H4P07Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H4P08.py"], shell=True)
    time.sleep(.1)
    with open("H4P08Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H4P09.py"], shell=True)
    time.sleep(.1)
    with open("H4P09Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H4P10.py"], shell=True)
    time.sleep(.1)
    with open("H4P10Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H4P11.py"], shell=True)
    time.sleep(.1)
    with open("H4P11Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H4P12.py"], shell=True)
    time.sleep(.1)
    with open("H4P12Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H4P13.py"], shell=True)
    time.sleep(.1)
    with open("H4P13Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H4P14.py"], shell=True)
    time.sleep(.1)
    with open("H4P14Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H4P15.py"], shell=True)
    time.sleep(.1)
    with open("H4P15Status.txt", 'w') as file:
        print("Starting", file=file)
    subprocess.Popen(["python", "H4P16.py"], shell=True)
    time.sleep(.1)
    with open("H4P16Status.txt", 'w') as file:
        print("Starting", file=file)

def stop():
    global h1p01stat
    h1p01stat = "Stopped"
    print("Stop Button")

def restart():
    global h1p01stat
    h1p01stat = "Restarted"
    print("Restart Button ")

status = "Not Started"
    
root = Tk()

root.title("Network Erasure")
mainframe = ttk.Frame(root, padding=15, relief=SOLID)
header = ttk.Frame(mainframe, padding=10, relief=SOLID)
frame1 = ttk.Frame(mainframe, padding=25, relief=SUNKEN)
frame2 = ttk.Frame(mainframe, padding=25, relief=SUNKEN)
frame3 = ttk.Frame(mainframe, padding=25, relief=SUNKEN)
frame4 = ttk.Frame(mainframe, padding=25, relief=SUNKEN)

h1p1frame = ttk.Frame(frame1,padding=5,relief=SOLID)
h1p2frame = ttk.Frame(frame1,padding=5,relief=SOLID)
h1p3frame = ttk.Frame(frame1,padding=5,relief=SOLID)
h1p4frame = ttk.Frame(frame1,padding=5,relief=SOLID)
h1p5frame = ttk.Frame(frame1,padding=5,relief=SOLID)
h1p6frame = ttk.Frame(frame1,padding=5,relief=SOLID)
h1p7frame = ttk.Frame(frame1,padding=5,relief=SOLID)
h1p8frame = ttk.Frame(frame1,padding=5,relief=SOLID)
h1p9frame = ttk.Frame(frame1,padding=5,relief=SOLID)
h1p10frame = ttk.Frame(frame1,padding=5,relief=SOLID)
h1p11frame = ttk.Frame(frame1,padding=5,relief=SOLID)
h1p12frame = ttk.Frame(frame1,padding=5,relief=SOLID)
h1p13frame = ttk.Frame(frame1,padding=5,relief=SOLID)
h1p14frame = ttk.Frame(frame1,padding=5,relief=SOLID)
h1p15frame = ttk.Frame(frame1,padding=5,relief=SOLID)
h1p16frame = ttk.Frame(frame1,padding=5,relief=SOLID)

h2p1frame = ttk.Frame(frame2,padding=5,relief=SOLID)
h2p2frame = ttk.Frame(frame2,padding=5,relief=SOLID)
h2p3frame = ttk.Frame(frame2,padding=5,relief=SOLID)
h2p4frame = ttk.Frame(frame2,padding=5,relief=SOLID)
h2p5frame = ttk.Frame(frame2,padding=5,relief=SOLID)
h2p6frame = ttk.Frame(frame2,padding=5,relief=SOLID)
h2p7frame = ttk.Frame(frame2,padding=5,relief=SOLID)
h2p8frame = ttk.Frame(frame2,padding=5,relief=SOLID)
h2p9frame = ttk.Frame(frame2,padding=5,relief=SOLID)
h2p10frame = ttk.Frame(frame2,padding=5,relief=SOLID)
h2p11frame = ttk.Frame(frame2,padding=5,relief=SOLID)
h2p12frame = ttk.Frame(frame2,padding=5,relief=SOLID)
h2p13frame = ttk.Frame(frame2,padding=5,relief=SOLID)
h2p14frame = ttk.Frame(frame2,padding=5,relief=SOLID)
h2p15frame = ttk.Frame(frame2,padding=5,relief=SOLID)
h2p16frame = ttk.Frame(frame2,padding=5,relief=SOLID)

h3p1frame = ttk.Frame(frame3,padding=5,relief=SOLID)
h3p2frame = ttk.Frame(frame3,padding=5,relief=SOLID)
h3p3frame = ttk.Frame(frame3,padding=5,relief=SOLID)
h3p4frame = ttk.Frame(frame3,padding=5,relief=SOLID)
h3p5frame = ttk.Frame(frame3,padding=5,relief=SOLID)
h3p6frame = ttk.Frame(frame3,padding=5,relief=SOLID)
h3p7frame = ttk.Frame(frame3,padding=5,relief=SOLID)
h3p8frame = ttk.Frame(frame3,padding=5,relief=SOLID)
h3p9frame = ttk.Frame(frame3,padding=5,relief=SOLID)
h3p10frame = ttk.Frame(frame3,padding=5,relief=SOLID)
h3p11frame = ttk.Frame(frame3,padding=5,relief=SOLID)
h3p12frame = ttk.Frame(frame3,padding=5,relief=SOLID)
h3p13frame = ttk.Frame(frame3,padding=5,relief=SOLID)
h3p14frame = ttk.Frame(frame3,padding=5,relief=SOLID)
h3p15frame = ttk.Frame(frame3,padding=5,relief=SOLID)
h3p16frame = ttk.Frame(frame3,padding=5,relief=SOLID)

h4p1frame = ttk.Frame(frame4,padding=5,relief=SOLID)
h4p2frame = ttk.Frame(frame4,padding=5,relief=SOLID)
h4p3frame = ttk.Frame(frame4,padding=5,relief=SOLID)
h4p4frame = ttk.Frame(frame4,padding=5,relief=SOLID)
h4p5frame = ttk.Frame(frame4,padding=5,relief=SOLID)
h4p6frame = ttk.Frame(frame4,padding=5,relief=SOLID)
h4p7frame = ttk.Frame(frame4,padding=5,relief=SOLID)
h4p8frame = ttk.Frame(frame4,padding=5,relief=SOLID)
h4p9frame = ttk.Frame(frame4,padding=5,relief=SOLID)
h4p10frame = ttk.Frame(frame4,padding=5,relief=SOLID)
h4p11frame = ttk.Frame(frame4,padding=5,relief=SOLID)
h4p12frame = ttk.Frame(frame4,padding=5,relief=SOLID)
h4p13frame = ttk.Frame(frame4,padding=5,relief=SOLID)
h4p14frame = ttk.Frame(frame4,padding=5,relief=SOLID)
h4p15frame = ttk.Frame(frame4,padding=5,relief=SOLID)
h4p16frame = ttk.Frame(frame4,padding=5,relief=SOLID)






mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
header.grid(column=0, row=0, columnspan=8, sticky=(N))
frame1.grid(column=1, row=1, sticky=(W, E))
frame2.grid(column=2, row=1, sticky=(W, E))
frame3.grid(column=3, row=1, sticky=(W, E))
frame4.grid(column=4, row=1, sticky=(W, E))


h1p1frame.grid(column=0, row=2, columnspan=4, sticky=(N,E,W,S))
h1p2frame.grid(column=0, row=3, columnspan=4, sticky=(N,E,W,S))
h1p3frame.grid(column=0, row=4, columnspan=4, sticky=(N,E,W,S))
h1p4frame.grid(column=0, row=5, columnspan=4, sticky=(N,E,W,S))
h1p5frame.grid(column=0, row=6, columnspan=4, sticky=(N,E,W,S))
h1p6frame.grid(column=0, row=7, columnspan=4, sticky=(N,E,W,S))
h1p7frame.grid(column=0, row=8, columnspan=4, sticky=(N,E,W,S))
h1p8frame.grid(column=0, row=9, columnspan=4, sticky=(N,E,W,S))
h1p9frame.grid(column=0, row=10, columnspan=4, sticky=(N,E,W,S))
h1p10frame.grid(column=0, row=11, columnspan=4, sticky=(N,E,W,S))
h1p11frame.grid(column=0, row=12, columnspan=4, sticky=(N,E,W,S))
h1p12frame.grid(column=0, row=13, columnspan=4, sticky=(N,E,W,S))
h1p13frame.grid(column=0, row=14, columnspan=4, sticky=(N,E,W,S))
h1p14frame.grid(column=0, row=15, columnspan=4, sticky=(N,E,W,S))
h1p15frame.grid(column=0, row=16, columnspan=4, sticky=(N,E,W,S))
h1p16frame.grid(column=0, row=17, columnspan=4, sticky=(N,E,W,S))

h2p1frame.grid(column=0, row=2, columnspan=4, sticky=(N,E,W,S))
h2p2frame.grid(column=0, row=3, columnspan=4, sticky=(N,E,W,S))
h2p3frame.grid(column=0, row=4, columnspan=4, sticky=(N,E,W,S))
h2p4frame.grid(column=0, row=5, columnspan=4, sticky=(N,E,W,S))
h2p5frame.grid(column=0, row=6, columnspan=4, sticky=(N,E,W,S))
h2p6frame.grid(column=0, row=7, columnspan=4, sticky=(N,E,W,S))
h2p7frame.grid(column=0, row=8, columnspan=4, sticky=(N,E,W,S))
h2p8frame.grid(column=0, row=9, columnspan=4, sticky=(N,E,W,S))
h2p9frame.grid(column=0, row=10, columnspan=4, sticky=(N,E,W,S))
h2p10frame.grid(column=0, row=11, columnspan=4, sticky=(N,E,W,S))
h2p11frame.grid(column=0, row=12, columnspan=4, sticky=(N,E,W,S))
h2p12frame.grid(column=0, row=13, columnspan=4, sticky=(N,E,W,S))
h2p13frame.grid(column=0, row=14, columnspan=4, sticky=(N,E,W,S))
h2p14frame.grid(column=0, row=15, columnspan=4, sticky=(N,E,W,S))
h2p15frame.grid(column=0, row=16, columnspan=4, sticky=(N,E,W,S))
h2p16frame.grid(column=0, row=17, columnspan=4, sticky=(N,E,W,S))

h3p1frame.grid(column=0, row=2, columnspan=4, sticky=(N,E,W,S))
h3p2frame.grid(column=0, row=3, columnspan=4, sticky=(N,E,W,S))
h3p3frame.grid(column=0, row=4, columnspan=4, sticky=(N,E,W,S))
h3p4frame.grid(column=0, row=5, columnspan=4, sticky=(N,E,W,S))
h3p5frame.grid(column=0, row=6, columnspan=4, sticky=(N,E,W,S))
h3p6frame.grid(column=0, row=7, columnspan=4, sticky=(N,E,W,S))
h3p7frame.grid(column=0, row=8, columnspan=4, sticky=(N,E,W,S))
h3p8frame.grid(column=0, row=9, columnspan=4, sticky=(N,E,W,S))
h3p9frame.grid(column=0, row=10, columnspan=4, sticky=(N,E,W,S))
h3p10frame.grid(column=0, row=11, columnspan=4, sticky=(N,E,W,S))
h3p11frame.grid(column=0, row=12, columnspan=4, sticky=(N,E,W,S))
h3p12frame.grid(column=0, row=13, columnspan=4, sticky=(N,E,W,S))
h3p13frame.grid(column=0, row=14, columnspan=4, sticky=(N,E,W,S))
h3p14frame.grid(column=0, row=15, columnspan=4, sticky=(N,E,W,S))
h3p15frame.grid(column=0, row=16, columnspan=4, sticky=(N,E,W,S))
h3p16frame.grid(column=0, row=17, columnspan=4, sticky=(N,E,W,S))

h4p1frame.grid(column=0, row=2, columnspan=4, sticky=(N,E,W,S))
h4p2frame.grid(column=0, row=3, columnspan=4, sticky=(N,E,W,S))
h4p3frame.grid(column=0, row=4, columnspan=4, sticky=(N,E,W,S))
h4p4frame.grid(column=0, row=5, columnspan=4, sticky=(N,E,W,S))
h4p5frame.grid(column=0, row=6, columnspan=4, sticky=(N,E,W,S))
h4p6frame.grid(column=0, row=7, columnspan=4, sticky=(N,E,W,S))
h4p7frame.grid(column=0, row=8, columnspan=4, sticky=(N,E,W,S))
h4p8frame.grid(column=0, row=9, columnspan=4, sticky=(N,E,W,S))
h4p9frame.grid(column=0, row=10, columnspan=4, sticky=(N,E,W,S))
h4p10frame.grid(column=0, row=11, columnspan=4, sticky=(N,E,W,S))
h4p11frame.grid(column=0, row=12, columnspan=4, sticky=(N,E,W,S))
h4p12frame.grid(column=0, row=13, columnspan=4, sticky=(N,E,W,S))
h4p13frame.grid(column=0, row=14, columnspan=4, sticky=(N,E,W,S))
h4p14frame.grid(column=0, row=15, columnspan=4, sticky=(N,E,W,S))
h4p15frame.grid(column=0, row=16, columnspan=4, sticky=(N,E,W,S))
h4p16frame.grid(column=0, row=17, columnspan=4, sticky=(N,E,W,S))


ttk.Label(h1p1frame, text="H1-P01: ").grid(column=0, row=0)
ttk.Label(h1p2frame, text="H1-P02: ").grid(column=0, row=0)
ttk.Label(h1p3frame, text="H1-P03: ").grid(column=0, row=0)
ttk.Label(h1p4frame, text="H1-P04: ").grid(column=0, row=0)
ttk.Label(h1p5frame, text="H1-P05: ").grid(column=0, row=0)
ttk.Label(h1p6frame, text="H1-P06: ").grid(column=0, row=0)
ttk.Label(h1p7frame, text="H1-P07: ").grid(column=0, row=0)
ttk.Label(h1p8frame, text="H1-P08: ").grid(column=0, row=0)
ttk.Label(h1p9frame, text="H1-P09: ").grid(column=0, row=0)
ttk.Label(h1p10frame, text="H1-P10: ").grid(column=0, row=0)
ttk.Label(h1p11frame, text="H1-P11: ").grid(column=0, row=0)
ttk.Label(h1p12frame, text="H1-P12: ").grid(column=0, row=0)
ttk.Label(h1p13frame, text="H1-P13: ").grid(column=0, row=0)
ttk.Label(h1p14frame, text="H1-P14: ").grid(column=0, row=0)
ttk.Label(h1p15frame, text="H1-P15: ").grid(column=0, row=0)
ttk.Label(h1p16frame, text="H1-P16: ").grid(column=0, row=0)

ttk.Label(h2p1frame, text="H2-P01: ").grid(column=0, row=0)
ttk.Label(h2p2frame, text="H2-P02: ").grid(column=0, row=0)
ttk.Label(h2p3frame, text="H2-P03: ").grid(column=0, row=0)
ttk.Label(h2p4frame, text="H2-P04: ").grid(column=0, row=0)
ttk.Label(h2p5frame, text="H2-P05: ").grid(column=0, row=0)
ttk.Label(h2p6frame, text="H2-P06: ").grid(column=0, row=0)
ttk.Label(h2p7frame, text="H2-P07: ").grid(column=0, row=0)
ttk.Label(h2p8frame, text="H2-P08: ").grid(column=0, row=0)
ttk.Label(h2p9frame, text="H2-P09: ").grid(column=0, row=0)
ttk.Label(h2p10frame, text="H2-P10: ").grid(column=0, row=0)
ttk.Label(h2p11frame, text="H2-P11: ").grid(column=0, row=0)
ttk.Label(h2p12frame, text="H2-P12: ").grid(column=0, row=0)
ttk.Label(h2p13frame, text="H2-P13: ").grid(column=0, row=0)
ttk.Label(h2p14frame, text="H2-P14: ").grid(column=0, row=0)
ttk.Label(h2p15frame, text="H2-P15: ").grid(column=0, row=0)
ttk.Label(h2p16frame, text="H2-P16: ").grid(column=0, row=0)

ttk.Label(h3p1frame, text="H3-P01: ").grid(column=0, row=0)
ttk.Label(h3p2frame, text="H3-P02: ").grid(column=0, row=0)
ttk.Label(h3p3frame, text="H3-P03: ").grid(column=0, row=0)
ttk.Label(h3p4frame, text="H3-P04: ").grid(column=0, row=0)
ttk.Label(h3p5frame, text="H3-P05: ").grid(column=0, row=0)
ttk.Label(h3p6frame, text="H3-P06: ").grid(column=0, row=0)
ttk.Label(h3p7frame, text="H3-P07: ").grid(column=0, row=0)
ttk.Label(h3p8frame, text="H3-P08: ").grid(column=0, row=0)
ttk.Label(h3p9frame, text="H3-P09: ").grid(column=0, row=0)
ttk.Label(h3p10frame, text="H3-P10: ").grid(column=0, row=0)
ttk.Label(h3p11frame, text="H3-P11: ").grid(column=0, row=0)
ttk.Label(h3p12frame, text="H3-P12: ").grid(column=0, row=0)
ttk.Label(h3p13frame, text="H3-P13: ").grid(column=0, row=0)
ttk.Label(h3p14frame, text="H3-P14: ").grid(column=0, row=0)
ttk.Label(h3p15frame, text="H3-P15: ").grid(column=0, row=0)
ttk.Label(h3p16frame, text="H3-P16: ").grid(column=0, row=0)

ttk.Label(h4p1frame, text="H4-P01: ").grid(column=0, row=0)
ttk.Label(h4p2frame, text="H4-P02: ").grid(column=0, row=0)
ttk.Label(h4p3frame, text="H4-P03: ").grid(column=0, row=0)
ttk.Label(h4p4frame, text="H4-P04: ").grid(column=0, row=0)
ttk.Label(h4p5frame, text="H4-P05: ").grid(column=0, row=0)
ttk.Label(h4p6frame, text="H4-P06: ").grid(column=0, row=0)
ttk.Label(h4p7frame, text="H4-P07: ").grid(column=0, row=0)
ttk.Label(h4p8frame, text="H4-P08: ").grid(column=0, row=0)
ttk.Label(h4p9frame, text="H4-P09: ").grid(column=0, row=0)
ttk.Label(h4p10frame, text="H4-P10: ").grid(column=0, row=0)
ttk.Label(h4p11frame, text="H4-P11: ").grid(column=0, row=0)
ttk.Label(h4p12frame, text="H4-P12: ").grid(column=0, row=0)
ttk.Label(h4p13frame, text="H4-P13: ").grid(column=0, row=0)
ttk.Label(h4p14frame, text="H4-P14: ").grid(column=0, row=0)
ttk.Label(h4p15frame, text="H4-P15: ").grid(column=0, row=0)
ttk.Label(h4p16frame, text="H4-P16: ").grid(column=0, row=0)



h1p1l = ttk.Label(h1p1frame, text=status)
h1p1l.grid(column=2, row=0, columnspan=2)

h1p2l = ttk.Label(h1p2frame, text=status)
h1p2l.grid(column=2, row=0, columnspan=2)

h1p3l = ttk.Label(h1p3frame, text=status)
h1p3l.grid(column=2, row=0, columnspan=2)

h1p4l = ttk.Label(h1p4frame, text=status)
h1p4l.grid(column=2, row=0, columnspan=2)

h1p5l = ttk.Label(h1p5frame, text=status)
h1p5l.grid(column=2, row=0, columnspan=2)

h1p6l = ttk.Label(h1p6frame, text=status)
h1p6l.grid(column=2, row=0, columnspan=2)

h1p7l = ttk.Label(h1p7frame, text=status)
h1p7l.grid(column=2, row=0, columnspan=2)

h1p8l = ttk.Label(h1p8frame, text=status)
h1p8l.grid(column=2, row=0, columnspan=2)

h1p9l = ttk.Label(h1p9frame, text=status)
h1p9l.grid(column=2, row=0, columnspan=2)

h1p10l = ttk.Label(h1p10frame, text=status)
h1p10l.grid(column=2, row=0, columnspan=2)

h1p11l = ttk.Label(h1p11frame, text=status)
h1p11l.grid(column=2, row=0, columnspan=2)

h1p12l = ttk.Label(h1p12frame, text=status)
h1p12l.grid(column=2, row=0, columnspan=2)

h1p13l = ttk.Label(h1p13frame, text=status)
h1p13l.grid(column=2, row=0, columnspan=2)

h1p14l = ttk.Label(h1p14frame, text=status)
h1p14l.grid(column=2, row=0, columnspan=2)

h1p15l = ttk.Label(h1p15frame, text=status)
h1p15l.grid(column=2, row=0, columnspan=2)

h1p16l = ttk.Label(h1p16frame, text=status)
h1p16l.grid(column=2, row=0, columnspan=2)

h2p1l = ttk.Label(h2p1frame, text=status)
h2p1l.grid(column=2, row=0, columnspan=2)

h2p2l = ttk.Label(h2p2frame, text=status)
h2p2l.grid(column=2, row=0, columnspan=2)

h2p3l = ttk.Label(h2p3frame, text=status)
h2p3l.grid(column=2, row=0, columnspan=2)

h2p4l = ttk.Label(h2p4frame, text=status)
h2p4l.grid(column=2, row=0, columnspan=2)

h2p5l = ttk.Label(h2p5frame, text=status)
h2p5l.grid(column=2, row=0, columnspan=2)

h2p6l = ttk.Label(h2p6frame, text=status)
h2p6l.grid(column=2, row=0, columnspan=2)

h2p7l = ttk.Label(h2p7frame, text=status)
h2p7l.grid(column=2, row=0, columnspan=2)

h2p8l = ttk.Label(h2p8frame, text=status)
h2p8l.grid(column=2, row=0, columnspan=2)

h2p9l = ttk.Label(h2p9frame, text=status)
h2p9l.grid(column=2, row=0, columnspan=2)

h2p10l = ttk.Label(h2p10frame, text=status)
h2p10l.grid(column=2, row=0, columnspan=2)

h2p11l = ttk.Label(h2p11frame, text=status)
h2p11l.grid(column=2, row=0, columnspan=2)

h2p12l = ttk.Label(h2p12frame, text=status)
h2p12l.grid(column=2, row=0, columnspan=2)

h2p13l = ttk.Label(h2p13frame, text=status)
h2p13l.grid(column=2, row=0, columnspan=2)

h2p14l = ttk.Label(h2p14frame, text=status)
h2p14l.grid(column=2, row=0, columnspan=2)

h2p15l = ttk.Label(h2p15frame, text=status)
h2p15l.grid(column=2, row=0, columnspan=2)

h2p16l = ttk.Label(h2p16frame, text=status)
h2p16l.grid(column=2, row=0, columnspan=2)

h3p1l = ttk.Label(h3p1frame, text=status)
h3p1l.grid(column=2, row=0, columnspan=2)

h3p2l = ttk.Label(h3p2frame, text=status)
h3p2l.grid(column=2, row=0, columnspan=2)

h3p3l = ttk.Label(h3p3frame, text=status)
h3p3l.grid(column=2, row=0, columnspan=2)

h3p4l = ttk.Label(h3p4frame, text=status)
h3p4l.grid(column=2, row=0, columnspan=2)

h3p5l = ttk.Label(h3p5frame, text=status)
h3p5l.grid(column=2, row=0, columnspan=2)

h3p6l = ttk.Label(h3p6frame, text=status)
h3p6l.grid(column=2, row=0, columnspan=2)

h3p7l = ttk.Label(h3p7frame, text=status)
h3p7l.grid(column=2, row=0, columnspan=2)

h3p8l = ttk.Label(h3p8frame, text=status)
h3p8l.grid(column=2, row=0, columnspan=2)

h3p9l = ttk.Label(h3p9frame, text=status)
h3p9l.grid(column=2, row=0, columnspan=2)

h3p10l = ttk.Label(h3p10frame, text=status)
h3p10l.grid(column=2, row=0, columnspan=2)

h3p11l = ttk.Label(h3p11frame, text=status)
h3p11l.grid(column=2, row=0, columnspan=2)

h3p12l = ttk.Label(h3p12frame, text=status)
h3p12l.grid(column=2, row=0, columnspan=2)

h3p13l = ttk.Label(h3p13frame, text=status)
h3p13l.grid(column=2, row=0, columnspan=2)

h3p14l = ttk.Label(h3p14frame, text=status)
h3p14l.grid(column=2, row=0, columnspan=2)

h3p15l = ttk.Label(h3p15frame, text=status)
h3p15l.grid(column=2, row=0, columnspan=2)

h3p16l = ttk.Label(h3p16frame, text=status)
h3p16l.grid(column=2, row=0, columnspan=2)

h4p1l = ttk.Label(h4p1frame, text=status)
h4p1l.grid(column=2, row=0, columnspan=2)

h4p2l = ttk.Label(h4p2frame, text=status)
h4p2l.grid(column=2, row=0, columnspan=2)

h4p3l = ttk.Label(h4p3frame, text=status)
h4p3l.grid(column=2, row=0, columnspan=2)

h4p4l = ttk.Label(h4p4frame, text=status)
h4p4l.grid(column=2, row=0, columnspan=2)

h4p5l = ttk.Label(h4p5frame, text=status)
h4p5l.grid(column=2, row=0, columnspan=2)

h4p6l = ttk.Label(h4p6frame, text=status)
h4p6l.grid(column=2, row=0, columnspan=2)

h4p7l = ttk.Label(h4p7frame, text=status)
h4p7l.grid(column=2, row=0, columnspan=2)

h4p8l = ttk.Label(h4p8frame, text=status)
h4p8l.grid(column=2, row=0, columnspan=2)

h4p9l = ttk.Label(h4p9frame, text=status)
h4p9l.grid(column=2, row=0, columnspan=2)

h4p10l = ttk.Label(h4p10frame, text=status)
h4p10l.grid(column=2, row=0, columnspan=2)

h4p11l = ttk.Label(h4p11frame, text=status)
h4p11l.grid(column=2, row=0, columnspan=2)

h4p12l = ttk.Label(h4p12frame, text=status)
h4p12l.grid(column=2, row=0, columnspan=2)

h4p13l = ttk.Label(h4p13frame, text=status)
h4p13l.grid(column=2, row=0, columnspan=2)

h4p14l = ttk.Label(h4p14frame, text=status)
h4p14l.grid(column=2, row=0, columnspan=2)

h4p15l = ttk.Label(h4p15frame, text=status)
h4p15l.grid(column=2, row=0, columnspan=2)

h4p16l = ttk.Label(h4p16frame, text=status)
h4p16l.grid(column=2, row=0, columnspan=2)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
ttk.Label(header, text="Data Lab Network Erasure").grid(column=0, row=0, columnspan=8)
ttk.Label(frame1, text="Hub-01").grid(column=0, row=0, columnspan=4)
ttk.Label(frame2, text="Hub-02").grid(column=0, row=0, columnspan=4)
ttk.Label(frame3, text="Hub-03").grid(column=0, row=0, columnspan=4)
ttk.Label(frame4, text="Hub-04").grid(column=0, row=0, columnspan=4)

ttk.Label(frame1, text=[]).grid(column=1, row=1, columnspan=2)
ttk.Label(frame2, text=[]).grid(column=1, row=1, columnspan=2)

ttk.Label(frame1, text="Port:").grid(column=0, row=1)
ttk.Label(frame2, text="Port:").grid(column=0, row=1)
ttk.Label(frame3, text="Port:").grid(column=0, row=1)
ttk.Label(frame4, text="Port:").grid(column=0, row=1)

ttk.Button(frame1, padding=2, text="Start", command=start01).grid(column=1, row=20)
ttk.Button(frame2, padding=2, text="Start", command=start02).grid(column=1, row=20)
ttk.Button(frame3, padding=2, text="Start", command=start03).grid(column=1, row=20)
ttk.Button(frame4, padding=2, text="Start", command=start04).grid(column=1, row=20)

#ttk.Button(frame1, padding=2, text="Stop", command=stop).grid(column=2, row=20)
#ttk.Button(frame1, padding=2, text="Restart", command=restart).grid(column=3, row=20)


if __name__ == "__main__":
            threads = []
            for script in ["H1P01.py", "H1P02.py", "H1P03.py", "H1P04.py", "H1P05.py", "H1P06.py", "H1P07.py", "H1P08.py", "H1P09.py", "H1P10.py", "H1P11.py", "H1P12.py", "H1P13.py", "H1P14.py", "H1P15.py", "H1P16.py"]:
                thread = threading.Thread(target=start01, args=(script,))
                threads.append(thread)
                thread.start()
            for script in ["H2P01.py", "H2P02.py", "H2P03.py", "H2P04.py", "H2P05.py", "H2P06.py", "H2P07.py", "H2P08.py", "H2P09.py", "H2P10.py", "H2P11.py", "H2P12.py", "H2P13.py", "H2P14.py", "H2P15.py", "H2P16.py"]:
                thread = threading.Thread(target=start02, args=(script,))
                threads.append(thread)
                thread.start()
            for script in ["H3P01.py", "H3P02.py", "H3P03.py", "H3P04.py", "H3P05.py", "H3P06.py", "H3P07.py", "H3P08.py", "H3P09.py", "H3P10.py", "H3P11.py", "H3P12.py", "H3P13.py", "H3P14.py", "H3P15.py", "H3P16.py"]:
                thread = threading.Thread(target=start01, args=(script,))
                threads.append(thread)
                thread.start()
            for script in ["H4P01.py", "H4P02.py", "H4P03.py", "H4P04.py", "H4P05.py", "H4P06.py", "H4P07.py", "H4P08.py", "H4P09.py", "H4P10.py", "H4P11.py", "H4P12.py", "H4P13.py", "H4P14.py", "H4P15.py", "H4P16.py"]:
                thread = threading.Thread(target=start02, args=(script,))
                threads.append(thread)
                thread.start()

            for thread in threads:
                thread.join()



root.mainloop()
