TASK 2 - > pipenv was already installed as I worked with it before I started these labs . 

TASK 3 - > installed pyenv on my machine and used python3.7.13 to create the virtual env. 

TASK 4 - > Followed the steps . 

TASK 5 - > The app is running normally. 

TASK 6 - > Installed Pytest inside the virtual env. 

TASK 7 - > All 5 tests went normally .

TASK 8 - > At first I implemented the solution in the existing function , then used translator and it was showing me I had to create a new function to show day/night so I created this piece of code and then invoked the function in the main.

def check_day_or_night(d):
    if "time" in d.keys():
        day = "PM"
        night = "AM"
        if day in d['time']:
            print("GOOD DAY")
        elif night in d['time']:
            print("GOOD NIGHT")






