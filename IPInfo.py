import os
import sys
import time
import argparse
from sys import argv
import requests, json


api = "http://ip-api.com/json/"
print("""
 _____ _____    _____ _   _ ______ ____  
|_   _|  __ \  |_   _| \ | |  ____/ __ \ 
  | | | |__) |   | | |  \| | |__ | |  | |
  | | |  ___/    | | | . ` |  __|| |  | |
 _| |_| |       _| |_| |\  | |   | |__| |
|_____|_|      |_____|_| \_|_|    \____/ 
                                         
	""")
toma = input("1.Si desea obtener informacion de una ip \n2.Si desea obtener informacion de una lista de ip's \n>>> ")

if toma == "1":
	try:
		a = 0
		ip = str(input("Digita una ip: "))
		req = requests.get(api+ip).json()
		while req["status"] == "fail":
			a = 1
			if a == 1:
				print("Ip no existe")
				break
			if a == 0:
				print("Target", ":", req["query"])
				print("Status", ":", req["status"])
				print("Country", ":", req["country"])
				print("Country Code", ":", req["countryCode"])
				print("Region", ":", req["region"])
				print("Region Name", ":", req["regionName"])
				print("City", ":", req["city"])
				print("Zip Code", ":", req["zip"])
				print("Lat", ":", req["lat"])
				print("Lon", ":", req["lon"])
				print("Time Zone", ":", req["timezone"])
				print("Isp", ":", req["isp"])
				print("Org", ":", req["org"])
				print("··········································")

	except:
		print("Asegurese de tener conexion wifi")
else:
	try:
		combo = input("Ubicacion Del Combo : ")
		combo = open(combo, 'r').readlines()
		combo = list(set(combo))
		combo = [linea.replace('\n',"") for linea in combo]
		#i = 1
		for linea in combo:
			ips = linea
			req = requests.get(api+linea).json()
			if req["status"] == "fail":
				print("Ip no existe")
				continue
			print("Target", ":", req["query"])
			print("Status", ":", req["status"])
			print("Country", ":", req["country"])
			print("Country Code", ":", req["countryCode"])
			print("Region", ":", req["region"])
			print("Region Name", ":", req["regionName"])
			print("City", ":", req["city"])
			print("Zip Code", ":", req["zip"])
			print("Lat", ":", req["lat"])
			print("Lon", ":", req["lon"])
			print("Time Zone", ":", req["timezone"])
			print("Isp", ":", req["isp"])
			print("Org", ":", req["org"])
			print("··········································")
			print("··········································\n", "Target", ":", req["query"], "\n", "Status", ":", req["status"], "\n", "Country", ":", req["country"], "\n", "Country Code", ":", req["countryCode"], "\n", "Region", ":", req["region"], "\n", "Region Name", ":", req["regionName"], "\n", "City", ":", req["city"], "\n", "Zip Code", ":", req["zip"], "\n", "Lat", ":", req["lat"], "\n", "Lon", ":", req["lon"], "\n", "Time Zone", ":", req["timezone"], "\n", "Isp", ":", req["isp"], "\n", "Org", ":", req["org"], file=open("infoips.txt", "a+"))
			time.sleep(1.5)
	except:
		print("Asegurese de tener conexion wifi")
