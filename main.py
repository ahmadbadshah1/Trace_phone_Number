import phonenumbers
from phonenumbers import timezone,geocoder,carrier

number= input("Enter the phone number :")
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone,"en")

print(phone)
print(time)
print(car)





