# cloudcomputingproject

Steps

1.	Create EMR Cluster on AWS Console
2.	Associate the .pem key to the EMR Cluster
3.	Enable SSH Traffic in the Inbound Rule in the security group.
4.	Connect the Master EC2 instance from the terminal
      $ chmod 400 Final.pem
      $ ssh -i "Final.pem" hadoop@ec2-3-235-147-82.compute-1.amazonaws.com
5.	Create the Python file to execute the F1 Score
      $ nano ProgrammingAssignment2.py
6.	Install and Run the following files
      $ sudo pip install --upgrade pip
      $ sudo apt-get install python3
      $ sudo  pip install pyspark
      $ sudo pip install wheel
      $ sudo pip install pyspark --no-cache-dir
      $ sudo pip install findspark
      $ sudo pip install numpy
      $ sudo apt install python3-pip
7.	Create a Docker account on Docker Hub
8.	Build the Docker on EC2 Instance and create the image of the Docker
      $ nano Dock
      $ sudo service docker start
      $ sudo docker build . -f Dock -t yes
      $ sudo docker run yes
      $ sudo docker build . -f Dock -t ianrokz/programmingassignment2

9.	Run the image of the Docker within the Docker Hub on EC2 Instance
      $ sudo docker run -t ianrokz/programmingassignment2
      $ sudo docker login -u ianrokz
      $ sudo docker push ianrokz/programmingassignment2

10.	Check if the push was successful in the Docker Hub account.

