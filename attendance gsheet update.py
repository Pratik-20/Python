import serial
import datetime
import gspread
import time

# using now() to get current time
current_time = datetime.datetime.now()

gs = gspread.service_account(filename="C:/Users/Pratik Thorawade/Downloads/sheetAuoth.json")
print(gs)
wks = gs.open("Attendance").sheet1
print(wks)

A = ['D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
     'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH']

B = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
     'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH']

ser = serial.Serial('COM3', 9600)  # replace 'COM3' with your Arduino port name

def write_read(x):
    ser.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = ser.readline()
    return data


def Initial_Data():

    fields = ['ID', 'Name', 'Branch']                       # Name first 3 fields
    for i in range (1,32):                                  # Add 31 Columns for each day of month
        fields.append('D'+str(i))                           # Day1 = D1

    wks.update('A1', [fields])                              # Add all fiels in sheet
    wks.format('1', {'textFormat': {'bold': True}})         # Make first Row Bold


#"""                                                        # While calling Initial Data remove '#'

def enroll():
    print("Enrolling New User in Google Sheet")
    num = input("Enter ID number To Enroll: ")              # Taking input from user
    value = write_read(num)
    #print("Enrolling New User at thew location - ",value)

    aa = int(num) + 1
    numm = str(aa)

    Acell = 'A'+ numm
    ID = numm
    #print(Acell)
    wks.update(Acell, [[num]])

    Bcell = 'B'+ str(numm)
    Name = str(input("Enter Student Name : "))
    #print(Acell)
    wks.update(Bcell, [[Name]])

    Ccell = 'C' + str(numm)
    Branch = str(input("Enter Student Branch : "))
    # print(Bcell)
    wks.update(Ccell, [[Branch]])



def Delet():
    print("Deleting User is Started")
    num = input("Enter ID number To Delete: ")                           # Taking input from user
    value = write_read(num)
    print(value)
    print("Deleting User")
    
    """
    b = str(value)
    a = ""
    for i in B:
        C = (i + b)
        wks.update(C, [[a]])
    """

def presenty():
    #print("Marking Attendance")
    ReceivedString = ser.readline().decode().rstrip()
    try:
        ID = ReceivedString
        ReceivedString = int(ID)
    except:
        ValueError()

    ID = int(ID) + 1

    if ID < 100:
        ID = str(ID)
        #print("ID is ",ID)

        Dcell = A[current_time.day - 1] + ID
        #print(Dcell)

        curr_time = time.strftime("%H:%M:%S", time.localtime())

        wks.update(Dcell, [[curr_time]])
        #print("Online Attendance Marked Successfully..!")



while True:
    while ser.in_waiting > 0:
        ReceivedString = ser.readline().decode().rstrip()
        #print(ReceivedString)
        while ReceivedString != None:
            ReceivedString = ser.readline().decode().rstrip()
            print(ReceivedString)

            if ReceivedString == "Found ID":
                presenty()
            elif ReceivedString == "Delete ID":
                Delet()
            elif ReceivedString == "New Enrollment":
                enroll()
#"""                                                       # While calling Initial Data remove '#'

#Initial_Data()