import time
import datetime
def validate_parameter(Time_play):
            if len(Time_play) != 10:
                print("Invalid Format")
            else:
                if int(Time_play[0:2]) > 12:
                    print("Invalid, Input Correct Hour")
                elif int(Time_play[3:5]) > 59:
                    print("Invalid,Input Correct Minutes ")
                elif int(Time_play[6:8])> 59:
                    print("Invalid, Input Correct Seconds!")
                else:
                    return 1
def validation_store():
    Time_ex = input("Enter time in HH:MM:SS AM/PM  format: ")
    Exercise= str(input("Your Request for Time Set:  "))
    validate = validate_parameter(Time_ex)
    if validate !=1:
        print(validate)
        return 1
    else:
        print(Time_ex,"Is Scheduled For", Exercise)
    Time_Exercise=Time_ex
    schedul_logi(Time_Exercise)


def schedul_logi(Time_Exercise):
    while True:
            print("Do You Want To Add Another Schedule: ")
            option =input("Y or N:  ")
            if option == "y":
                validation_store()

            else:
                break
    Time = Time_Exercise[:10]
    print(Time)

validation_store()