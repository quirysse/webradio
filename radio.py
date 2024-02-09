#!/usr/bin/env python3  
import subprocess  
import os  
import sys  
  
# Read radio stations from the text file  
def read_stations(file_name):  
	stations = {}  
	with open(file_name, "r") as file:  
		for line in file:  
			if line.strip():  
				key, name, url = line.strip()[1:-1].split("] ")[0], line.strip().split('"')[1], line.strip().split(' ')[-1]  
				stations[key] = {"name": name, "url": url}  
	return stations  
  
# Function to start the web radio  
def start_radio(url):  
	subprocess.Popen(["nohup", "mpg123", "-q", url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)  
  
# Function to stop the playback  
def stop_radio():  
	os.system("pkill -f mpg123")  
  
def change_radio(url):  
	stop_radio()  
	start_radio(url)  
  
# Launch the web radio  
if __name__ == "__main__":  
	stations = read_stations("stations.txt")  
	radio = stations[next(iter(stations))]["url"]    
  
	if len(sys.argv) == 2:  
		if sys.argv[1] == "on":  
			start_radio(radio)  
			print("Radio started in the background.")  
		elif sys.argv[1] == "off":  
			stop_radio()  
			print("Radio stopped.")  
		elif sys.argv[1] in stations:  
			change_radio(stations[sys.argv[1]]["url"])  
			print(f"Radio {stations[sys.argv[1]]['name']} started.")  
		else:  
			print("Unknown radio station.")  
	else:  
		print("Usage: python script.py [on|off|station_key]")  
