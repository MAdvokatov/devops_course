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

TASK 9 - > Wrote a simple test to check if the return value of the command is equal to GOOD DAY , which in my case will fail as it was showing AM before when I tried it . 

def test_task_9_DAY(self):
        url = "http://date.jsontest.com/"
        r = requests.get(url=url)
        self.assertEqual(check_day_or_night(r.json()), "GOOD DAY")

TASK 10 - > The command I used was: 
	pytest tests/tests.py > results.txt || python3 app.py >> results.txt

#used python3 instead of python as I have an alias for python 10 as python and the project here uses 3.7 (as per the initial installation for pipenv) .
 

TASK 11 - > Committed and pushed .

TASK 12 - > Updated the Makefile so it can go through all the steps automatically . 

TASK 13 - > Will commit and push to the repo again so I can clone it after that on the Ubuntu(I created an AWS instance as it is quicker than a new virtual box)




