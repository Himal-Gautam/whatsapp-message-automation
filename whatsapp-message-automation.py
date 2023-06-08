import pywhatkit
import time

msg = "yourMsg"

with open('yourFilePath') as file:
    I=0
    for number in file:
        number = number.strip() #preprocess line
        # syntax: phone number with country code, message, hour and minutes
        pywhatkit.sendwhatmsg_instantly(number, msg, 25, True, 5)
        print(number)
