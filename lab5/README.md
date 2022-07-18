5. Created the dir my_app and then just copied all the contents from the repo . 
Checked requirements.txt , it had to install redis and flask . 

6.Ran the commands to init the pipenv , install the requirements dependancies and ran the python app which produced a redis not connected error for some reason . Tried troubleshooting , still couldnt find a reason for this error except resource exaustion but even flushing all info inside the DB didnt work... Via many tests I understood that firstly my flask app I had done previously was working and then even it stopped working . The app works within containers so it is something within the environment . 

The tests did not run as it was showing me unrecognized argument --url . 
It looks like pytest's new version does not allow that . 

Deleted the pipfiles . The site stopped working since flask was not installed .

7. The app did not run so there were no files for deletion .

8. The directive $(STATES) loops through the Dockerfile.app and Dockerfile.tests dependancy directives and then builds the docker image . The Dockerfile app creates the same app we were trying to run (with the flask and redis dependancies) but within a container . The tests dependancy creates another container , installs the requirements and runs the pytest command we were trying to run before .

docker run creates a bridge network appnet , then runs redis container within that network as well as the app container created during the STATES build .

Tests is about the tests container created during states build as well .

docker-prune just clears all containers/volumes/networks/images .

9. At first used only make and it just created the image app (it does not consider tests at all for some reason ) . That made me spent some hrs and I finally gave up trying to rewrite it so it can work and just did these in 2 different dependancies and bound them to the other dependancy directives and now it works as expected (just a bit bruteforcing) . 

<<<<<<< HEAD
10. The project was in detached mode so I had nothing to stop with ctrl+c so I just used make docker-prune to clean all the resources I created (although the images I created were not pruned but that is a specific of the docker prune command used in the makefile ) . 

11. I had previously updated the images to my dockerhub , but will just remove them and update them again . 10. The project was in detached mode so I had nothing to stop with ctrl+c so I just used make docker-prune to clean all the resources I created (although the images I created were not pruned but that is a specific of the docker prune command used in the makefile ) . 

11. I had previously updated the images to my dockerhub , but will just remove them and update them again . 10. The project was in detached mode so I had nothing to stop with ctrl+c so I just used make docker-prune to clean all the resources I created (although the images I created were not pruned but that is a specific of the docker prune command used in the makefile ) . 

11. I had previously updated the images to my dockerhub , but will just remove them and update them again . 10. The project was in detached mode so I had nothing to stop with ctrl+c so I just used make docker-prune to clean all the resources I created (although the images I created were not pruned but that is a specific of the docker prune command used in the makefile ) . 

11. I had previously updated the images to my dockerhub , but will just remove them and update them again . 10. The project was in detached mode so I had nothing to stop with ctrl+c so I just used make docker-prune to clean all the resources I created (although the images I created were not pruned but that is a specific of the docker prune command used in the makefile ) . 

11. I had previously updated the images to my dockerhub , but will just remove them and update them again . 10. The project was in detached mode so I had nothing to stop with ctrl+c so I just used make docker-prune to clean all the resources I created (although the images I created were not pruned but that is a specific of the docker prune command used in the makefile ) . 

11. I had previously updated the images to my dockerhub , but will just remove them and update them again . 10. The project was in detached mode so I had nothing to stop with ctrl+c so I just used make docker-prune to clean all the resources I created (although the images I created were not pruned but that is a specific of the docker prune command used in the makefile ) . 

11. I had previously updated the images to my dockerhub , but will just remove them and update them again . 10. The project was in detached mode so I had nothing to stop with ctrl+c so I just used make docker-prune to clean all the resources I created (although the images I created were not pruned but that is a specific of the docker prune command used in the makefile ) . 

11. I had previously updated the images to my dockerhub , but will just remove them and update them again . 10. The project was in detached mode so I had nothing to stop with ctrl+c so I just used make docker-prune to clean all the resources I created (although the images I created were not pruned but that is a specific of the docker prune command used in the makefile ) . 

11. I had previously updated the images to my dockerhub , but will just remove them and update them again . 10. The project was in detached mode so I had nothing to stop with ctrl+c so I just used make docker-prune to clean all the resources I created (although the images I created were not pruned but that is a specific of the docker prune command used in the makefile ) . 

11. I had previously updated the images to my dockerhub , but will just remove them and update them again using the makefile directive . 
=======

>>>>>>> fc3ace8 (lab5 initial commit)


