1
-----------------------------------
command used to clone the repo :
git clone https://github.com/BobasB/devops_course.git

2
-----------------------------------
git log 

Author: Mario <ma.advo@abv.bg>
Date:   Tue Jul 12 17:02:12 2022 +0300

    Lab_1 first commit

commit 73bdc448c6d844302f4e7ae1e5d12aa96d7671c6 (origin/master, origin/HEAD)
Author: bbuhyl <bbuhyl@cisco.com>
Date:   Sat Dec 4 16:30:34 2021 +0200

3
------------------------------------
here 2 commands can be used to make a new branch (and to switch to it):

git branch <name> + git checkout <name>
git checkout -b <name> , which will do both 

4
-----------------------------------
The changes are missing in master since we are working in another branch right now . Fixed that with git merge new_branch which is the name of the branch I worked in . 

6
--------------------------------------------
just saw that the merge request had to be done in the 6 task so I messed it a bit by doing it earlier . Will skip this as it is done and described in the readme log above . Command used git checkout master , git merge new_branch

7
--------------------------------------------
There was no conflict after the merge of new_branch into master . 

8
--------------------------------------------
make dir lab1 , (I also had to delete the previously created ones)
put README file into the lab1 dir .

9
--------------------------------------------
edited the file , used git pull to sync the local repo with the remote one . Also had to commit the changes I had done to the local repo before that so I could have been able to pull . 

10
---------------------------------------------
![TEXT TO SHOW ... ](/Users/mario/testScripts/photo.jpeg "Text mouseover")








