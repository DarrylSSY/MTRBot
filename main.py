import csv
import random
import requests
import schedule
import time
from datetime import date, datetime
import pytz

timezone = pytz.timezone("Asia/Singapore")

def main():
    schedule.every().monday.at("13:05").do(automate_data)
    while True:
        schedule.run_pending()
        time.sleep(60)

def send_data(name, week, pushup, situp):
    url = 'https://docs.google.com/forms/u/0/d/e/1FAIpQLSeP9wociq9JAwWymcmXjOsIS0DcTDcPQ7_HYFQ1Tkm1I0fl-A/formResponse'
    data = {'entry.1653511189': name, 'entry.1794772023': week, 'entry.287396502': int(pushup), 'entry.1222094474': int(situp)}
    x = requests.post(url, data)
    print("Attempting to submit pushups of " + pushup + " and situps of " + situp + " to " + name + " at " + week)

def calculate_new_number(number):
    if number < 60 :
        return number + random.randrange(-1, 2)
    else:
        return number + random.randrange(-2, 1)
def automate_data():
    d = datetime.now()
    d_aware = timezone.localize(d)
    d_aware.tzinfo

    day = date.strftime(d, '%d/%m/%Y')


    print(day)
    week = "Week 12 (21/12 - 25/12)"
    if day == "21/12/2020":
        week = "Week 12 (21/12 - 25/12)"
    elif day == "28/12/2020":
        week = "Week 13 (28/12 - 1/1)"
    elif day == "4/1/2021":
        week = "Week 14 (4/1 - 8/1)"
    elif day == "11/1/2021":
        week = "Week 15 (11/1 - 15/1)"
    elif day == "18/1/2021":
        week = "Week 16 (18/1 - 22/1)"
    elif day == "25/1/2021":
        week = "Week 17 (25/1 - 29/1)"
    elif day == "1/2/2021":
        week = "Week 18 (1/2 - 5/2)"
    elif day == "8/2/2021":
        week = "Week 19 (8/2 - 12/2)"
    elif day == "15/2/2021":
        week = "Week 20 (15/2 - 19/2)"
    elif day == "22/2/2021":
        week = "Week 21 (22/2 - 26/2)"
    test = []
    usersSource = csv.reader(open('users.csv', "r", newline=""), delimiter=',')
    for row in usersSource:
        print(row)

    with open('users.csv', newline='') as csvfile:
        file = csv.reader(csvfile, delimiter=',')
        users = []
        for user in file:
            users.append(user)

    with open('users.csv', "w", newline='') as fout:
        csvwriter = csv.writer(fout, delimiter=',')
        for row in users:
            print(row)
            if row[0] != 'name':
                print(row)
                row[1] = str(calculate_new_number(int(row[2])))
                row[2] = str(calculate_new_number(int(row[2])))
                send_data(row[0], week, row[1], row[2])
            csvwriter.writerow(row)



main()


