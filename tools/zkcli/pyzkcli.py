# -*- coding:UTF-8 -*-
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')
from types import *
import pykeeper
import getopt
import sys
import json

def help():
    print("usage:")
    print("     pyzkcli -i a.json -z 127.0.0.1 -p 2181")
    print("     pyzkcli --import=a.json --zkhost=127.0.0.1 --zkport=2181")    
    pass

def zk_import(zk, s_json):
    for k, v in s_json.items():
        print "key=> ", k, " value=> ", v
        zk_set(zk, "/" + k, v)
    pass

def zk_set(zk, key, value):
    if type(value) is DictType:
        print "zk_set map => ", value
        for k, v in value.items():
            tosetKey = '/'.join([key, k])
            print tosetKey
            if not zk.exists(tosetKey):
                zk.create_recursive(tosetKey, '')
            zk_set(zk, tosetKey , v)
        return
        pass
    else:
        value = str(value)
        print "zk to set => ", key, ":", value
        if not zk.exists(key):
            zk.create_recursive(key, value)
        else:
            zk.set(key, value)
        return
        pass
    assert False, "unsupport type " + str(type(value))
    pass

def zk_dump(zk):
    zk_get(zk, '/')
    pass

def zk_get(zk, path):
    v = {}
    ret = zk.get(path)[0]
    print "key:value => ", path,":", ret
    children = zk.get_children(path)
    if len(children) > 0:
        for c in children:
            togetKey = '/'.join([path, c])
            if path is '/':
                togetKey = path + c
            # print "togetKey: ", togetKey
            zk_get(zk, togetKey)
        pass

    pass

if __name__ == '__main__':
    opts, _ = getopt.getopt(sys.argv[1:], "hi:z:p:", ["all", "help", "import=", "zkhost=", "zkport="])
    #print opts
    import_json = ""
    zk_host = '127.0.0.1'
    zk_port = '2181'
    for op, value in opts:
        if op in ("-h", "--help"):
            help()
            exit(1)
        if op in ("-i", "--import"):
            import_json = value
        elif op in ("-z", "--zkhost"):
            zk_host = value            
        elif op in ("-p", "--zkport"):
            zk_port = value   
        else:
            help()
            exit(1)
    
    if not import_json:
        help()
        exit(1)
            
    pykeeper.install_log_stream()
    client = pykeeper.ZooKeeper(":".join([zk_host, zk_port]))
    client.connect()

    data = json.load(open(import_json), "utf-8")
    zk_import(client, data)
    zk_dump(client)

    pass
