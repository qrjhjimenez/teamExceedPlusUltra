import urllib.parse
import requests
from tabulate import tabulate

main_api = "https://www.mapquestapi.com/directions/v2/route?" 
key = "fZadaFOY22VIEEemZcBFfxl5vjSXIPpZ"

historyMiles = [['Starting Location', 'Destination', 'Trip Duration', 'Miles', 'Fuel Used (Gal):']]
historyKilo = [['Starting Location', 'Destination', 'Trip Duration', 'Kilometers', 'Fuel Used (Ltr)']]

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break

    metric = input("Enter (M) for Miles or (K) for kilometer: ")
    if metric == "m" or metric == "M":
        url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
        print("URL: " + (url))
        json_data = requests.get(url).json()
        json_status = json_data["info"]["statuscode"]


        if json_status == 0:
            duration = (json_data["route"]["formattedTime"])
            numiles = str(json_data["route"]["distance"])
            numfuelgal = str(json_data["route"]["fuelUsed"])

            currentMiles = [['{}'.format(orig),'{}'.format(dest),'{}'.format(duration), '{}'.format(numiles),'{}'.format(numfuelgal)]]
            historyMiles.extend(currentMiles)
            print(tabulate(historyMiles, headers='firstrow', tablefmt='fancy_grid'))
            for each in json_data["route"]["legs"][0]["maneuvers"]:
                print((each["narrative"]) + " (" + str(json_data["route"]["distance"]) + " Miles)")
            print("=============================================\n")

    elif metric == "K" or metric == "k":
        if json_status == 0:
            duration = (json_data["route"]["formattedTime"])
            numkil = str("{:.2f}".format((json_data["route"]["distance"])*1.61))
            numfuellit = str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78))

            currentKilo = [['{}'.format(orig),'{}'.format(dest),'{}'.format(duration), '{}'.format(numkil),'{}'.format(numfuellit)]]
            historyKilo.extend(currentKilo)
            print(tabulate(historyKilo, headers='firstrow', tablefmt='fancy_grid'))
            for each in json_data["route"]["legs"][0]["maneuvers"]:
                print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])) + " Kilometers)"))
            print("=============================================\n")

    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")


