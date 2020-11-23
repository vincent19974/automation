1. Create docker image with library dependencies needed. 

Eg. : 

 

#!/bin/bash 

FROM python:3.8 

WORKDIR /code 

RUN apt update 

RUN pip3 install pandas 

RUN pip3 install pyhive 

RUN pip3 install wheel 

RUN pip3 install thrift 

RUN yes | apt-get install python-dev libsasl2-dev gcc 

RUN pip3 install thrift-sasl 

RUN pip install cassandra-driver 

RUN pip install boto3 

#CMD ["python3", "test.py"] 

 
2. make your docker image a tar file. 

> sudo docker save -o <path for generated tar file> <image name> 

 
3. Download your docker image to desired s3 bucket 
4. make a shell script and download it as well into the s3 bucket for bootstrapping process containing command: 
#~: 
#! /bin/bash 
aws s3 cp s3://path/for/docker.tar /home/hadoop 
 

5. Create cluster and make a bootstrap action>custom action and load the created script on your s3 bucket. Docker command: 
6. wait 23-25 minutes for bootstrapping depending on the image size/memory size. 
7. now if emr cluster already created, ssh on the terminal and load the docker.tar. 

Enter command to load docker image: 

 

 
Note: make sure the docker is already installed already started. to check, enter command.  
> docker - -version. 

 
8. assuming docker is already installed already started. enter command to load the docker tar file: 
> #~:  docker load -i <path to image tar file> 
wait a few minutes for loading the docker. 

 
9. check if docker images is already created: 
> sudo docker images 
10. run your docker image first: 
> sudo docker run -t -d <container_imageid> 
11. now start docker image: 
>sudo docker exec -it <container_id> /bin/bashDone, you can check the dependencies/software you downloaded on the docker Image. 

 

 

 

Done, you can check the dependencies/software you downloaded on the docker Image. 
