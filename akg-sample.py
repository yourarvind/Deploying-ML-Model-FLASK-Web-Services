# ------------------------------------------------ 
# setup python based web services using FLASK
# Author: Arvind Kumar
# Email: arvind.cse@gmail.com
#-------------------------------------------------

from flask import Flask
from flask import request
from flask import jsonify
#import sys
#.......................................
app = Flask(__name__)
#.......................................
# http://localhost:5000/static/akg-hello.html
@app.route('/akg-hello',methods=['POST'])
def hello():
    message = request.get_json(force=True)
    name = message['name']
#    sys.stdout.flush()		
#    print(name, file=sys.stderr)
    response = {
            'greeting': 'Namaste, ' + name + ' Jee!'
    }
    
    return jsonify(response)
#.......................................
# http://localhost:5000/static/akg-sample
@app.route('/akg-sample')
def running():
    return 'Hello, Flask is running'
#.......................................
