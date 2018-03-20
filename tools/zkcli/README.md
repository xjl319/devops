# HOW TO USE

## build
```
    docker build -t pyzkcli .
```
## test
```
    docker run --rm --name zk-for-test -d -p 2181:2181 docker-registry:5000/zookeeper
    docker run --rm --link zk-for-test:zk -v `pwd`/zkimport.json:/usr/app/zkimport.json pyzkcli -i zkimport.json -z zk -p 2181
```
## USE
```
    echo '{ "global_vars_11" : { "hello" : "111" , "bbbb" : "222" } }' > a.json
    docker run --rm -v `pwd`/a.json:/usr/app/a.json docker-registry:5000/pyzkcli -i a.json -z zkserver -p 2181
```