import csv
import random
import time
import pandas as pd
# Open the csv file for writing
def writeRow(h,m,s):
    h = str(h)
    m = str(m)
    s = str(s)
    Timestamp = "9/29/2022" +" " + h + ":" + m+ ":" + s
    TZ = 'n'
    JType = random.uniform(98.5, 100)
    ir1 = random.uniform(98.5, 400)
    ir2 = random.uniform(98.5, 400)
    ir3 = random.uniform(98.5, 400)
    ir4 = random.uniform(98.5, 400)
    ir5 = random.uniform(98.5, 400)
    ir6 = random.uniform(98.5, 400)
    ir7 = random.uniform(98.5, 400)
    ir8 = random.uniform(98.5, 400.0)
    ir9 = random.uniform(98.5, 400.0)
    ir10 = random.uniform(98.5, 400.0)
    rtd1 = random.uniform(98.5, 400.0)
    rtd2 = random.uniform(98.5, 400.0)
    rtd3 = random.uniform(98.5, 400.0)
    p2 = random.uniform(98.5, 400.0)
    p1 = random.uniform(-11.9, -11.0)
    ifmWater1 = random.uniform(40.0, 50.0)
    ifm2 = random.uniform(240.0, 260.0)
    ifmAir = random.uniform(-13.0, -12.0)
    ifmWater2 = random.uniform(40.0, 50.0)

    row = [Timestamp,JType,ir1,ir2,ir3,ir4,ir5,ir6,ir7,ir8,ir9,ir10,rtd1,rtd2,rtd3,p2,p1,ifmWater1,ifm2,ifmAir,ifmWater2]
    return row



with open('numbers.csv', 'w') as fileObj:
    # Creater a CSV writer object
    writerObj = csv.writer(fileObj)
    # Add header row as the list
    

    header = ["Timestamp","TZ","J-Type TC 1 (degF)","IR 1 (F)","IR 2 (F)","IR 3 (F)","IR 4 (F)",
              "IR 5 (F)","IR 6 (F)","IR 7 (F)","IR 8 (F)","IR 9 (F)","IR 10 (F)","RTD 1 (degF)",
              "RTD 2 (degF)","RTD 3 (degF)","QPSH P2 (mA)","ASHCROFT P1 (mA)","IFM Water Flow 1 (gpm)",
              "IFM Air Vel 1 (mA)","IFM Water Flow 2 (gpm)"]
    writerObj.writerow(header)
    h,m,s = 15,0,0
    for i in range(60):
        for j in range(12):

            row = writeRow(h,m,s)
            print(row)
            writerObj.writerow(row)
            s = s + 5
            if(m == 60):
                m = 0
            if(s == 60):
                s = 0
            print('sleep ' + str(m) + str(s))

            time.sleep(5)
        m = m + 1

            
            


    
