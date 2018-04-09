FROM python:2.7

RUN mkdir /usr/app
WORKDIR /usr/app
RUN wget http://www-us.apache.org/dist/zookeeper/zookeeper-3.4.11/zookeeper-3.4.11.tar.gz 
RUN tar xvf zookeeper-3.4.11.tar.gz 
RUN cd zookeeper-3.4.11/src/c/ && ./configure && make && make install && ldconfig 

COPY requirements.txt /usr/app/
RUN pip install --no-cache-dir -r requirements.txt
COPY pyzkcli.py /usr/app

ENTRYPOINT ["python", "pyzkcli.py"]
