# I want to create a program that allows peopel to see performance average increase between teams thorught the years
# Example Force India Racing point 2019/2020 increase dramticly between the two, count the first race and the last race or the average pace increases. 
# so 2019 their average pace was 1:19 for thes first race and 1:17 in the next years race for  opening so a 25% increase in pace, now we take that over 25 races and average the overall pace we would get 20 % increase,
#https://documenter.getpostman.com/view/11586746/SztEa7bL#46c7fbee-e90f-409f-b2ff-d8b77e85e5f6
#https://ergast.com/mrd/


import requests
# import xml.etree.ElementTree as ET
# tree = ET.parse("http://ergast.com/api/f1/2021/21/qualifying")
# root = tree.getroot()
url = "http://ergast.com/api/f1/2021/21/qualifying"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

# def parse_request_driver_qualifying():
#     url = "http://ergast.com/api/f1/2021/21/qualifying"
#     payload={}
#     headers = {}
#     response = requests.request("GET", url, headers=headers, data=payload)
#     for data in response:
#         new_recipie = Recipie(
#             recipe["name"],
#             recipe["ingredients"],
#             recipe["calories"],
#             recipe["protein"],
#             recipe["difficulty"],
#             recipe["link"],
#             recipe["time"]
#         )
#         ALL_LIST.append(new_recipie)
