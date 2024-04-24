import datetime
import time
import winsound
def alarm(date_obj):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        date = current_time.strftime("%d/%m/%Y")
        #print("The Set Date is:"+date)
        if date_obj[0:2] == current_time.strftime("%I"):
            if date_obj[3:5] ==current_time.strftime("%M"):
                if date_obj[6:8] == current_time.strftime("%S"):
                    if date_obj[8:] == current_time.strftime("%p"):
                        print("hey wake up")
                        break

def accept_actual_time():
    #while True:
    alarm_peri =input("Enter time in HH:MM:SS AM/PM  format: ")
    if len(alarm_peri) != 10:
        print("Invalid format")
    else:
        alarm_hour = int(alarm_peri[0:2])
        alarm_minute = int(alarm_peri[3:5])
        alarm_second = int(alarm_peri[6:8])
        alarm_period = alarm_peri[8:]
        if alarm_hour > 12:
            print("Invalid, Input Correct Hour")
        elif alarm_minute > 59:
            print("Invalid,Input Correct Minutes ")
        elif alarm_second > 59:
            print( "Invalid, Input Correct Seconds")
        else:
            print("Alarm Set TO Be ",alarm_hour,':',alarm_minute,':',alarm_second,alarm_period)
    date_obj = f"{alarm_hour}:{alarm_minute}:{alarm_second}{alarm_period}"
    alarm(date_obj)
accept_actual_time()