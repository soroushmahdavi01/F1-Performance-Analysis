# I want to create a program that allows peopel to see performance average increase between teams thorught the years
# Example Force India Racing point 2019/2020 increase dramticly between the two, count the first race and the last race or the average pace increases. 
# so 2019 their average pace was 1:19 for thes first race and 1:17 in the next years race for  opening so a 25% increase in pace, now we take that over 25 races and average the overall pace we would get 20 % increase,
#https://documenter.getpostman.com/view/11586746/SztEa7bL#46c7fbee-e90f-409f-b2ff-d8b77e85e5f6
#https://ergast.com/mrd/


import requests
import tkinter as tk
import pandas as pd
import json

while True:
    team_a_year = 2021
    team_a_constructor = "red bull"
    team_a_constructor = '_'.join(team_a_constructor.split())
    url = f"https://ergast.com/api/f1/{team_a_year}/constructors/{team_a_constructor}/qualifying.json"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    data = json.loads(response.text)
    df = pd.json_normalize(data["MRData"]["RaceTable"]["Races"])
    print(df)


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



