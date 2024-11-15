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

# Calls both function
pit_data = get_pit_data()
lap_data = get_lap_data()


# Grabs the neccesary data from json files
laps = [pitstop["lap"] for race in pit_data["MRData"]["RaceTable"]["Races"] for pitstop in race["PitStops"]]
lap_times = [
    (lap["number"], timing["time"]) for race in lap_data["MRData"]["RaceTable"]["Races"]
    for lap in race["Laps"] for timing in lap["Timings"]
]
# Prints the output
'''
Output looks like:
Lap numbers: ['16', '41']
Lap 1: 1:28.375
Lap 2: 1:22.600
Lap 3: 1:23.006
Lap 4: 1:22.433
Lap 5: 1:22.629
Lap 6: 1:22.572
'''
print("Lap numbers:", laps)
for lap_number, lap_time in lap_times:
    print(f"Lap {lap_number}: {lap_time}")
