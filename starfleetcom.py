__author__ = 'mrasamny'

import random
import urllib2


def postImage(url,fileName):
    body= '';
    try:
        file = open(fileName,'rb')
        body = file.read()
        file.close()
    except OSError:
        return b''

    part_boundary = b'---------------------Boundary'+bytes(str(int(random.random()*1e10)),'utf-8')
    data = []
    data.append(b'--'+part_boundary)
    data.append(bytes('Content-Disposition: form-data; name="file"; filename="{}"'.format(fileName),'utf-8'))
    data.append(bytes('Content-Type: {}'.format('image/png'),'utf-8'))
    data.append(b'')
    data.append(body)
    data.append(b'--' + part_boundary + b'--')
    data.append(b'')
    body = b''
    for item in data:
        body += item + b'\r\n'

    request = urllib2.Request(url)
    # adding charset parameter to the Content-Type header.
    request.add_header("Content-Type","multipart/form-data;boundary={}".format(str(part_boundary)))
    request.add_header('Content-length', len(body))
    webHandle = urllib2.urlopen(request,body)
    reply = webHandle.read();
    webHandle.close()
    return reply

def deleteCommand(url):
    request = urllib2.Request(url)
    request.get_method = lambda: 'DELETE'
    webHandle = urllib2.urlopen(request)
    command = webHandle.read();
    webHandle.close()
    return command

def getCommand(url):
    request = urllib2.Request(url)
    webHandle = urllib2.urlopen(request)
    command = webHandle.read();
    webHandle.close()
    return command

if __name__=="__main__":
    url = 'http://localhost:8080/robot'
    #print(postImage(url,'/Users/mrasamny/Downloads/image2.jpg')) #example image post
    #cmdInJSONFormat = getCommand(url) # example command get
    #cmdInJSONFormat = deleteCommand(url) # example command delete
    # You will need to figure out how to convert a JSON object into a dictionary!
    