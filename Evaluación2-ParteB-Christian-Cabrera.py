import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "5GxS089RD44ilkFrWGPhevdzbBJkA3p9"

while True:
    desde = input("Ingrese su ciudad de origen: ")
    if desde == "salir" or desde == "s":
        break
    hasta = input("Ingrese su ciudad de destino: ")
    if hasta == "salir" or hasta == "s":
        break
    url = main_api + urllib.parse.urlencode({"key" :key, "from" :desde, "to" :hasta})
    print("URL: " + (url))
    
    json_data = requests.get(url).json()
    json_status = json_data ["info"] ["statuscode"]
   
    if json_status == 0:
       print("Estado de la API: " + str(json_status) + " = Solicitud de ruta exitosa.\n")
       print("=============================================")
       print("Direcciones desde " + (desde) + " hasta " + (hasta))
       print("Duracion del viaje:   " + (json_data["route"]["formattedTime"]))
       print("Kilometros: " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)) + " Kms")
       print("=============================================")
       for each in json_data["route"]["legs"][0]["maneuvers"]:
           print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
           print("=============================================\n")
               
    elif json_status == 402:
        print("**********************************************")
        print("Codigo Status: " + str(json_status) + "; Entrada invalida para una o ambas ubicaciones.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Codigo Status: " + str(json_status) + "; Entrada faltante para una o ambas ubicaciones.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("Para Codigo Status: " + str(json_status) + "; Consultar en:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")