# I want to create a program that allows peopel to see performance average increase
# between teams thorught the years
# Example Force India Racing point 2019/2020 increase dramticly between the
# two, count the first race and the last race or the average pace increases.
# so 2019 their average pace was 1:19 for thes first race and 1:17 in the next
# years race for  opening so a 25% increase in pace, now we take that over 25 races and average the overall pace we would get 20 % increase,
# https://documenter.getpostman.com/view/11586746/SztEa7bL#46c7fbee-e90f-409f-b2ff-d8b77e85e5f6
# https://ergast.com/mrd/


import requests
import tkinter as tk
import pandas as pd
import json

race_time_list = [] 
average_time_list = []

# TODO: #1 Make the ^ variable names dynamic

def create_db(year, constructor):
    team_a_year = year
    team_a_constructor = constructor
    team_a_constructor = '_'.join(team_a_constructor.split())
    url = f"https://ergast.com/api/f1/{team_a_year}/constructors/{team_a_constructor}/qualifying.json"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    data = json.loads(response.text)
    df = pd.json_normalize(data["MRData"]["RaceTable"]["Races"])
    return df


def pull_driver_times(team, i):
    driver1_list = []
    driver2_list = []
    try:
        driver1_q3 = team.QualifyingResults[i][0]["Q3"]
        driver1_list.append(driver1_q3)
    except KeyError:
        try:
            driver1_q2 = team.QualifyingResults[i][0]["Q2"]
        except KeyError:
            driver1_q1 = team.QualifyingResults[i][0]["Q1"]
        except IndexError:
            pass
    except IndexError:
        pass
    try:
        driver1_q2 = team.QualifyingResults[i][0]["Q2"]
        driver1_list.append(driver1_q2)
    except KeyError:
        pass
    except IndexError:
            pass
    try:
        driver1_q1 = team.QualifyingResults[i][0]["Q1"]
        driver1_list.append(driver1_q1)
    except KeyError:
        pass
    except IndexError:
            pass
    #####
    try:
        driver2_q3 = team.QualifyingResults[i][1]["Q3"]
        driver2_list.append(driver2_q3)
    except KeyError:
        try:
            driver2_q2 = team.QualifyingResults[i][1]["Q2"]
        except KeyError:
            driver2_q1 = team.QualifyingResults[i][1]["Q1"]
        except IndexError:
            pass
    except IndexError:
            pass
    try:
        driver2_q2 = team.QualifyingResults[i][1]["Q2"]
        driver2_list.append(driver2_q2)
    except KeyError:
        pass     
    except IndexError:
            pass
    try:
        driver2_q1 = team.QualifyingResults[i][1]["Q1"]
        driver2_list.append(driver2_q1) 
    except KeyError:
        pass
    except IndexError:
            pass
    
    # Make this a dictonary?
    return driver1_list,driver2_list

def driver_fastest_lap(driver1_list, driver2_list):
    driver1_list_seconds = []
    for i in driver1_list:
        x = i[0]
        x = int(x) * 60
        y = float(i[2:8])
        driver1_list_seconds.append(round(x+y, 3))
    driver2_list_seconds = []
    for i in driver2_list:
        x = i[0]
        x = int(x) * 60
        y = float(i[2:8])
        driver2_list_seconds.append(round(x+y, 3))
    return(min(driver1_list_seconds),min(driver2_list_seconds))
   

def calcualte_average_time(race_time_list):
    for i in race_time_list:
        x = i[0]
        x = int(x) * 60
        y = float(i[2:8])
        average_time_list.append(round(x+y, 3))
    g = 0
    for i in average_time_list:
        g += i
    g = g/len(average_time_list)
    return g

def year_fastest_times(db):
    x=True
    i=0
    c=1
    year_fastest = []
    while x:   
        try:
            driver1, driver2 = pull_driver_times(db,i)
            year_fastest.append(min(driver_fastest_lap(driver1,driver2)))
            i+=1
            c+=1
        except KeyError:
            x=False
    return year_fastest



Hass_DB_2022 = create_db(2022, "Haas")
print(year_fastest_times(Hass_DB_2022))
mclaren2022 = create_db(2022, "Mclaren")
print(year_fastest_times(mclaren2022))

# print(Hass_DB_2022)
# print(Hass_Driver_1_2022)
# print(Hass_Driver_2_2022)

# print(min(driver_fastest_lap(Hass_Driver_1_2022,Hass_Driver_2_2022)))





# RedBull_DB_2022 = create_db(2022, "Redbull")
# RedBull_Driver_1, RedBull_Driver_2 = pull_driver_times(RedBull_DB_2022, 0)

# mercedes_db_2022 = create_db(2022, "mercedes")
# mercedes_driver_1, mercedes_driver_2 = pull_driver_times(mercedes_db_2022, 0)

# averg = calcualte_average_time(race_time_list)

# print(RedBull_Driver_1/averg)

# print(RedBull_DB_2022)
# print(average_time_list)
# print(round(averg, 4))
# df.columns.get_loc("salary")

# merged = pd.merge(qualifying_db,drivers_db, on="driverId",how='left')
# merged = pd.merge(constructors_db, merged, how='left')

# root= tk.Tk()
# canvas1 = tk.Canvas(root, width = 400, height = 300)
# canvas1.pack()

# year = tk.Entry (root)
# canvas1.create_window(200, 140, window=year)

# button1 = tk.Button(text='Start F1 Performance Analysis', command=parse_qualifying_times)
# canvas1.create_window(200, 180, window=button1)

# root.mainloop()


# driver_list = {}
# race_list = {}
# constructors_list = {}
# qualifying_list = []
