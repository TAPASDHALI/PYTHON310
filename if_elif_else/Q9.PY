## ACCEPT ANY CITY FROM THE USER AND DISPLAY MONUMENT OF THAT CITY
##  CITY             MONUMNET
## DELHI             RED FORT
## AGRA              TAJ MAHAL
## JAIPUR            JAL MAHAL

city = input("Write The city:- ")
if city.lower() == "delhi":
    print("Monumnent name is :- Red Fort")
elif city.lower() == "agra":
    print("Monumnent name is :- Taj Mahal")
elif city.lower() == "jaipur":
    print("Monumnent name is :- Jal Mahal")
else:
    print("Please write the correct name:- ")