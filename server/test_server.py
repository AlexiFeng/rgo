from flask import Flask
import os
import json
app = Flask(__name__)

@app.route('/app/<appid>/about')
def about(appid):
    return 'A Test'+appid

@app.route('/app/<lang>/<appid>/')
def execute(lang,appid):
    if lang is "python2":
      c=os.popen("python2 "+appid+".py").read()
    else:
      c=os.popen("python3 "+appid+".py").read()[:-1]
    return json.dumps(c)

if __name__ == '__main__':
    app.run()