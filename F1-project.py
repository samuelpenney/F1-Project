# Import json and os modules
import json
import os

# Used to change the directory if needed
os.chdir(r"")
# Defines a function that reads the pit data from F12024R3SAINZ.json
def get_pit_data():
    with open("F12024R3SAINZ.json") as f:
        data = json.load(f)
    return data
# Defines a function that reads the lap data using f1laps.json
def get_lap_data():
    with open("f1laps.json") as f:
        data = json.load(f)
    return data

# Defines a function called diplay_lapbylap which will display the time on every lap
def display_lapbylap():
    # Calls pit_data and lap_data functions
    pit_data = get_pit_data()
    lap_data = get_lap_data()

    # Gets important variables from the json files
    driver_name = [pit_data["MRData"]["RaceTable"]["driverId"]]
    laps = [pitstop["lap"] for race in pit_data["MRData"]["RaceTable"]["Races"] for pitstop in race["PitStops"]]
    lap_times = [
        (lap["number"], timing["time"]) for race in lap_data["MRData"]["RaceTable"]["Races"]
        for lap in race["Laps"] for timing in lap["Timings"]
    ]
    # Prints out the drivers name, their pit laps and all of their times
    print(driver_name[0])
    print("Pitted at:", laps)
    for lap_number, lap_time in lap_times:
        lap_number = int(lap_number)
        # Temp solution for tire compounds
        if lap_number <= 16:
            tire_compound = 'M'
        else:
            tire_compound = 'H'
        print(f"Tire: {tire_compound}. Lap {lap_number}: {lap_time}")
        # Temp solution to display pit
        if lap_number == 16 or lap_number == 41:
            print("PIT")
# Calls the display_lapbylap function
display_lapbylap()
