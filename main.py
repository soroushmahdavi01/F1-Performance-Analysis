# I want to create a program that allows peopel to see performance average increase between teams thorught the years
# Example Force India Racing point 2019/2020 increase dramticly between the two, count the first race and the last race or the average pace increases. 
# so 2019 their average pace was 1:19 for thes first race and 1:17 in the next years race for  opening so a 25% increase in pace, now we take that over 25 races and average the overall pace we would get 20 % increase,
#https://documenter.getpostman.com/view/11586746/SztEa7bL#46c7fbee-e90f-409f-b2ff-d8b77e85e5f6
#https://ergast.com/mrd/

import csv
# x = "948"
driver_list = {}
race_list = {}
def parse_qualifying_times():
    with open('data/drivers.csv','r', encoding="utf8") as drivers_file:
        drivers_reader = csv.DictReader(drivers_file)
        for line in drivers_reader:
            driver_list[line['driverId']]=line['forename'] + " " + line['surname']
    with open('data/races.csv','r', encoding="utf8") as races_file:
        races_reader = csv.DictReader(races_file)
        for line in races_reader:
            race_list[line['raceId']]=line['year'] + " " + line["name"]
    with open('data/qualifying.csv', 'r') as qualifying_file:
        qualifying_reader = csv.DictReader(qualifying_file)
        for line in qualifying_reader:
            # if line["raceId"] >= x:
                print(race_list[line['raceId']],driver_list[line['driverId']],line['q1'])



