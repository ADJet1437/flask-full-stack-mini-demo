
## Getting Started
Download the code and place somewhere on your machine, for example, /home/

```bash
cd /home/klarna_assignment
```
#### If you do not have docker installed
If you do not want some packages installing on your local environment, I would recommend install `virtualenv`. (Following this link https://virtualenvwrapper.readthedocs.io/en/latest/ to setup your own virtual environment). It's also fine if you do not want a virtual environment, just run the following commands directly.

```bash
pip install -r requirements.txt
```
```bash
python start_app.py
```
And then checkout your browser http://localhost:5000/

#### If you have docker installed (recommended)
(Note that `flask-db` instance only running in docker container)
```bash
docker-compose build
```
```bash
docker-compose up -d
```
And then checkout your browser http://localhost:5000/

## Overview
This project has 3 features:

###web_app

The main thing of this assignment. It uses `Flask` as the base framework, with `bootstrap` 
 integrated on frontend. web_app provides 3 mathematical calculations, which are `Ackermann` function, `Factorial` of 
 non-negative integer, and `Fibonacci` sequence respectively. The functions are implemented in **models** directory.
 
 ### tests
 Testing is considered as a fundamental need of every programming project. In this project, I created 3 test 
 functions in `test_models.py` to test algorithms. For example, to test the general formula of `fibonacci` sequence, I
 compared the general formula with the standard function of `sympy` library in the function `test_fibonacci_general_formula`.

### mysql 
In this case, database is not mandatory, or it's more for **future** usage. The current consideration of database 
 is more from an architecture point of view. A potential need of database for this project which I might think about is 
 **cache warming**. Because when input values are big, it may cause long time to get a response. Hence, pre-calculate 
 results with big values and store in database is kind of a solution. But calculating big results is also a challenge of 
 this project, unfortunately, I am not managed to do that, further big data technologies may apply, and this is also the
 TODO list of this project. Another scenario that may touch database is that, we do not want to hardcoded front elements
 in html files, you may want to control data in database to control the front layout. This is more applied in frontend frameworks
 like `Angular` and `React` etc., these frameworks are more about data oriented. **In this project, I would just show how I 
 prepare data in database.**, which is run the following command after all containers are up.
 ```bash
docker-compose run flask-app python database/db.py
```
To verify data have been inserted, on your local machine, run:
```bash
mysql -uroot -ppassword -P3303 -h127.0.0.1
```
When you are inside mysql terminal:
```
mysql> USE front;
mysql> SELECT * FROM templates;
```
Output similar like this:
```bash
+----+-----------+-------------------------+---------------------+
| id | title     | small_title             | create_time         |
+----+-----------+-------------------------+---------------------+
|  1 | New title |  New custom small title | 2019-12-25 19:14:37 |
+----+-----------+-------------------------+---------------------+
1 row in set (0,00 sec)
```


## About frameworks

### Flask
Flask is a python framework for full stack web development.

Alternately, another popular architecture is api + frontend frameworks, such as using `falcon` + `Angular` (etc.) to 
separate frontend and backend. Considering we have small services to provide, in this project, I would use `Flask` to 
connect frontend and backend stacks.


### Bootstrap
Bootstrap is a frontend framework that helps to beautify your web page a lot. It provides many predefined classes
for each tag element, thus you can easily use without specifying formatting for elements using `css`.

Consider viewing from different devices, screen size will change from equipment to equipment.
Thus, Bootstrap will help you with displaying responsively. 

A simple usage example of this project is when you shrink your browser window size, the text
will also shrink their size accordingly. Press `F12` and change the screen size to test it.


### Docker
There is a trend of application containerization. Package all environment inside a container and run applications is more
portable because containers are isolated. 

This project has 2 services in `docker-compose`, `flask-app` is responsible for all the web app services 
 and the `flask-db` is the backend `mysql` database service. 
 
 To investigate the `flask-app` containers, run the following command:
 ```bash
docker-compose stop flask-app
```
```bash
docker-compose run flask-app bash
``` 
Then you will be inside a container as a `root`. You may want to ping another container to check the communication. 
Install `ping` first:
```bash
apt update && apt install iputils.ping -y
```
After installed, 
```bash
ping flask-db
```
Then you will see the ping output message similar like this
```bash
64 bytes from klarna_assignment_flask-db_1.klarna_assignment_default (172.20.0.2): icmp_seq=1 ttl=64 time=0.217 ms
64 bytes from klarna_assignment_flask-db_1.klarna_assignment_default (172.20.0.2): icmp_seq=2 ttl=64 time=0.249 ms
64 bytes from klarna_assignment_flask-db_1.klarna_assignment_default (172.20.0.2): icmp_seq=3 ttl=64 time=0.139 ms
64 bytes from klarna_assignment_flask-db_1.klarna_assignment_default (172.20.0.2): icmp_seq=4 ttl=64 time=0.138 ms
64 bytes from klarna_assignment_flask-db_1.klarna_assignment_default (172.20.0.2): icmp_seq=5 ttl=64 time=0.157 ms
64 bytes from klarna_assignment_flask-db_1.klarna_assignment_default (172.20.0.2): icmp_seq=6 ttl=64 time=0.220 ms
```
Exit the container
```bash
exit
```

To bring down all your containers, run:
```bash
docker-compose down
```
To check containers status,
```bash
docker-compose ps
```
You can also only bring one container up, run:
```bash
docker-compose up flask-app -d
```
`d` is the detached mode, if you want to see output, you can also 
run it without `d` argument, that is
```bash
docker-compose up flask-app
```

## Test
If you are not using docker and have installed the requirements.txt.
In `klarna_assignment` directory, run:
```bash
py.test tests/ -m function --cache-clear
```
Docker way:
```bash
docker-compose run flask-app py.test tests/ -m function --cache-clear
```
If you see **.pyc files in your directory, better to remove them to run the test. That is:
```bash
docker-compose run flask-app rm tests/__init__.pyc  && py.test tests/ -m function --cache-clear
```

### Other TODO list
* CI / CD
* Nginx


## Author

**Zijie Liang** - *liangzijie1437@gmail.com*
