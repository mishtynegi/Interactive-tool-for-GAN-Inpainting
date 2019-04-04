# -*- coding: utf-8 -*-
import bottle
from bottle import route, run, template, request, response, static_file
import base64
import os

bottle.BaseRequest.MEMFILE_MAX = 1024 * 1024 # (or whatever you want)
app = bottle.app()

@app.hook('after_request')
def enable_cors():
        # set CORS headers
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Headers'] = 'Access-Control-*, Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token, Cache-Control, X-File-Name, If-Modified-Since, User-Agent, Depth, X-File-Size'
    response.headers['Access-Control-Expose-Headers'] = 'Access-Control-*'
    print(response)

@app.route('/static/<filename:path>', method=['OPTIONS', 'GET'])
def send_static(filename):
    return static_file(filename, root='data')

@app.route('/home/<filename:path>')
def index(filename):
    return static_file(filename, root='views')

@app.route('/inpaint', method=['OPTIONS', 'POST'])
def inpaint():
    data = request.json

    model = data['model']

    inputData = base64.b64decode(data['input'])
    inputFile = './input.png'
    with open(inputFile, 'wb') as f:
        f.write(inputData)

    maskData = base64.b64decode(data['mask'])
    maskFile = './mask.png'
    with open(maskFile, 'wb') as f:
        f.write(maskData)

    command = 'python test.py' + ' --image ' + inputFile +  ' --mask ' + maskFile + ' --output ./output.png' +  ' --checkpoint ./model_logs/' + model
    os.system(command)

    with open("./output.png", "rb") as image_file:
        output = base64.b64encode(image_file.read())

    return output

@app.route('/styleTransfer', method=['OPTIONS', 'POST'])
def styleTransfer():
    data = request.json

    inputAData = base64.b64decode(data['inputA'])
    inputAFile = './inputA.png'
    with open(inputAFile, 'wb') as f:
        f.write(inputAData)

    inputBData = base64.b64decode(data['inputB'])
    inputBFile = './inputB.png'
    with open(inputBFile, 'wb') as f:
        f.write(inputBData)

    command = 'python inpaint_ops.py' + ' --imageA ' + inputAFile +  ' --imageB ' + inputBFile + ' --imageOut ./output2.png'
    os.system(command)

    with open("./output2.png", "rb") as image_file:
        output2 = base64.b64encode(image_file.read())

    return output2

app.run(host='localhost', port=8080)
