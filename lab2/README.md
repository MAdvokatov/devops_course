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

TASK 14 - > I had to install make as it was not installed on the ec2 ubuntu instance . The main issue here was that I built my makefile on a Mac OS with brew as packed manager so I had to update that to apt for ubuntu . Also had to run apt-get update before that  
After trying for 1.30h many many issues appeared on the ubuntu offered by AWS and finally , the last issue I encountered was related to the requests module and 

pipenv install requests
/home/ubuntu/.local/lib/python3.10/site-packages/pkg_resources/__init__.py:123: PkgResourcesDeprecationWarning: 1.1build1 is an invalid version and will not be supported in a future release
  warnings.warn(
/home/ubuntu/.local/lib/python3.10/site-packages/pkg_resources/__init__.py:123: PkgResourcesDeprecationWarning: 0.1.43ubuntu1 is an invalid version and will not be supported in a future release
  warnings.warn(
Installing requests...
⠋ Installing...Failed to load paths: Traceback (most recent call last):
  File "<string>", line 1, in <module>
ModuleNotFoundError: No module named 'distutils.sysconfig'

Output:
⠙ Installing requests...Failed to load paths: Traceback (most recent call last):
  File "<string>", line 1, in <module>
ModuleNotFoundError: No module named 'distutils.sysconfig'

Output:
Failed to load paths: Traceback (most recent call last):
  File "<string>", line 1, in <module>
ModuleNotFoundError: No module named 'distutils.sysconfig'

Output:
Error:  An error occurred while installing requests!
Error text:
Traceback (most recent call last):
  File "/usr/lib/python3.7/runpy.py", line 193, in _run_module_as_main
    "__main__", mod_spec)
  File "/usr/lib/python3.7/runpy.py", line 85, in _run_code
    exec(code, run_globals)
  File "/home/ubuntu/.local/share/virtualenvs/lab2-whCfRT2V/lib/python3.7/site-packages/pip/__main__.py", line 29, in <module>
    from pip._internal.cli.main import main as _main
  File "/home/ubuntu/.local/share/virtualenvs/lab2-whCfRT2V/lib/python3.7/site-packages/pip/_internal/cli/main.py", line 9, in <module>
    from pip._internal.cli.autocompletion import autocomplete
  File "/home/ubuntu/.local/share/virtualenvs/lab2-whCfRT2V/lib/python3.7/site-packages/pip/_internal/cli/autocompletion.py", line 10, in <module>
    from pip._internal.cli.main_parser import create_main_parser
  File "/home/ubuntu/.local/share/virtualenvs/lab2-whCfRT2V/lib/python3.7/site-packages/pip/_internal/cli/main_parser.py", line 8, in <module>
    from pip._internal.cli import cmdoptions
  File "/home/ubuntu/.local/share/virtualenvs/lab2-whCfRT2V/lib/python3.7/site-packages/pip/_internal/cli/cmdoptions.py", line 23, in <module>
    from pip._internal.cli.parser import ConfigOptionParser
  File "/home/ubuntu/.local/share/virtualenvs/lab2-whCfRT2V/lib/python3.7/site-packages/pip/_internal/cli/parser.py", line 12, in <module>
    from pip._internal.configuration import Configuration, ConfigurationError
  File "/home/ubuntu/.local/share/virtualenvs/lab2-whCfRT2V/lib/python3.7/site-packages/pip/_internal/configuration.py", line 26, in <module>
    from pip._internal.utils.logging import getLogger
  File "/home/ubuntu/.local/share/virtualenvs/lab2-whCfRT2V/lib/python3.7/site-packages/pip/_internal/utils/logging.py", line 27, in <module>
    from pip._internal.utils.misc import ensure_dir
  File "/home/ubuntu/.local/share/virtualenvs/lab2-whCfRT2V/lib/python3.7/site-packages/pip/_internal/utils/misc.py", line 39, in <module>
    from pip._internal.locations import get_major_minor_version
  File "/home/ubuntu/.local/share/virtualenvs/lab2-whCfRT2V/lib/python3.7/site-packages/pip/_internal/locations/__init__.py", line 14, in <module>
    from . import _distutils, _sysconfig
  File "/home/ubuntu/.local/share/virtualenvs/lab2-whCfRT2V/lib/python3.7/site-packages/pip/_internal/locations/_distutils.py", line 9, in <module>
    from distutils.cmd import Command as DistutilsCommand
ModuleNotFoundError: No module named 'distutils.cmd'
