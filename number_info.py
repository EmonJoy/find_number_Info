import pyfiglet
import phonenumbers
from phonenumbers import timezone , geocoder, carrier

fig = pyfiglet.figlet_format("TTF Number INFO Gathering", font = "digital")
print(fig)
try:
    number = input("Enter your number with country code: ")
    phone = phonenumbers.parse(number)
    get_data = geocoder.description_for_number(phone, lang="en")
    car = carrier.name_for_number(phone, lang="en")
    tym = timezone.time_zones_for_number(phone)

    print(car)
    print(get_data)
    print(tym)
except:
    print("Error, Looks like you are not using country code,try again with country code\nE:X-\nfor BD use +88\nfor US use +1\nfor India use +91 etc..")
