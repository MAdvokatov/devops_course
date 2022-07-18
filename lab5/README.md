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

10. The project was in detached mode so I had nothing to stop with ctrl+c so I just used make docker-prune to clean all the resources I created (although the images I created were not pruned but that is a specific of the docker prune command used in the makefile ) . 

11: Modified the Makefile so it could update the images to my repo in Dockerhub.

This is my directive.

docker-push:
        @docker push $(REPO):$(STATE)
        @docker push $(REPO):$(STATE_TEST)

12. Made another makefile directive to delete all possible images locally : 

docker-image-remove:
        @docker rmi $$(docker images -a -q) --force

13. Checked the docker-compose yaml file and the networks are needed so the containers can be put in the same network so they can establish a communication between each other . the app will be in both networks created with names public and secret. tests will be only in the public one and redis will be only in the secret network . I have updated the repo names as well . 

14. Ran docker compose successfully

15. The website works and it is on port 80 since port 80 on my local machine is mapped to port 5000 that is running the flask app on the container . 

    ports:
      - 80:5000

So port 80 is taken by default by the browsers and the url the site is reachable on is either 127.0.0.1 , localhost(only if mapped to the loopback address via the hosts file (set by default , but who knows) . ) and 0.0.0.0 .  

16. Yes , docker compose recreated the 2 images and pulled the redis one from the internet . The tags are what I have set in the docker-compose file (madvokatov/devops_course:compose-app and compose-tests) . The docker-prune directive in the makefile was using docker image prune to clear all images with no tag . 

17. DONE . However docker-compose down just removed the containers as well as the networks . The images are still there as well as the volumes . 

18. Used docker-compose push to upload everything to dockerhub. 

19. The makefile is more powerfull than docker-compose , but it takes more time to initially set everything there , after that it will save that time .

20 Did the docker-compose.yml using the syntax from this lab's docker-compose and it works for the django app , however when both containers are placed within the django-net network , the monitoring app is not working again . 

It worked when the monitoring app was placed on the host network as it was requesting the url localhost:8000/health which was within the host's subnet . Will try with docker network inspect to see the range of the network within the network I created django-network in which is the django app and will try to make the monitoring app run within it somehow (but I suppose I will have to update the monitoring app as it will need to connect to it as well ) . It would work if I modify the monitoring in the lab3 dir so the url would be 172.31.0.3 which I fould was always assigned to the django app and I would have added it to the allowed hosts in settings . But I also had to push that to github so dockerfiles could have pulled the updated version so I decided not to mess up my proj as this was not part of the task so skipping , main task is done . 

version: '3.7'
services:
  server:
    build:
      context: /Users/mario/test/devops_course/lab4
      dockerfile: Dockerfile
    image: marioadvokatov/devops_course:django-compose
    container_name: django-composed
    networks:
      - django-net
    ports:
      - "8000:8000"

  monitoring:
    build:
      context: /Users/mario/test/devops_course/lab4
      dockerfile: Dockerfile.site
    image: madvokatov/devops_course:monitoring-compose
    container_name: monitoring-composed
    network_mode: host

networks:
  django-net:
    driver: bridge 
