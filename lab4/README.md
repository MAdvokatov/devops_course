1. Checked the docs of Docker.

2. I had installed Docker previously so I had it and the tests for version and help went through fine . Also got the remote image whalesay and tested it as it was described in the task . Also redirected the output of the commands in my_work.log and committed .

3. Checked the Dockerfile docs . 

4.Pulled the image , then removed it so I dont have it locally so the Dockerfile could have pulled it .

Created the Dockerfile , copied the contents from Bohdan's Dockerfile and updated what was necessary to point it to my repo .

5. I already had a dockerhub acct so I just created a new repo .

6. Built the image as madvokatov/devops_course:django

Path to it https://hub.docker.com/repository/docker/madvokatov/devops_course

Logged in with docker login and pushed the image I have created into dockerhub repo . 

7. Started the website successfully, but decided to make it on port 8080 instead of 8000 .  

Went to localhost:8080 and it works.

8. Created a 2nd dockerfile named Dockerfile.site which was building my image for the monitoring app . 

Given tag monitoring(even before that :) , just got lucky about the name as I dont have to change it again ) 

launched both containers simultaneously and they work for now , I created a docker network so I could have been sure they would have been placed in the same network so they can communicate to each other . I used port 8080 on my machine and port 8000 on the docker network for the container with django and used port 8000 on my machine and port 8001 on the docker network for the container with the monitoring app . Now I have to exec to get into the monitoring one to see if it writes correctly to the server.log file . 

Edit : Looks like they cant talk to each other for some reason . Will troubleshoot now .

They were unable to talk even when put in the same network , but I found out that the monitoring app was checking on localhost:8000/health and I had run that on localhost:8080/health and thats why it was not working .However , after I fixed the django app to work on port 8000 and I have set the monitoring one to work on 8001 , it was still not working . I used --net=host on the monitoring app so it would work as suggested , however I will try to put the containers and make them work without specifying the key --net=host for monitoring. 
Couldnt make it work without --net=host . Will leave it as it is . 


used this command to mount the volumes : docker run -it --name=monitoring --rm -p 8001:8000 --net=host -v /Users/mario/test/devops_course/lab4/server.log:/app/server.log  madvokatov/devops_course:monitoring 




