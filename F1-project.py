# Import json and os modules 
import json
import os

# Change the directory
os.chdir(r"")

# Defines a function called laptime which will change the format of the time from mm:ss.mss to ss.mss
def laptime(time_str):
    minutes, seconds = time_str.split(':')
    return int(minutes) * 60 + float(seconds)

# Defines a function called get_pit_data which opens the F12024R3SAINZ.json file
def get_pit_data():
    with open("F12024R3SAINZ.json") as f:
        data = json.load(f)
    return data

# Defines a function called get_lap_data which opens the f1lap1.json file
def get_lap_data():
    with open("f1lap1.json") as f:
        data = json.load(f)
    return data

# Defines a function called groupinglaps which will serperate each lap into different stints based on pit stops
def groupinglaps(lap_times, pit_laps):

    stints = []
    current_stint = []

    for lap_time in lap_times:
        lap_number = lap_time["lap"]  
        current_stint.append(lap_time["time"]) 

        if lap_number in pit_laps:
            stints.append(current_stint)  
            current_stint = []  

    if current_stint:
        stints.append(current_stint)

    return stints

# Defines a function called display_lapbylap which will only display the lap and laptimes
def display_lapbylap():
    pit_data = get_pit_data()
    lap_data = get_lap_data()

    driver_name = [pit_data["MRData"]["RaceTable"]["driverId"]]
    pitlaps = [pitstop["lap"] for race in pit_data["MRData"]["RaceTable"]["Races"] for pitstop in race["PitStops"]]
    lap_times = [
        (lap["number"], timing["time"]) for race in lap_data["MRData"]["RaceTable"]["Races"]
        for lap in race["Laps"] for timing in lap["Timings"]
    ]

    print(driver_name[0])
    print("Pitted at:", pitlaps)
    for lap_number, lap_time in lap_times:
        lap_number = int(lap_number)
        if lap_number <= 16:
            tire_compound = 'M'
        else:
            tire_compound = 'H'
        print(f"Tire: {tire_compound}. Lap {lap_number}: {lap_time}")
        if lap_number == 16 or lap_number == 41:
            print("PIT")

def lapstr_toint():
    pit_data = get_pit_data()
    lap_data = get_lap_data()
    
    lap_times = [{"lap": int(lap["number"]), "time": laptime(timing["time"])}
                 for race in lap_data["MRData"]["RaceTable"]["Races"]
                 for lap in race["Laps"] for timing in lap["Timings"]
    ]

    pit_stop_data = [
        int(pit_stop["lap"])
        for race in pit_data["MRData"]["RaceTable"]["Races"]
        for pit_stop in race["PitStops"]
    ]


    for pit_stop in pit_stop_data:
        print(f"Pit lap: {pit_stop}")

    for lap_datas in lap_times:
        print(f"Lap {lap_datas['lap']}: {lap_datas['time']:.3f} seconds")

    stints = groupinglaps(lap_times, pit_stop_data)

    for i, stint in enumerate(stints, 1):
        print(f"Stint {i}: {stint}")


lapstr_toint()
