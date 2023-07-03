import datetime
import pyfiglet
import time
from colorama import Fore, Back, Style
import phonenumbers
from phonenumbers import timezone , geocoder, carrier

fig = pyfiglet.figlet_format("TTF Number INFO Gathering", font = "digital")
print(fig)
class color:
    red = Fore.RED
    green = Fore.GREEN
    cyan = Fore.LIGHTCYAN_EX
    bright_style = Style.BRIGHT
    back_style = Back.GREEN
class clock:
    clc = datetime.datetime.now()
    main_TYM = clc.strftime("%H/%D/%M")
print(color.cyan+color.bright_style+"CODDED BY MR MORNINGSTAR.")
print("Loading...")
time.sleep(2)

try:
    number = input("Enter your number with country code ==> ")
    phone = phonenumbers.parse(number)
    get_data = geocoder.description_for_number(phone, lang="en")
    car = carrier.name_for_number(phone, lang="en")
    tym = timezone.time_zones_for_number(phone)

    with open("info.txt", "a") as info:
        info.write(clock.main_TYM+"\n")
        info.write(number+"\n")
        info.write(car+"\n")
        info.write(get_data+"\n")
        info.write(str(tym)+"\n" + "\n")

    print(car)
    print(get_data)
    print(tym)
    print(color.green+color.bright_style+"File saved as info.txt in this path...")
except:
    print(color.red+color.bright_style+"Error, Looks like you are not using country code,try again with country code you stupid!Fix it and try again!!!\nE:X-\nfor BD use +88\nfor US use +1\nfor India use +91 etc..")
