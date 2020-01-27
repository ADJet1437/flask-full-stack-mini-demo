FROM ubuntu:18.04

RUN apt-get update -y && apt-get install python-pip python-dev -y

WORKDIR /klarna_assignment

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . /klarna_assignment

CMD ["python" , "start_app.py" ]